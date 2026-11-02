# QA·Security Automation Policy V3.0

Project operating policy informed by ISTQB CTFL, OWASP ASVS/WSTG, and tool docs. The four-area split and dual-tool rule are project policy, not external mandates.

## Apply

Always follow `AGENTS.md`. Never claim automation from documentation alone—verify local hooks and GitHub Actions.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r qa/requirements.txt -r ai/requirements-dev.txt -r data/requirements.txt
npm ci --prefix web-vite
# JDK 17, Node 22+, Docker, actionlint, jq as needed
git config --local core.hooksPath .githooks
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --verify-automation
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --changed   # related TCs
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py             # full gate
```

## Areas

| Folder | Tool A | Tool B |
|---|---|---|
| `01_unit_integration` | JUnit / pytest / Vitest | Testcontainers or API/DB blackbox |
| `02_web_api` | Playwright | Schemathesis / independent API check |
| `03_security_quality` | CodeQL | Semgrep |
| `04_infra_deploy` | Docker Compose readiness | `curl` smoke (+ k6 only in isolated env) |

Static SAST does not replace behavioral checks. If a required second path is unavailable, write `risk.md` + `qa/risks.json` and do not final-PASS that TC.

## Files

```
qa/
├── master_test_sheet.xlsx          # sole root Excel; latest aggregate
├── input/testcases.tsv             # TC definitions (AI adds; runner reads)
├── config/test_map.json            # TC → commands, path globs (no AI guessing)
├── history/execution_log.tsv       # append-only cross-date history
└── results/{area}/{section}/{YYYY-MM-DD}/
    ├── test_sheet.xlsx
    ├── pass.md
    ├── fail.md
    ├── risk.md
    └── results.tsv                 # append-only per RUN_ID
```

Korean prose in MD bodies; English paths/IDs/columns. Evidence logs under `qa/.runtime/` (gitignored). No secrets in logs.

## Status

`PASS|FAIL|BLOCKED|ERROR|NOT_RUN|SKIPPED`. RISK ledger is separate. Link `RUN_ID`, `TC_ID`, `FEATURE_ID`, times (KST), tools/commands/results, expected/actual, evidence paths, Git SHA, file/function/line (`UNKNOWN` if unknown), ISSUE/RISK IDs.

## Continuous QC

New feature → TCs in `testcases.tsv` before run → code+tests → dual execute → pre-record FAIL/RISK → fix → dual re-run → PR/deploy full gate. Required CI failure or open HIGH/CRITICAL blocks merge/deploy. Remote rulesets must be configured separately; do not claim server-side protection from repo files alone.

## References

- https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
- https://asvs.owasp.org/
- https://wstg.owasp.org/
- https://docs.pytest.org/en/stable/how-to/parametrize.html
- https://playwright.dev/docs/test-assertions
- https://docs.docker.com/compose/how-tos/startup-order/
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://grafana.com/docs/k6/latest/using-k6/thresholds/
