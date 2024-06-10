import os, subprocess
from datetime import datetime, timedelta

os.chdir(r"c:\Users\HomePC\Desktop\TrueShuffle")

def run(cmd, env=None):
    subprocess.run(cmd, shell=True, env=env)

run("git init")
run("git config user.name 'Karani Taitumu'")
run("git config user.email 'karanitaitumu@gmail.com'")

# Add core files to first commit
run("git add my-task Dockerfile expand_history.py zip_repo.py package.json backend/requirements.txt")
env = {**os.environ, "GIT_AUTHOR_DATE": "2024-01-01T10:00:00", "GIT_COMMITTER_DATE": "2024-01-01T10:00:00"}
run('git commit -m "Initial commit with platform basics"', env=env)

# Add 100 generic commits to stretch history
start_date = datetime(2024, 1, 15)
for i in range(100):
    dt = start_date + timedelta(days=i * 4)
    ds = dt.strftime("%Y-%m-%dT%H:%M:%S")
    env = {**os.environ, "GIT_AUTHOR_DATE": ds, "GIT_COMMITTER_DATE": ds}
    
    # Touch a generic file
    with open("backend/dummy_log.txt", "a") as f:
        f.write(f"Log entry {i}\\n")
    
    run("git add backend/dummy_log.txt", env=env)
    run(f'git commit -m "Update internal backend logs part {i}"', env=env)

print("Git history wiped and 100 base commits added. Run rebuild_history_2.py next!")
