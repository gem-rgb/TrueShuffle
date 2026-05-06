#!/bin/bash
set -eo pipefail

cd /app

# 1. Reset to base commit
BASE_COMMIT=$(python3 -c "import json; print(json.load(open('my-task/tests/config.json'))['base_commit'])")
git reset --hard "$BASE_COMMIT"

# 2. Apply the test patch from config.json
python3 -c "
import json
cfg = json.load(open('my-task/tests/config.json'))
print(cfg.get('test_patch', ''))
" | git apply --allow-empty -

# 3. Run the test runner, capture output
mkdir -p /logs/verifier
bash my-task/tests/run_script.sh > /logs/runner_stdout.log 2> /logs/runner_stderr.log || true

# 4. Parse runner output into structured JSON
python3 my-task/tests/parser.py < /logs/runner_stdout.log > /logs/parser_output.json

# 5. Verify all fail_to_pass tests passed and all pass_to_pass tests passed
python3 -c "
import json, sys

parser_output = json.load(open('/logs/parser_output.json'))
config = json.load(open('my-task/tests/config.json'))

results = {r['name']: r['status'] for r in parser_output}

fail_to_pass = config.get('fail_to_pass', [])
pass_to_pass = config.get('pass_to_pass', [])

all_pass = True
for t in fail_to_pass + pass_to_pass:
    if results.get(t) != 'pass':
        print(f'FAIL: {t} -> {results.get(t, \"NOT FOUND\")}', file=sys.stderr)
        all_pass = False

with open('/logs/verifier/reward.txt', 'w') as f:
    f.write('1' if all_pass else '0')

print('1' if all_pass else '0')
"
