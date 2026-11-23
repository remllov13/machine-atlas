# The Machine Atlas

A growing, cross-linked library of business "machines." Each entry is one JSON file that studies how a business works (a **teardown**) or how you'd start one (a **buildout**). The map (`index.html`) is a render of these JSON records.

**The decks are exhaust. The Atlas is the asset. The fluency is the product.**

## v3: an industry city with company districts

**Top map (index.html):** each building is an industry, sized by the industry's revenue (every 10x in revenue roughly doubles the height). Rows are supply chains (AI stack, Money, Media, Community); within a row, suppliers sit left and customers right, and roads run supplier → customer. Dashed plots are locked industries that a daily run has not mapped yet.

**Click an industry:** its district opens. Each company is a building; height compares share of that market against a fixed 100% reference, so a near-monopoly looks like one tower among huts and an oligopoly looks like a skyline. Lit windows = a teardown exists. Plain = known, not studied. A crane = a teardown ordered. The staked lot adds a company that isn't listed.

**Queue box:** Industry mode maps a new industry; Company mode orders a teardown or buildout. Each opens a prefilled GitHub issue (`queue: industry: X` or `queue: company: X | industry: id | mode: teardown`).

**Daily run:** one industry per day (must map to a 2022 NAICS code; trends go to `data/macro/queue.json`, not the map), plus one queued company teardown. Companies stay plain until ordered.

`classic.html` is the v2 company map, kept for reference.

## Layout

```
machine-atlas/
├── index.html                 v3 city map (loads data over HTTP; no inlined data)
├── classic.html               v2 company map
├── build.py                   regenerates data/manifest.json (teardowns) + classic fallback
└── data/
    ├── industries/city.json   chains, roads, locked plots
    ├── industries/<id>.json   one industry: revenue, structure, companies with sourced shares
    ├── <slug>.json            company or industry teardowns (free writing, thin wiring)
    ├── manifest.json          list of teardown slugs
    └── macro/                 macro forces (future weather layer)
```

## Industry file (industry/v1, fixed shape)

`id, name, chain, stage, naics{code,title}, one_line, sells, customers, suppliers, revenue{value_usd, display, metric, period, basis, confidence, source_url, note}, structure{type, why, hhi, hhi_note}, econ, companies[{name, share_pct, share_basis, revenue_usd, revenue_display, rank, source_url, as_of_date, teardown, note}]`, optional `industry_teardown` / `industry_buildout`.

Teardowns keep the loose v2 shape ("free writing, thin wiring"); a standard teardown protocol is a later phase.

## Publish (GitHub Pages)

Repo Settings → Pages → Deploy from branch → main / root. The `.nojekyll` file makes Pages serve the map instead of rendering this README.
