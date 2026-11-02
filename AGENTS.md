# Always-on QA·Security Rules V3.0

Apply to every feature add/change, maintenance, bugfix, refactor, and API/DB/UI/infra/deploy change. Users must not need to request QA each time.

Do not report “automation complete” from policy text alone. Local hooks/change watch and GitHub Actions must be connected and verified.

## Areas and dual verification

| Area | Tool A | Tool B | Focus |
|---|---|---|---|
| `01_unit_integration` | JUnit / pytest / Vitest (stack-appropriate) | Testcontainers or independent API/DB blackbox | Function results, branches, real service·DB |
| `02_web_api` | Playwright | Schemathesis (OpenAPI) or independent API CLI | UI flows, HTTP status/body/errors/auth |
| `03_security_quality` | CodeQL | Semgrep | Vuln patterns, secrets, auth gaps, SAST |
| `04_infra_deploy` | Docker Compose config/health | `curl` smoke (k6 only in isolated env) | Container readiness, real request success |

- Do not force unfit tools (e.g. Testcontainers on pure unit logic).
- Running the same command twice is not dual verification.
- If only one required path is possible, record reason + alternate plan in `risk.md` and do not treat as final PASS.
- CodeQL/Semgrep do not replace behavioral UI/API/deploy checks.

## Atomic TC decomposition

Map `requirement → feature → UI/API → service/function → DB/external → exception/state`. Prefer changed files first; do not reload the whole project into AI context every time.

Decompose into distinct atomic TCs for applicable: input, boundary, branch, output, state/data, authz, external failure, security/ops, regression. Each TC needs a clear expected result (never only “works normally”).

Required fields: `TC_ID`, `FEATURE_ID`, `REQUIREMENT_ID`, `AREA`, `SECTION`, `SCENARIO`, `PRECONDITION`, `INPUT`, `STEPS`, `EXPECTED_RESULT`, `TOOL_A`, `COMMAND_A`, `TOOL_B`, `COMMAND_B`, `CODE_FILE`, `FUNCTION`, `RISK_LEVEL` (as needed). TC IDs are stable across reruns.

## Completion workflow

1. Before change: map requirements and existing TCs.
2. New feature: add TCs to `qa/input/testcases.tsv` **before** execution. Preserve existing TCs on edits; add/update only what is needed.
3. Ship feature with test code/fixtures/independent commands.
4. Run tool A and B for the change scope; collect status, logs, evidence paths.
5. On FAIL/RISK: record reports **before** further code fixes; notify the user; fix only in approved scope.
6. Re-run fixed and related regression TCs on both paths.
7. Do not report complete without required TCs and dual evidence.
8. Before PR/deploy: full regression/security/deploy checks. CI must block on required failures and open HIGH/CRITICAL risks.

## Layout (English names only)

```
qa/
├── master_test_sheet.xlsx
├── input/testcases.tsv
├── config/test_map.json
├── history/execution_log.tsv
└── results/{area}/{section}/{YYYY-MM-DD}/
    test_sheet.xlsx | pass.md | fail.md | risk.md | results.tsv
```

Paths/IDs/sheet tabs: English. Report bodies: Korean. Dates: Asia/Seoul `YYYY-MM-DD`. Create date folders only for executed area/section. History TSV is append-only; master Excel may refresh to latest.

## Status and gate

Statuses: `PASS / FAIL / BLOCKED / ERROR / NOT_RUN / SKIPPED`. RISK is a separate ledger (`qa/risks.json`), not a status substitute.

PASS requires both required paths executed, all required assertions passed, and evidence present. Unrun work is never PASS. Open HIGH/CRITICAL blocks complete/merge/deploy.

## Automation and AI

- One QA Agent, one QA Skill.
- Execution/judgment/reports/Excel via deterministic scripts (`scripts/qa/run.py`).
- Commands live in `qa/config/test_map.json`—AI must not invent commands every run.
- Local: hook/watch runs **related** TCs after work (debounced). CI: push/PR required checks. Branch protection/rulesets are separate remote settings.
- AI only for new TC design, complex impact analysis, unexplained FAIL/RISK. Do not feed whole repo/TSV every time.

Official runner: `PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py`. Details: `qa-policy.md`.
