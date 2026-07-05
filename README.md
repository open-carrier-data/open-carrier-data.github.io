# Open Carrier Data Website

This repository publishes the static documentation website for Open Carrier
Data:

```text
https://open-carrier-data.github.io/
```

The carrier database itself lives in:

```text
https://github.com/open-carrier-data/open-carrier-data
```

## Purpose

The website is the plain-language front door for the project.

It should help a new reader quickly understand:

- what Open Carrier Data is;
- why carrier settings need a shared database;
- how stable data, community claims, and candidate claims differ;
- how ROMs, apps, and build tools should consume the data;
- how to report missing or wrong carrier data;
- what private data must never be submitted.
- why stale private vendor/OEM snapshots should not be published as stable
  data.

The website is documentation only. Phones should not depend on it at runtime.

## Files

```text
index.html          main page content
styles.css          layout and visual styling
app.js              small navigation behavior
assets/             icon, favicon, and social preview images
.github/workflows/  GitHub Pages deployment
```

Carrier profiles, schemas, validators, generated data, and community claims
belong in the public database repo, not in this website repo.

## Local Preview

Open `index.html` in a browser, or serve this folder with any static file
server.

Before publishing, check:

- the first screen says what the project is without needing background
  knowledge;
- the main buttons point to the public repo, the docs sections, and the issue
  flow;
- contribution text makes clear that users do not need repo write access;
- long code blocks fit on mobile screens;
- links to the public repo, snapshot, schema, and issue forms still work.

## Deployment

Changes pushed to `main` are deployed by GitHub Pages through:

```text
.github/workflows/pages.yml
```

## Rules

- Keep the site simple and readable.
- Prefer examples over abstract wording.
- Do not hide important limits.
- Do not store carrier data here.
- Do not make phone runtime behavior depend on this site.
- Keep private source automation in the private repo.

## License Status

No final license file has been added yet. Until a clear license is added, treat
the website assets and code as project material and do not assume they can be
reused outside this repository.
