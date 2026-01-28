# Portfolio site — local dev & checks

This repository is a small static portfolio site (HTML, CSS and JS) served from the repository root.

Quick start

1. Local preview (no build):

```bash
# macOS / zsh
python3 -m http.server 8000
# then open http://localhost:8000
```

2. Add a portfolio item

- Add `projectN.html` at the repo root.
- Add the asset image to the `images/` directory and reference it with a relative path from `index.html`.
- Keep the same overlay markup (title, category and "Meer zien →") so styles and hover behavior stay consistent.

Repository checks (pre-commit)

This repo includes a simple pre-commit hook and validation scripts to help avoid broken image references and missing navigation IDs.

Files added:

- `scripts/check_images.py`: Scans HTML and CSS for src and url(...) references and verifies that referenced files exist.
- `scripts/check_site.py`: Ensures required IDs exist in `index.html` and runs the image checker.
- `.githooks/pre-commit`: A sample pre-commit hook that runs the checks.

Enable the hook locally (recommended):

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

Notes and gotchas

- Do not rename existing images unless you update all references in HTML and CSS. Many image filenames contain spaces and unusual extensions.
- The `site.webmanifest` file lives in the `images/` directory and is referenced from the HTML head — preserve that path.

Want automation on CI? I can add a GitHub Actions workflow that runs `python3 scripts/check_site.py` on PRs.
