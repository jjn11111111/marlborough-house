#!/usr/bin/env python3
"""Generate the Marlborough House consolidated wedding PDF from index.html."""

from pathlib import Path
import shutil
import sys

from playwright.sync_api import sync_playwright


HERE = Path(__file__).resolve().parent
HTML = HERE / "index.html"
OUT = HERE / "Marlborough-House-Wedding-Packages-and-Menu-2026.pdf"


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


def main() -> int:
    if not HTML.exists():
        raise FileNotFoundError(f"Missing source HTML: {HTML}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chrome_executable(),
            headless=True,
            args=["--allow-file-access-from-files"],
        )
        page = browser.new_page(viewport={"width": 1100, "height": 1400})
        page.goto(HTML.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUT),
            format="Letter",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0.42in", "right": "0.42in", "bottom": "0.42in", "left": "0.42in"},
        )
        browser.close()

    print(f"SUCCESS: PDF written to {OUT}")
    print(f"Size: {OUT.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
