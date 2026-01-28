# Copilot / AI contributor instructions

Repository snapshot: small static portfolio site (HTML, CSS, JS) served from repository root.

Quick summary
- Single-page structure with named anchor ids: home, portfolio, about, contact.
- Per-project detail pages live at project1.html through project7.html in the project root.
- Images and other assets live in the images directory. Some filenames contain spaces and unusual extensions (for example: "Tshirt Mockup.png" and "Kroegentocht poster 17-10-2024.pdf"). Do not rename assets without updating references.
- No build system. The site is static HTML/CSS/JS and is typically deployed with GitHub Pages (a CNAME file exists).

What to edit and why
- index.html is the canonical content file. Keep the navbar anchor ids (home, portfolio, about, contact) intact — JS and CSS depend on them.
- script.js contains small DOM behaviors to preserve:
  - the footer year updater (element id: year)
  - the show-more button (element id: show-more-btn) which toggles visibility of the more-projects container (element id: more-projects)
  - visibility-on-scroll logic for elements with class portfolio-item
- style.css is the single source of styling. Visual tokens to respect: base background hex 0a0a0a and accent hex ff6b00; the Inter font is used. Prefer small responsive tweaks rather than large rewrites.

Concrete examples and patterns
- To add a portfolio item follow the article element with class portfolio-item inside the portfolio-grid. Steps:
  1) Add projectN.html at repo root.
  2) Add an image into images/ and reference it from index.html with a relative path.
  3) Use the same overlay structure (title, category, and the text "Meer zien →") so styles and hover behavior stay consistent.

Project gotchas to watch for
- Many image filenames contain spaces and at least one PDF is referenced as an image source; renaming files without updating references will break the site. Prefer kebab-case for new filenames (for example: kroegentocht-poster-2024.jpg).
- Older CSS rules used selectors named .grid and .card while the site markup uses portfolio-grid and portfolio-item. When refactoring, search for both patterns.
- The site.webmanifest file is located in images/ and referenced from the page head; preserve that path when updating the manifest.

Developer workflows
- Local preview: open index.html in a browser or run a tiny static server from the repo root:

```
python3 -m http.server 8000
```

- Deploy: push to GitHub and enable GitHub Pages from the repository root (default branch). If you change the domain, update the CNAME and DNS records.

Checks and testing
- No CI or automated tests are configured. Quick PR checks:
  - Validate HTML with an online validator or local tool.
  - Run Lighthouse for performance and accessibility.
  - Manually check: navigation anchors, the "Meer bekijken" show-more flow, and the footer year updater.

Small follow-ups I can add
- A small pre-commit script that validates HTML and checks that referenced image files exist.
- A short README with local preview and deploy steps.

If anything above is unclear or you want me to add the README or pre-commit checks, say which one and I will implement it.

