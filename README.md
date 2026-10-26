# Live 2 Help Recruitment website

Main site for live2helprecruitment.co.uk. The careers site, ATS and Talent Suite live in the separate `live2help` repo.

- `src/` holds the page content and build script (Python 3, no dependencies).
- `docs/` is the built site that GitHub Pages serves. Do not edit it by hand.

To change a page, edit the content in `src/pages.py` (main pages), `src/legal.py` (policies) or `src/redirects.py` (old addresses), then run:

    cd src && python3 build.py

and commit both `src/` and `docs/`.
