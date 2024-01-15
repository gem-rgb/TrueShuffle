"""Parse pytest verbose output into a list of {name, status} records."""
import json
import sys
import re


def parse_pytest_output(text: str):
    results = []
    # pytest -v outputs lines like:
    #   backend/tests/test_popularity_unification.py::test_foo PASSED
    #   backend/tests/test_popularity_unification.py::test_bar FAILED
    pattern = re.compile(
        r"backend/tests/test_popularity_unification\.py::(\w+)\s+(PASSED|FAILED)"
    )
    for line in text.splitlines():
        m = pattern.search(line)
        if m:
            name = m.group(1)
            status = "pass" if m.group(2) == "PASSED" else "fail"
            results.append({
                "name": f"test_popularity_unification.{name}",
                "status": status,
            })
    return results


if __name__ == "__main__":
    stdout = sys.stdin.read()
    results = parse_pytest_output(stdout)
    json.dump(results, sys.stdout, indent=2)
    print()  # trailing newline
