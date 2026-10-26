#!/usr/bin/env python3
"""Builds the Live 2 Help main website into ../site.
Every internal link uses a relative prefix ({R}) so the site works on the
custom domain, on a GitHub Pages project URL and in a preview."""
import os, html, datetime, json
from pages import PAGES
from legal import LEGAL
from redirects import REDIRECTS

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs')
DOMAIN = 'https://live2helprecruitment.co.uk'

NAV = [
    ('employers/', 'Employers'),
    ('candidates/', 'Candidates'),
    ('sectors/', 'Sectors'),
    ('TS', 'Talent Suite'),
    ('ROLES', 'Live Roles'),
    ('about/', 'About'),
    ('contact/', 'Contact'),
]

def careers(path, medium, content):
    return ('https://careers.live2helprecruitment.co.uk/' + path +
            '?utm_source=website&utm_medium=' + medium + '&utm_content=' + content)

def head(title, desc, R, canonical, noindex=False):
    t = html.escape(title)
    d = html.escape(desc)
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{DOMAIN}/{canonical}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="theme-color" content="#0B0B18">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Live 2 Help Recruitment">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{DOMAIN}/{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{R}assets/favicon.png">
<link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(R, active):
    links = []
    for href, label in NAV:
        if href == 'TS':
            url = careers('talent-suite/', 'nav', 'talent_suite')
        elif href == 'ROLES':
            url = careers('', 'nav', 'live_roles')
        else:
            url = R + href
        cur = ' aria-current="page"' if href == active else ''
        links.append(f'<a href="{url}"{cur}>{label}</a>')
    links.append(f'<a class="btn btn-gold" href="{careers("hire/", "nav", "hiring_toolkit")}">Free Hiring Toolkit</a>')
    return f'''<header class="hdr">
<div class="wrap">
<a class="brand" href="{R or './'}" aria-label="Live 2 Help Recruitment home"><img src="{R}assets/logo-wide.png" alt="Live 2 Help Recruitment" width="164" height="46"></a>
<button class="burger" type="button" aria-controls="nav" aria-expanded="false" aria-label="Menu"><span></span></button>
<nav class="nav" id="nav" aria-label="Main">{''.join(links)}</nav>
</div>
</header>
<main id="main">
'''

def footer(R):
    year = datetime.date.today().year
    return f'''</main>
<footer class="ftr">
<div class="wrap">
<div class="fcols">
<div>
<img class="logo" src="{R}assets/logo-wide.png" alt="Live 2 Help Recruitment" width="185" height="52">
<p class="tl">Anyone · Anywhere · Anytime</p>
<p>Specialist recruitment across the UK, with free tools that help employers hire smarter and candidates get seen.</p>
</div>
<div>
<h4>Employers</h4>
<ul>
<li><a href="{R}employers/">How we work</a></li>
<li><a href="{careers('hire/', 'footer', 'hiring_toolkit')}">Free Hiring Toolkit</a></li>
<li><a href="{R}sectors/">Sectors we cover</a></li>
<li><a href="{R}contact/?type=employer">Send us a vacancy</a></li>
</ul>
</div>
<div>
<h4>Candidates</h4>
<ul>
<li><a href="{careers('', 'footer', 'live_roles')}">Live Roles</a></li>
<li><a href="{careers('talent-suite/', 'footer', 'talent_suite')}">Talent Suite</a></li>
<li><a href="{careers('talent-suite/career/', 'footer', 'career_toolkit')}">Free Career Toolkit</a></li>
<li><a href="{careers('talent-pool/', 'footer', 'talent_pool')}">Join the talent pool</a></li>
</ul>
</div>
<div>
<h4>Contact</h4>
<ul>
<li><a href="mailto:office@live2helprecruitment.co.uk">office@live2helprecruitment.co.uk</a></li>
<li><a href="tel:+441902945444">01902 945444</a></li>
<li><a href="https://www.linkedin.com/company/live-2-help-recruitment" rel="noopener">LinkedIn</a></li>
<li><a href="https://g.page/r/CU5L4ObMovbGEBM/review" rel="noopener">Google reviews</a></li>
</ul>
</div>
</div>
<div class="fbase">
<span>© {year} Live 2 Help Recruitment Ltd. Registered in England and Wales, company no. 11731080.</span>
<nav aria-label="Policies">
<a href="{R}legal/website-terms/">Website terms</a>
<a href="{R}legal/privacy-policy/">Privacy</a>
<a href="{R}legal/ethical-behaviour-policy/">Ethical behaviour</a>
<a href="{R}legal/child-labour-policy/">Child labour</a>
<a href="{R}legal/whistleblowing-policy/">Whistleblowing</a>
</nav>
</div>
</div>
</footer>
<script src="{R}assets/site.js" defer></script>
</body>
</html>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)

def prefix(path):
    depth = path.count('/') if path.endswith('/') else path.count('/')
    return '../' * depth

def expand(body, medium):
    # {CAREERS:path|slot} tokens become tracked careers links
    import re
    def rep(m):
        path, slot = m.group(1), m.group(2)
        return careers(path, medium, slot)
    return re.sub(r'\{CAREERS:([^|}]*)\|([^}]+)\}', rep, body)

def render_page(p):
    path = p['path']
    R = p.get('root', prefix(path))
    body = expand(p['body'], p.get('medium', path.strip('/') or 'home')).replace('{R}', R)
    out = head(p['title'], p['desc'], R, path, p.get('noindex', False)) + header(R, p.get('active', '')) + body + footer(R)
    assert '—' not in out, 'em dash found in ' + path
    write(p.get('file', path + 'index.html'), out)

def render_redirect(old, new):
    R = prefix(old)
    target = new if new.startswith('http') else R + new
    canon = new if new.startswith('http') else DOMAIN + '/' + new
    out = f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Moved - Live 2 Help Recruitment</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{canon}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace({json.dumps(target)} + location.hash);</script>
</head><body><p>This page has moved. <a href="{target}">Continue to the new page</a>.</p></body></html>
'''
    write(old + 'index.html', out)

def main():
    for p in PAGES:
        render_page(p)
    for p in LEGAL:
        render_page(p)
    for old, new in REDIRECTS.items():
        render_redirect(old, new)
    # sitemap
    today = datetime.date.today().isoformat()
    urls = [p['path'] for p in PAGES + LEGAL if not p.get('noindex')]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f'  <url><loc>{DOMAIN}/{u}</loc><lastmod>{today}</lastmod></url>')
    sm.append('</urlset>')
    write('sitemap.xml', '\n'.join(sm) + '\n')
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    print('built', len(PAGES) + len(LEGAL), 'pages and', len(REDIRECTS), 'redirects')

if __name__ == '__main__':
    main()
