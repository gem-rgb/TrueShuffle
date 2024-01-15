import os
import zipfile

source_dir = r"c:\Users\HomePC\Desktop\TrueShuffle"
output_filename = r"c:\Users\HomePC\Desktop\TrueShuffle_Submission.zip"
top_level_dir = "TrueShuffle"  # All files nested under this folder in the zip

if os.path.exists(output_filename):
    os.remove(output_filename)

excludes = ["node_modules", "dist", ".tools", "src-tauri\\target"]

with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_dir):
        # Mutate dirs in-place to skip excluded directories
        dirs[:] = [d for d in dirs if not any(x in os.path.join(root, d) for x in excludes)]
        
        for file in files:
            file_path = os.path.join(root, file)
            # Ensure timestamp is >= 1980 to avoid zipfile ValueError
            try:
                st = os.stat(file_path)
                if st.st_mtime < 315532800: # Jan 1, 1980
                    os.utime(file_path, (315532800, 315532800))
            except Exception:
                pass
                
            rel_path = os.path.relpath(file_path, source_dir)
            # Nest under top-level directory
            arc_name = os.path.join(top_level_dir, rel_path)
            zipf.write(file_path, arc_name)

print(f"Successfully created {output_filename}")
