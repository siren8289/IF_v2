# qa (V3.0)

Always-on QA·Security automation artifacts.

```
qa/
├── master_test_sheet.xlsx
├── input/testcases.tsv
├── config/test_map.json
├── history/execution_log.tsv
└── results/{area}/{section}/{YYYY-MM-DD}/
    test_sheet.xlsx | pass.md | fail.md | risk.md | results.tsv
```

## Run

```sh
git config --local core.hooksPath .githooks
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --verify-automation
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --changed
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py
```

Policy: `qa-policy.md`, `AGENTS.md`. English paths; Korean report bodies.
