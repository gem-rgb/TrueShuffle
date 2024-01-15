import os
import random
import string
import json

os.makedirs('backend/data_chunks', exist_ok=True)

music_tags = ['pop', 'hip-hop', 'drill', 'trap', 'afrobeats', 'reggaeton', 'amapiano', 'rnb', 'dancehall', 'soca']

for i in range(8):
    chunk_data = []
    for j in range(5000):
        track = {
            'track_uid': f'tr_{i}_{j:06d}_{"".join(random.choices(string.ascii_lowercase, k=10))}',
            'song_title': f'Song {random.randint(100, 99999)}',
            'performer': f'Performer {random.randint(1, 5000)}',
            'album_name': f'Album {random.randint(1, 2000)}',
            'length_ms': random.randint(60000, 600000),
            'global_popularity': round(random.random(), 5),
            'tags': random.sample(music_tags, random.randint(1, 4)),
            'bpm': round(random.uniform(60, 200), 1),
            'intensity': round(random.random(), 3),
            'dance_score': round(random.random(), 3),
            'mood_score': round(random.random(), 3),
            'acoustics': round(random.random(), 3),
            'vocals': round(random.random(), 3),
            'play_freq': random.randint(0, 1000000),
            'skip_freq': random.randint(0, 50000),
            'audio_signature': [round(random.gauss(0, 1), 5) for _ in range(512)],
            'frequency_bands': [round(random.uniform(-50, 50), 3) for _ in range(128)]
        }
        chunk_data.append(track)
    
    filename = f'backend/data_chunks/catalog_chunk_{i:03d}.json'
    with open(filename, 'w') as f:
        json.dump(chunk_data, f, indent=2)

print("Generated 50 new distinct data chunks.")
