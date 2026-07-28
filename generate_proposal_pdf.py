#!/usr/bin/env python3
"""Generate a print-ready PDF from a proposal HTML file in proposals/."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


HERE = Path(__file__).resolve().parent
PROPOSALS = HERE / "proposals"


def chrome_executable() -> str:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return str(path)

    for name in ("google-chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return found

    raise RuntimeError("No Chrome or Chromium executable found.")


def proposal_paths(slug: str) -> tuple[Path, Path]:
    html = PROPOSALS / f"{slug}.html"
    pdf = PROPOSALS / f"{slug}.pdf"
    if not html.exists():
        raise FileNotFoundError(f"Missing proposal HTML: {html}")
    return html, pdf


def render_pdf(html: Path, pdf: Path, *, base_url: str | None = None) -> None:
    url = base_url or html.as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chrome_executable(),
            headless=True,
            args=["--allow-file-access-from-files"],
        )
        page = browser.new_page(viewport={"width": 1100, "height": 1400})
        page.goto(url, wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf),
            format="Letter",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0.42in", "right": "0.42in", "bottom": "0.42in", "left": "0.42in"},
        )
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a proposal PDF from HTML.")
    parser.add_argument(
        "slug",
        nargs="?",
        default="rachel-horner-wedding-proposal",
        help="Proposal filename without extension (default: rachel-horner-wedding-proposal)",
    )
    parser.add_argument(
        "--url",
        help="Optional HTTP URL to render instead of the local file (e.g. GitHub Pages preview)",
    )
    args = parser.parse_args()

    html, pdf = proposal_paths(args.slug)
    render_pdf(html, pdf, base_url=args.url)
    print(f"SUCCESS: PDF written to {pdf}")
    print(f"Size: {pdf.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
