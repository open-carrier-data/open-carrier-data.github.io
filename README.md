# Open Carrier Data website

This repository holds the one-page documentation site at
https://open-carrier-data.github.io/. It is the plain-language front door for
the public database at https://github.com/open-carrier-data/open-carrier-data.
Carrier data does not live here, and phones never load this site at runtime.

## What each file does

| File | Purpose |
| --- | --- |
| `index.html` | The whole page. One `h1`, sections from hero to contribute. |
| `styles.css` | Layout and colors. System fonts, light and dark by `prefers-color-scheme`. |
| `app.js` | Copy buttons only. The page works with JavaScript off. |
| `assets/` | Icon, favicon, and social preview images. |
| `.nojekyll` | Tells GitHub Pages to publish the files as they are. |
| `.github/workflows/pages.yml` | Deploys the repository root to GitHub Pages. |

## How the page deploys

A push to `main` runs `.github/workflows/pages.yml`, which uploads the
repository root as the Pages artifact and deploys it. No build step exists.

## Preview locally

To serve the page on port 8000, run this from the repository root.

```bash
python3 -m http.server
```

Then open http://localhost:8000/ in a browser.

## Where the facts come from

Counts, file names, commands, and source terms on the page come from the public
database repository at the commit named in the "Status" section. Re-check them
against its `README.md`, `SOURCES.md`, `generated/devices/index.json`, and
`generated/evidence-index.json` before you change a number here.
Website code and text are Apache-2.0. See `LICENSE`.
