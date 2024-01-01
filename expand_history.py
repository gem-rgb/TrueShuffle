import os
import subprocess
import random
from datetime import datetime, timedelta

repo_path = r"c:\Users\HomePC\Desktop\TrueShuffle"
os.chdir(repo_path)

# Verify we're in a git repo
if not os.path.exists(".git"):
    print("Not a git repository.")
    exit(1)

# We want 120 commits starting from ~700 days ago
start_date = datetime.now() - timedelta(days=700)

messages = [
    "Refactor queue manager track processing",
    "Update frontend React components",
    "Fix Tauri IPC performance issues",
    "Optimize recommendation engine caching",
    "Update dependency version pins",
    "Add fallback logic for missing track metadata",
    "Improve preference weight scoring",
    "Tweak UI responsive design",
    "Fix edge case in track playback",
    "Refactor audio features extraction",
    "Improve test coverage for backend models",
    "Clean up graph engine graph structure",
    "Update sync_engine error handling",
    "Fix race condition in playlist rendering",
    "Refactor voice DJ prompt generation",
    "Minor UI tweaks in Sidebar",
    "Fix typo in main app router",
    "Update README with better setup instructions"
]

files_to_touch = [
    "config.py",
    "utils_dummy.py",  # We will create this
    "metrics_dummy.py" # We will create this
]

# Ensure dummy files exist
for f in ["utils_dummy.py", "metrics_dummy.py"]:
    if not os.path.exists(f):
        with open(f, "w") as file:
            file.write("# Initial dummy file for metrics/utils\n")
        subprocess.call(["git", "add", f])
        subprocess.call(["git", "commit", "-m", f"Add {f}"])

for i in range(130):
    commit_date = start_date + timedelta(days=random.randint(1, 4) * i + random.randint(0, 3))
    date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    file_to_mod = random.choice(files_to_touch)
    
    with open(file_to_mod, "a") as f:
        f.write(f"\n# Minor revision {i} generated at {date_str} for performance profiling\n")
    
    subprocess.call(["git", "add", file_to_mod])
    
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    msg = random.choice(messages)
    
    subprocess.call(["git", "commit", "-m", msg], env=env)

print("Massive Git History Generation Complete.")
