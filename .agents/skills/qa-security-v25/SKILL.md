---
name: qa-security-v25
description: >-
  Vibe-coding QA·Security automation V3.0. Always-on TC design/update and dual verification
  for feature/bug/refactor/API/DB/UI/infra/deploy changes. Records under
  qa/results/{area}/{section}/{YYYY-MM-DD}/; uses test_map.json; pre-records FAIL/RISK.
  English paths; Korean report bodies. Do not claim automation without verified hooks/CI.
---

# QA·Security Automation V3.0 Skill

Policy: `qa-policy.md`, `AGENTS.md`. Runner: `scripts/qa/run.py`. One Agent + one Skill.

## Always

On every change: map impact → add/update atomic TCs in `qa/input/testcases.tsv` before run → execute tool A/B from `qa/config/test_map.json` → append results → pre-record FAIL/RISK before fixes → dual re-verify → full gate before PR/deploy.

## Layout

```
qa/master_test_sheet.xlsx
qa/input/testcases.tsv
qa/config/test_map.json
qa/history/execution_log.tsv
qa/results/{area}/{section}/{YYYY-MM-DD}/
  test_sheet.xlsx | pass.md | fail.md | risk.md | results.tsv
```

Areas: `01_unit_integration`, `02_web_api`, `03_security_quality`, `04_infra_deploy`.

## Commands

```sh
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --verify-automation
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --changed
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --tc TC-ID
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py
python3 scripts/qa/run.py --risks-only
```

AI only for new TC design, complex impact, unexplained FAIL/RISK. Never invent commands when `test_map.json` has them. Never PASS unrun paths. Never claim always-on automation if hooks/CI were not verified.
