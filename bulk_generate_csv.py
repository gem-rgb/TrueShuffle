import os
import csv
import random

os.makedirs('backend/data_chunks', exist_ok=True)

# We want roughly 400MB of data. We'll create 8 CSV files, 50MB each.
# Each row will be an id and 128 float values (an embedding vector)
# A row with 128 floats will be roughly 1000 bytes.
# 50MB = 50,000,000 bytes. So 50,000 rows per file.

for i in range(8):
    filename = f'backend/data_chunks/audio_embeddings_{i:03d}.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        # Header
        writer.writerow(['track_id'] + [f'feature_{j}' for j in range(128)])
        for row_idx in range(50000):
            track_id = f'trk_{i}_{row_idx:06d}'
            features = [round(random.gauss(0, 1), 6) for _ in range(128)]
            writer.writerow([track_id] + features)
    print(f'Created {filename}')
