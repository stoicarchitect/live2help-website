# Old GoDaddy page addresses -> new pages, so old links and Google results keep working.
# Slugs confirmed from the live GoDaddy site (Oct 2026). GoDaddy used "%26" for "&",
# so each of those gets a folder with a literal "&" and one with "%26", covering
# however the host decodes the request.
CAREERS = 'https://careers.live2helprecruitment.co.uk/'

_AMP = {
    'accountancy-&-finance/': 'sectors/#finance',
    'catering-&-hospitality/': 'sectors/',
    'engineering-&-technical/': 'sectors/#engineering',
    'it-&-it-sales/': 'sectors/#it',
}

REDIRECTS = {
    'about-us/': 'about/',
    'contact-us/': 'contact/',
    'permanent-recruitment/': 'employers/',
    'resources/': CAREERS + 'hire/?utm_source=website&utm_medium=redirect&utm_content=old_resources',
    'commercial/': 'sectors/#commercial',
    'construction/': 'sectors/#construction',
    'corporate/': 'sectors/#executive',
    'driving/': 'sectors/#logistics',
    'health-and-social-care/': 'sectors/#health',
    'industrial/': 'sectors/#manufacturing',
    # Policy pages: likely GoDaddy slugs, harmless if unused
    'legal/': 'legal/website-terms/',
    'privacy-policy/': 'legal/privacy-policy/',
    'child-labour-policy/': 'legal/child-labour-policy/',
    'ethical-behaviour-policy/': 'legal/ethical-behaviour-policy/',
    'whistleblowing-policy/': 'legal/whistleblowing-policy/',
}
for k, v in _AMP.items():
    REDIRECTS[k] = v
    REDIRECTS[k.replace('&', '%26')] = v
