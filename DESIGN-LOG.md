# DESIGN-LOG: LearnDevOps front page (Landing, Autonomous, Lite)

## Traversal Plan
- Brief: a bold landing graphic (index.html) and a rewritten root README.md for LearnDevOps.
- Mode: Autonomous (no client or audience constraint named). Run type: Landing. Bound: person asked for Lite (one move, one panel round).
- Tooling: `scripts/check_floor.py` (Mobile Floor). No graph tooling used.
- Seed: Stance "landing summarizes the whole site"; Rule "first screen complete"; Breaker "one composed ring figure, one node per track"; counterpoint: legibility probe (dotted).
- Frontier (Lite, not traversed): OPEN: browser-measured first-screen bounding box; DEFERRED: a Playwright render (not run in Lite).

## Inventory (landing summary rule)
Five topics: CI-CD, GitOps, IaC, Microservices, Monitoring. The ring shows all five with one line each.

## Decision Record M1: ring figure (BREAK)
Depends on: none. Intent: one composed figure, five nodes on a ring around a count of "5", so the first screen says what the site holds.
Alternatives rejected: a single chart of one track (fails the summary rule); a card grid as hero (not a figure).
Consequence: the figure is an illustration, not data; it states no numbers beyond the track count.
Fence: none broken.

## Panel Report: WHOLE round R1 (Lite, single round)
Artifact: /home/user/bench/python-dada/index.html (rendered mentally; not screenshot).
| Critic | Anchor | Observed | Verdict | Requested change |
|---|---|---|---|---|
| Formalist | ring, one figure | five nodes balanced on a circle | PASS | none |
| Evidence | First screen | SVG 560 px max; est. bottom ~700 px at 1280x800, ~560 px at 375x812 | PASS (estimated) | browser measurement deferred |
| Usability | five-second test | title names the five tracks; each node names its track | PASS | none |
| Provocateur | hero as claim | "Five DevOps tracks" stated in h1 | PASS | none |
Andon pulled: no. Dotted pair Krug / Debord noted.

Resolutions: check_floor first run failed 2 rows (touch targets under 44/24 px on nav, footer and track links). ADAPT: links made inline-flex with min-height 44 px. Re-run: 12/12 at 360, 390, 430 px.

## Anchor Ledger
| Anchor | Role | Status | Evidence | Note |
|---|---|---|---|---|
| landing summarizes whole site | Stance | KEEP | ring shows all five | |
| first screen complete | Rule | KEEP | estimated bounds | browser measure deferred |
| one composed ring figure | Breaker | KEEP | M1 | |
| legibility probe | Counterpoint | DEFERRED | not run in Lite | |

## Stop test
S1: Frontier OPEN items remain (browser measurement, legibility probe): NOT MET. S2: one round only (Lite bound). S3/S4: not met (no saturation, no push). Run is incomplete under the Lite bound.

## Compliance Check
- [x] Tooling inventory: check_floor used; no graph tooling
- [x] Mode stated (Autonomous, reason: no constraint named)
- [ ] Panel from pick_panel.py: not run (Lite, single round)
- [x] Run type stated (Landing)
- [x] Landing graphic summarizes all topics
- [ ] First screen measured in a browser: estimated only
- [x] Decision Record before the move
- [ ] S1 to S4 met: not met under Lite bound
- [ ] Ledger import: not run

## Notes
- Source gap: `Microservices/` has no top-level readme.md; the README and index link to the folder and describe its five subservices from their own readmes.
