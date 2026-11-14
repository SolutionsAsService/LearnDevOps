# DESIGN-LOG: LearnDevOps landing (Landing run, Autonomous, Lite)

## Traversal Plan
- Brief: a landing graphic and a rewritten root README for the five tracks (CI-CD, GitOps, IaC, Microservices, Monitoring).
- Mode: Autonomous (no client or audience constraint named). Run type: Landing. Bound: user asked for LITE, one move and one panel round.
- Palette source: the ANSI/xterm 16-colour terminal palette, the colour system of the shell and YAML these tracks live in. Hues assigned per track: CI-CD green, GitOps magenta, IaC cyan, Microservices blue, Monitoring yellow; red is reserved for the change path.
- Tools: rustdada check-floor (Mobile Floor); headless google-chrome for measurement; python for ΔE76 and WCAG contrast. No graph or workflow tooling used; anchor graph not rendered.
- Pages: single page, justified because the landing summarizes the five tracks and each track links to its own readme.

## Inventory (Landing step 1)
Five tracks, plus five Microservices examples (AuthService, DistributedSystems, E-Commerce, ProductCatalog, ServerlessApplications). The hero shows all five tracks; the Microservices node lists its five examples.

## Decision Record, M1: one path through five tracks (BREAK)
Depends on: none. Anchors: Landing form "one chart whose marks are the topics".
Intent: a red path joins five coloured nodes, one per track, with each track's facts under its node; the phone version runs the same path vertically.
Alternatives rejected: a card row (not a composed figure); a single-track chart (fails the summary rule).
Consequence: the path order (CI/CD, GitOps, IaC, Microservices, Monitoring) is a pedagogical reading, not a claim in the readmes; the README says so by listing the tracks without ordering claims.
Mode field: Reception dial used, plain labels with each track's own name beside its colour.

## Measurements (final state)
- Palette, dark: min pairwise ΔE76 52.7 (iac/micro); category hues 6.3 to 11.6:1 against the background; red signal 6.9:1.
- Palette, light: min pairwise ΔE76 40.7 (gitops/micro); category hues 5.8 to 7.4:1; red 6.1:1.
- Fills carry numerals in ink: dark ink on fills 7.0 to 11.6:1; light white on fills 6.3 to 7.9:1.
- Hero bottom edge at 1280 x 800: 626 px (above the fold). At 375 x 812: 798 px (above the fold, 14 px spare), figure right edge 344 px, document scroll width 360 px (no sideways scroll).
- Mobile Floor (`rustdada check-floor --web`): 12/12 hold at 360, 390 and 430 px. First run failed one row: the IaC nav link was 41 px wide; fixed with min-width 44 px.

## Panel
Not convened. The LITE pass asked for one panel round, but no independent seat agents were run in this session; the checks above are measurements, not panel verdicts. The Panel Report and Frontier are therefore not produced. Treat this run as incomplete under the stop test: S2 to S5 not met.

## Compliance Check (partial)
- [x] Tooling inventory done (none for graphs; rustdada check-floor used)
- [x] Mode stated; Run type stated (Landing)
- [ ] Panel seated and run
- [x] Palette derived from a named source, ΔE and contrast measured in light and dark
- [x] Landing leads with one graphic summarizing every topic; measured complete at 1280 x 800 and 375 x 812
- [x] One BREAK move taken
- [x] Decision Record written before the move (M1 above)
- [ ] Panel Report per round, WHOLE rounds, S1 to S5
- [x] Mobile Floor measured at the final state
- [ ] Anchor Ledger and live graph; double-loop paragraph; ledger import
- Shadw/Vercel config: root vercel.json and fluid.json added. The root index.html is the site itself, so the redirect file and a second vercel.json inside a subfolder were not added; .vercelignore not added.
- Open frontier (resume point): convene the Landing panel (Formalist, Evidence, Usability, Provocateur; dotted pair Krug and Debord) on the rendered page, then run S4 hero push.
