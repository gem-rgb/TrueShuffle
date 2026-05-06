import os
import zipfile

source_dir = r"c:\Users\HomePC\Desktop\TrueShuffle_clean"
output_filename = r"c:\Users\HomePC\Desktop\TrueShuffle_Submission.zip"

if os.path.exists(output_filename):
    os.remove(output_filename)

excludes = ["node_modules", "dist", ".tools", "src-tauri\\target"]

with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if not any(x in os.path.join(root, d) for x in excludes)]
        
        for file in files:
            file_path = os.path.join(root, file)
            try:
                st = os.stat(file_path)
                if st.st_mtime < 315532800:
                    os.utime(file_path, (315532800, 315532800))
            except Exception:
                pass
                
            rel_path = os.path.relpath(file_path, source_dir)
            arc_name = os.path.join("TrueShuffle", rel_path)
            zipf.write(file_path, arc_name)

print(f"Successfully created {output_filename}")
