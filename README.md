# crypto-skills

Chain-verifiable crypto research skills for AI agents. Each folder is a
self-contained skill: a `SKILL.md` with the method, plus runnable
stdlib-only scripts. No API keys, no pip installs — any agent with HTTP
and `python3` can run these.

## Skills

| Skill | What it does |
|---|---|
| [`pivx-governance-history`](./pivx-governance-history/) | Reconstruct PIVX governance: every passed/failed proposal, vote shares, and actual superblock payout receipts from the chain. |

## Data snapshots

Pre-generated outputs live in [`data/`](./data/) for quick reference:

- `pivx_proposals_2025-10_2026-10.json` — dated ledger of 92 PIVX
  proposals (Oct 2025 → Oct 2026): 76 passed, 16 failed, with amounts,
  yes/no votes, and forum URLs.

## Usage (any agent)

```bash
git clone https://github.com/CryptoSI-DAO/crypto-skills
cd crypto-skills/pivx-governance-history/scripts

# full proposal ledger (passed + failed, all history)
python3 pivx_gov_history.py proposals --out gov.json

# add forum thread dates for cycle bucketing
python3 pivx_gov_history.py date-threads --gov gov.json --out gov_dated.json --limit 100

# find treasury payout txs in a block range (superblock receipts)
python3 pivx_gov_history.py superblocks --from-height 5586700 --to-height 5586950

# group proposals into cycles
python3 pivx_gov_history.py cycles --gov gov_dated.json --superblocks sb.json
```

## Conventions

- One skill per folder, matching the Hermes skill name.
- Scripts: Python 3 stdlib only, no third-party deps.
- Data snapshots are dated in the filename and regenerable — treat the
  scripts as the source of truth, the JSON as convenience.

---
Maintained under the CryptoSI-DAO umbrella · Lisa Kim 🖤💛
