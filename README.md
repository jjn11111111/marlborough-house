# The Marlborough House Wedding Packages & Catering Menu 2026

Client-facing HTML and PDF version of The Marlborough House wedding packages and catering menu.

## Permanent Access (GitHub Pages)

These URLs stay live as long as this repo is published. No local server or port forwarding required.

| Resource | URL |
| --- | --- |
| **Packages & menu** | https://jjn11111111.github.io/marlborough-house/ |
| **Client proposals hub** | https://jjn11111111.github.io/marlborough-house/proposals/ |
| **The Gay Couple — HTML** | https://jjn11111111.github.io/marlborough-house/proposals/the-gay-couple-wedding-proposal.html |
| **The Gay Couple — PDF** | https://jjn11111111.github.io/marlborough-house/proposals/the-gay-couple-wedding-proposal.pdf |
| **Amanda Bolduc — HTML** | https://jjn11111111.github.io/marlborough-house/proposals/amanda-bolduc-wedding-proposal.html |
| **Amanda Bolduc — PDF** | https://jjn11111111.github.io/marlborough-house/proposals/amanda-bolduc-wedding-proposal.pdf |
| **Rachel Horner — HTML** | https://jjn11111111.github.io/marlborough-house/proposals/rachel-horner-wedding-proposal.html |
| **Rachel Horner — PDF** | https://jjn11111111.github.io/marlborough-house/proposals/rachel-horner-wedding-proposal.pdf |

Share the **proposals hub** link with your team; share individual HTML or PDF links with clients.

## Files

- `index.html` - browser-viewable source document
- `Marlborough-House-Wedding-Packages-and-Menu-2026.pdf` - print/share PDF
- `proposals/` - client-specific wedding proposal decks (HTML + PDF, print-ready)
- `proposals/index.html` - proposals hub with links to all client decks
- `assets/` - logo and menu imagery used by the HTML document
- `generate_pdf.py` - regenerates the menu PDF from `index.html`
- `generate_proposal_pdf.py` - regenerates a proposal PDF from `proposals/<slug>.html`

## Regenerating a Proposal PDF

```bash
# From repo root, with a local server serving the repo (for correct asset paths):
python3 -m http.server 8080
python3 generate_proposal_pdf.py --url http://127.0.0.1:8080/proposals/rachel-horner-wedding-proposal.html
git add proposals/rachel-horner-wedding-proposal.pdf && git commit -m "Update Rachel Horner proposal PDF" && git push
```

## Client Proposals

| Client | HTML | PDF |
| --- | --- | --- |
| The Gay Couple — Package 3, 85 guests, midnight blue & gold | [View](https://jjn11111111.github.io/marlborough-house/proposals/the-gay-couple-wedding-proposal.html) | [Download](https://jjn11111111.github.io/marlborough-house/proposals/the-gay-couple-wedding-proposal.pdf) |
| Amanda Bolduc — Package 3, 100 guests | [View](https://jjn11111111.github.io/marlborough-house/proposals/amanda-bolduc-wedding-proposal.html) | [Download](https://jjn11111111.github.io/marlborough-house/proposals/amanda-bolduc-wedding-proposal.pdf) |
| Rachel Horner — July 2027, Package 3, 110 guests | [View](https://jjn11111111.github.io/marlborough-house/proposals/rachel-horner-wedding-proposal.html) | [Download](https://jjn11111111.github.io/marlborough-house/proposals/rachel-horner-wedding-proposal.pdf) |

Source files: `proposals/the-gay-couple-wedding-proposal.html`, `proposals/amanda-bolduc-wedding-proposal.html`, `proposals/rachel-horner-wedding-proposal.html`
