# The Machine Atlas

A growing, cross-linked library of business "machines." Each entry is one JSON file that studies how a business works (a **teardown**) or how you'd start one (a **buildout**). The dashboard (`index.html`) is just a render of these JSON records.

**The decks are exhaust. The Atlas is the asset. The fluency is the product.**

## Design: free writing, thin wiring (managed drift)

Entries are written freely — the model that writes them is not forced into a rigid template, because that freedom is what makes them good. The dashboard is a **tolerant reader**: it bends to each entry's shape instead of demanding one. It handles, for example:

- `identity` nested as an object **or** flat at the top level
- `recall.questions` **or** `recall.three_questions`
- `in_the_wild` as a string **or** a `{name, confidence}` object
- `engine.inputs` as an array **or** a string
- `unit` as a string **or** an object
- `economics_lens` present or absent; buildout-only sections appear only when present

The only things that stay stable (the "wiring") are the few fields that let entries find each other: an entry's `id`, its `mode`, and `chain.parent_id` / `chain.relation` / `chain.suggested_next`. Those let the dashboard trace chains and let the daily run know what's already covered.

## Layout

```
machine-atlas/
├── index.html            the dashboard (tolerant reader; works offline + on Pages)
├── .nojekyll             tells GitHub Pages to serve files as-is
├── build.py              regenerates data/manifest.json + re-inlines the offline fallback
└── data/
    ├── manifest.json     list of entry slugs the dashboard loads
    └── <slug>.json       one entry per file
```

## Current entries (6)

**Finance chain:** `banking` (teardown) -> `payment-networks` (symbiote); plus `banking-buildout`.
**AI-stack chain:** `nvidia` (root) -> `tsmc` (supplier).
**Convening:** `frontier-room` (buildout -- the Fort Lauderdale AI Builders' Club).

## Adding an entry

1. Drop `data/<slug>.json` into the folder (write it however reads best -- the dashboard will bend to it).
2. Run `python3 build.py` to update the manifest and the offline fallback.
3. Commit. The dashboard picks it up automatically.

## Publish (GitHub Pages)

Repo **Settings -> Pages -> Deploy from branch -> main / root**. Live at `https://<you>.github.io/machine-atlas/`. The `.nojekyll` file is what makes it serve the dashboard instead of rendering this README.
