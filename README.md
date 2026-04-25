# leetcode-solutions

Auto-synced LeetCode solutions with a Python test harness.

## Layout

```
solutions/
  conftest.py        # pytest harness, auto-discovers tests.json next to each solution.py
  helpers.py         # ListNode, TreeNode, type parsing, value comparison
  0001-two-sum/
    solution.py
    tests.json
    README.md
```

Each problem directory contains the submitted solution, the example test cases captured from LeetCode, and a generated README with the problem statement and your runtime/memory stats.

## Running the tests

This project uses [`uv`](https://docs.astral.sh/uv/) for environment management.

```bash
# Run every test
uv run pytest

# Run one problem
uv run pytest solutions/0001-two-sum/

# Run with verbose output
uv run pytest -v
```

CI runs the same on every pull request. PRs auto-merge once the test job passes.

## How solutions are added

A browser extension running on `leetcode.com` watches for accepted submissions, captures the code and metadata, and opens a pull request to this repo. CI runs the example test cases against the submitted code; if green, auto-merge lands the commit on `main`.
