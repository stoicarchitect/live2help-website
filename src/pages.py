# Page content for the Live 2 Help main website.
# {R} = relative path to site root. {CAREERS:path|slot} = tracked link to the careers subdomain.

REVIEWS = [
    ("My experience with Live 2 Help Recruitment could not have been any better. Dan was extremely helpful and went above and beyond for me. He found a job suited to my skill set and extremely local to me. Where Dan really shined is that he made what could have been a stressful experience anything but that. I had multiple check-ins up until the interview and even after. A super easy recommendation to anyone.", True),
    ("I had a great experience throughout the entire recruitment process. Daniel was exceptional from start to finish, always available to help, guide, motivate and support. His professionalism and dedication made a real difference.", False),
    ("Trustworthy, honest and caring. Daniel has been pivotal in preparation and has gone the extra step to help. The platform and resources we are given which are bespoke to L2H are second to none.", False),
    ("Wow, a fabulous support and guidance service from start to finish. Very unusual these days to have such detailed guidance on correct preparation. Dan is an expert in his field.", False),
]

def reviews_block(heading='Trusted by employers and candidates', medium_note=True):
    cards = []
    for text, hero in REVIEWS:
        cls = 'rv hero-rv' if hero else 'rv'
        cards.append(f'<figure class="{cls} rv-in"><div class="stars" aria-label="5 stars">★★★★★</div><blockquote>"{text}"</blockquote><cite>Verified Google review</cite></figure>')
    return f'''<section class="sec line-top center" id="reviews">
<div class="wrap">
<span class="kick">Reviews</span>
<h2 class="h2">{heading}</h2>
<div class="score"><b>5.0</b><div><div class="stars">★★★★★</div><div>Rated on Google</div></div></div>
<div class="g3">{''.join(cards)}</div>
<div class="btns mt"><a class="btn btn-ink arrow" href="https://g.page/r/CU5L4ObMovbGEBM/review" rel="noopener">Read all Google reviews</a></div>
</div>
</section>
'''

SECTORS = [
    ('engineering', 'Engineering and Technical', 'Mechanical, electrical, design and maintenance engineers who can work from a drawing, solve a fault and keep a site running.', 'Design Engineer · Maintenance Engineer · NPD Technician · Electrical Engineer'),
    ('manufacturing', 'Manufacturing and Industrial', 'Production leaders, technicians and operatives for busy sites, screened for reliability and ready to start quickly.', 'Production Manager · Shift Leader · CNC Setter · Production Operative'),
    ('procurement', 'Procurement and Supply Chain', 'Buyers and planners who protect margin and keep materials moving, from project buying to category management.', 'Category Manager · Group Buyer · Materials Planner · Supply Chain Manager'),
    ('commercial', 'Commercial and Sales', 'Sales and business development people with a real pipeline and the credibility to sell into your market.', 'Sales Manager · Technical Sales · Account Manager · Business Development'),
    ('finance', 'Accountancy and Finance', 'From transactional finance to qualified accountants who run month end, budgets and management reporting.', 'Finance Manager · Management Accountant · Credit Controller · Purchase Ledger'),
    ('it', 'IT and Technology', 'Technical talent for internal IT teams and tech businesses, assessed on what they can actually do.', 'Software Developer · IT Support · Infrastructure Engineer · Data Analyst'),
    ('construction', 'Construction and Infrastructure', 'Site and office roles across construction and infrastructure projects, matched to your programme.', 'Site Manager · Quantity Surveyor · Estimator · Project Coordinator'),
    ('health', 'Health and Social Care', 'Compassionate, compliant people for regulated care environments, with checks completed before they start.', 'Care Home Manager · Deputy Manager · Senior Carer · Support Worker'),
    ('ai', 'AI and Emerging Technologies', 'People who can turn AI and automation into results inside a real business, not just a pilot.', 'AI Engineer · Automation Specialist · Data Scientist · AI Apprentice'),
    ('hr', 'HR and People Management', 'HR professionals who balance compliance with culture and can support a business as it grows.', 'HR Manager · HR Business Partner · HR Advisor · Recruitment Coordinator'),
    ('executive', 'Corporate and Executive', 'Confidential retained search for senior and leadership hires, where the wrong appointment is expensive.', 'Operations Director · Head of Department · General Manager · Senior Leadership'),
    ('logistics', 'Driving and Logistics', 'Drivers, warehouse teams and logistics leaders who keep goods moving safely and on time.', 'Transport Manager · Warehouse Manager · HGV Driver · Logistics Coordinator'),
]

def sector_tiles(link=True):
    out = []
    for slug, name, _, _ in SECTORS:
        if link:
            out.append(f'<a class="tile" href="{{R}}sectors/#{slug}"><i class="dot"></i>{name}</a>')
        else:
            out.append(f'<div class="tile"><i class="dot"></i>{name}</div>')
    return ''.join(out)

TOOLKIT_PANEL = '''<div class="panel" aria-hidden="true">
<div class="row"><span class="lbl">Vacancy cost calculator</span><span class="lbl">Example</span></div>
<div class="big">£4,280</div>
<div>What an empty seat has cost so far</div>
<div class="row" style="margin-top:14px"><span>Hiring health score</span><span style="color:#fff">62 / 100</span></div>
<div class="bar"><i style="width:62%"></i></div>
<div class="steps3"><span><b>STEP 1</b>Vacancy cost</span><span><b>STEP 2</b>Hiring health</span><span><b>STEP 3</b>Offer strength</span></div>
</div>'''

FINAL_CTA = '''<section class="dark line-top">
<div class="wrap duo" style="padding:0">
<div class="rv-in">
<span class="kick">Employers</span>
<h2>Hiring?</h2>
<p>Find out what your vacancy is really costing you. Three quick tools, instant results, no obligation.</p>
<a class="btn btn-gold arrow" href="{CAREERS:hire/|final_cta}">Get your free hiring score</a>
<p class="sm">Ready to brief us? <a class="tlink" href="{R}contact/?type=employer">Send us a vacancy</a></p>
</div>
<div class="rv-in">
<span class="kick">Candidates</span>
<h2>Looking for work?</h2>
<p>Sharpen your CV for free, then join our talent pool so we can match you as roles open.</p>
<a class="btn btn-line arrow" href="{CAREERS:talent-suite/career/|final_cta}">Try the free Career Toolkit</a>
<p class="sm">Already job-ready? <a class="tlink" href="{CAREERS:talent-pool/|final_cta}">Upload your CV</a></p>
</div>
</div>
</section>
'''

HOME = f'''<section class="dark hero center">
<div class="wrap">
<img class="mark" src="{{R}}assets/logo-mark.png" alt="" width="150" height="137">
<h1>Specialist talent.<br><em>Delivered with care.</em></h1>
<p class="lead">UK-wide recruitment across engineering, technical, commercial and professional roles. Plus free tools that help employers hire smarter and candidates get seen.</p>
<p class="tagline">Anyone · Anywhere · Anytime</p>
<div class="btns">
<a class="btn btn-gold arrow" href="{{CAREERS:hire/|hero}}">I'm hiring</a>
<a class="btn btn-line arrow" href="{{CAREERS:|hero}}">I'm looking for work</a>
</div>
</div>
</section>

<div class="trust" role="region" aria-label="Why Live 2 Help">
<ul>
<li><span class="stars">★★★★★</span> 5.0 rated on Google</li>
<li><i class="dot"></i>UK-wide coverage</li>
<li><i class="dot"></i>3-month replacement guarantee</li>
<li><i class="dot"></i>Shortlist in week one</li>
</ul>
</div>

<section class="sec" id="employers">
<div class="wrap">
<span class="kick">For employers</span>
<h2 class="h2">Hire smarter, starting today</h2>
<div class="split mt">
<div class="card feature rv-in">
{TOOLKIT_PANEL}
<h3>Free Hiring Toolkit</h3>
<p>Find out what an empty seat is really costing you, score your hiring process and test whether your offer will land. Three quick tools, instant results, no obligation.</p>
<a class="btn btn-gold arrow" href="{{CAREERS:hire/|employers}}">Get your free hiring score</a>
</div>
<div class="rv-in">
<h3 style="font-size:22px;margin-bottom:6px">How we help</h3>
<ul class="ticks">
<li><i class="dot"></i><div>Permanent recruitment<small>Contingency as standard. No placement, no fee.</small></div></li>
<li><i class="dot"></i><div>Retained search<small>For director and senior leadership roles.</small></div></li>
<li><i class="dot"></i><div>Temporary and contract placements<small>Flexible cover with a clear route to permanent.</small></div></li>
<li><i class="dot"></i><div>Written submission packs, not loose CVs<small>Every candidate mapped to your brief before you see them.</small></div></li>
</ul>
<p style="margin-top:24px"><a class="tlink" href="{{R}}employers/">See how we work with employers</a></p>
<p>Prefer to talk first? Email <a class="tlink" href="mailto:office@live2helprecruitment.co.uk">office@live2helprecruitment.co.uk</a></p>
</div>
</div>
</div>
</section>

<section class="sec line-top" id="candidates">
<div class="wrap">
<span class="kick">For candidates</span>
<h2 class="h2">Get past the filter</h2>
<p class="lead">Most CVs are rejected before a person ever reads them. We help you get past the filter and in front of the hiring manager.</p>
<div class="g3 mt">
<div class="card rv-in"><div class="num">01 · Live roles</div><h3>Browse current roles</h3><p>See the opportunities we are recruiting for right now and apply in a few minutes.</p><a class="btn btn-ink arrow" href="{{CAREERS:|candidates}}">View live roles</a></div>
<div class="card dk rv-in"><div class="num">02 · Free</div><h3>Career Toolkit</h3><p>Free CV and application tools that help you sharpen your CV before you apply.</p><div class="price">Free to use</div><a class="btn btn-gold arrow" href="{{CAREERS:talent-suite/career/|candidates}}">Try it free</a></div>
<div class="card rv-in"><div class="num">03 · Talent Suite</div><h3>Expert CV Review</h3><p>A human review of your CV from our recruiters, returned within 3 working days.</p><div class="price">From £25</div><a class="btn btn-ink arrow" href="{{CAREERS:talent-suite/|expert}}">Get expert help</a></div>
</div>
<p class="mt" style="margin-top:28px">Not seeing the right role? <a class="tlink" href="{{CAREERS:talent-pool/|candidates}}">Join our talent pool</a></p>
</div>
</section>

<section class="sec paper line-top">
<div class="wrap">
<span class="kick">How it works</span>
<h2 class="h2">Two weeks to placement</h2>
<ol class="steps mt">
<li class="rv-in"><div class="n">01</div><div class="when">Day one</div><h3>Briefing call</h3><p>A proper conversation, not a form. We learn the role, the team and what good looks like.</p></li>
<li class="rv-in"><div class="n">02</div><div class="when">Week one</div><h3>Your shortlist</h3><p>Every candidate is screened before you see them and arrives as a written submission pack.</p></li>
<li class="rv-in"><div class="n">03</div><div class="when">Week two</div><h3>Interview and placement</h3><p>Our target is two weeks from first conversation to placement, backed by our 3-month replacement guarantee.</p></li>
</ol>
</div>
</section>

<section class="sec dark">
<div class="wrap">
<span class="kick">Roles we place</span>
<h2 class="h2">Twelve sectors, one standard</h2>
<div class="g4 mt">{sector_tiles()}</div>
<div style="margin-top:56px;padding-top:40px;border-top:1px solid var(--line-d)">
<h3 style="font-size:15px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:22px">Recent placements</h3>
<div class="chips">
<div class="chip">NPD Technician<span>UK manufacturer</span></div>
<div class="chip">Category Manager, Metal Components<span>UK manufacturer</span></div>
<div class="chip">CAD Technician<span>Engineering</span></div>
<div class="chip">Finance Manager<span>Multi-site business</span></div>
<div class="chip">Industrial and Production Operatives<span>Several roles, one site</span></div>
</div>
</div>
</div>
</section>

{reviews_block()}

{FINAL_CTA}'''

EMPLOYERS = f'''<section class="dark page-hero">
<div class="wrap">
<span class="kick">For employers</span>
<h1>Every empty seat costs you<br>more than you think.</h1>
<p class="lead">A role goes live. Forty CVs land in your inbox. Half do not fit the brief, the interviews go nowhere, and the one good candidate takes a counteroffer. We are not a volume agency, and we never will be.</p>
<div class="btns">
<a class="btn btn-gold arrow" href="{{CAREERS:hire/|hero}}">Get your free hiring score</a>
<a class="btn btn-line" href="{{R}}contact/?type=employer">Send us a vacancy</a>
</div>
</div>
</section>

<section class="sec">
<div class="wrap split">
<div class="rv-in">
<span class="kick">Start here</span>
<h2 class="h2">The free Hiring Toolkit</h2>
<p class="lead">Three short tools, one after the other. You see the maths behind every number, and you leave with a clear picture of where your hiring is losing time and money.</p>
<ul class="ticks" style="margin-top:20px">
<li><i class="dot"></i><div>Vacancy cost calculator<small>What the empty seat is costing you each week, with every figure shown.</small></div></li>
<li><i class="dot"></i><div>Hiring health score<small>Where your process is slowing hires down.</small></div></li>
<li><i class="dot"></i><div>Offer strength check<small>Whether your offer will land or lose to a counteroffer.</small></div></li>
</ul>
<div class="btns" style="margin-top:28px"><a class="btn btn-gold arrow" href="{{CAREERS:hire/|toolkit}}">Start the toolkit</a></div>
</div>
<div class="card feature rv-in">{TOOLKIT_PANEL}<p style="margin:0">Takes around five minutes. Your results are yours to keep, with no obligation to work with us.</p></div>
</div>
</section>

<section class="sec paper line-top">
<div class="wrap">
<span class="kick">Services</span>
<h2 class="h2">Three ways to work with us</h2>
<div class="g3 mt">
<div class="card rv-in"><div class="num">Permanent</div><h3>Contingency recruitment</h3><p>Our standard model. No placement, no fee. Fees are banded by salary, charged on basic salary rather than OTE and agreed in writing before we begin.</p></div>
<div class="card dk rv-in"><div class="num">Senior hires</div><h3>Retained search</h3><p>For director and senior leadership roles. A commitment fee at instruction and the balance on placement, with a confidential, fully managed search.</p></div>
<div class="card rv-in"><div class="num">Flexible</div><h3>Temporary and contract</h3><p>Cover for peaks, projects and absences, with a clear and fair route if you want to make a temporary worker permanent.</p></div>
</div>
</div>
</section>

<section class="sec">
<div class="wrap">
<span class="kick">How we work</span>
<h2 class="h2">Two weeks from first conversation to placement</h2>
<p class="lead">Six clear stages. Our target is two weeks, with the pace set by your interview availability and how quickly decisions are made.</p>
<ol class="steps six mt">
<li class="rv-in"><div class="n">01</div><div class="when">Day 1</div><h3>Briefing call</h3><p>The role, your team, your culture and what has not worked before.</p></li>
<li class="rv-in"><div class="n">02</div><div class="when">Days 1 to 5</div><h3>Active sourcing</h3><p>Targeted search, headhunting, referrals and advertising.</p></li>
<li class="rv-in"><div class="n">03</div><div class="when">Days 3 to 7</div><h3>Screening</h3><p>Salary, notice, motivation, fit and the competencies you need.</p></li>
<li class="rv-in"><div class="n">04</div><div class="when">Week 1</div><h3>Submission packs</h3><p>Written packs, not loose CVs, so you decide in minutes.</p></li>
<li class="rv-in"><div class="n">05</div><div class="when">Week 2</div><h3>Interviews</h3><p>We schedule, confirm and prepare every candidate for your format.</p></li>
<li class="rv-in"><div class="n">06</div><div class="when">Offer</div><h3>Offer and placement</h3><p>We manage the offer, handle counteroffers and stay close to the start.</p></li>
</ol>
</div>
</section>

<section class="sec paper line-top">
<div class="wrap split">
<div class="rv-in">
<span class="kick">What lands in your inbox</span>
<h2 class="h2">A submission pack, not a CV dump</h2>
<p class="lead">Every candidate we put forward comes with a written submission that maps their experience directly to your brief. It saves your time and sharpens every shortlist decision.</p>
</div>
<div class="card feature rv-in">
<div class="num">Example submission</div>
<h3>Candidate A · Category Buyer</h3>
<ul class="ticks">
<li><i class="dot"></i><div>Fit against your brief<small>Each requirement matched to evidence from their career.</small></div></li>
<li><i class="dot"></i><div>Salary, notice and availability<small>Confirmed in conversation, not guessed from a CV.</small></div></li>
<li><i class="dot"></i><div>Motivation and reasons for moving<small>So you know the risk of a counteroffer up front.</small></div></li>
<li><i class="dot"></i><div>Our recommendation<small>Why we think they are worth your time.</small></div></li>
</ul>
</div>
</div>
</section>

<section class="sec">
<div class="wrap">
<span class="kick">Aftercare</span>
<h2 class="h2">The placement is not the finish line</h2>
<p class="lead">Most agencies disappear once the invoice is raised. We stay close, because a hire only counts if it works.</p>
<div class="g3 mt">
<div class="card rv-in"><div class="num">01</div><h3>Offer and counteroffer</h3><p>We handle the offer conversation and protect the hire if a counteroffer appears.</p></div>
<div class="card rv-in"><div class="num">02</div><h3>Pre-start onboarding</h3><p>Your new starter gets start details, first-week expectations and a day one checklist.</p></div>
<div class="card rv-in"><div class="num">03</div><h3>Client handover pack</h3><p>Employment details, right to work confirmation and references in one place.</p></div>
<div class="card rv-in"><div class="num">04</div><h3>Week 1 check-in</h3><p>We speak to you and your new starter at the end of the first week.</p></div>
<div class="card rv-in"><div class="num">05</div><h3>Month 1 check-in</h3><p>A second conversation, so anything small is caught early.</p></div>
<div class="card dk rv-in"><div class="num">06</div><h3>3-month guarantee</h3><p>If your hire leaves or is dismissed for performance within three months, we find you a replacement.</p></div>
</div>
</div>
</section>

<section class="sec dark">
<div class="wrap">
<span class="kick">Terms</span>
<h2 class="h2">Simple, transparent terms</h2>
<table class="terms mt">
<tr><th scope="row">Basis</th><td>Contingency as standard: no placement, no fee. Retained search for director and senior leadership roles.</td></tr>
<tr><th scope="row">Fees</th><td>Banded by salary and charged on basic salary, not OTE. Agreed in writing before we begin.</td></tr>
<tr><th scope="row">Guarantee</th><td>3-month replacement guarantee on every permanent placement.</td></tr>
<tr><th scope="row">Payment terms</th><td>14 days from the invoice date.</td></tr>
<tr><th scope="row">Timeline</th><td>Our target is two weeks from first conversation to placement.</td></tr>
<tr><th scope="row">Coverage</th><td>UK-wide. Remote, hybrid and on-site roles at every level.</td></tr>
</table>
<p style="margin-top:22px;font-size:15px">Full conditions are set out in our Terms of Engagement, shared at briefing stage.</p>
</div>
</section>

{FINAL_CTA}'''

CANDIDATES = f'''<section class="dark page-hero">
<div class="wrap">
<span class="kick">For candidates</span>
<h1>Get past the filter.<br><em class="gold-t" style="font-style:normal">Get in front of the hiring manager.</em></h1>
<p class="lead">Most CVs are rejected by software before a person reads them. We give you free tools to fix that, real roles to apply for and a recruiter who stays with you through every stage.</p>
<div class="btns">
<a class="btn btn-gold arrow" href="{{CAREERS:|hero}}">View live roles</a>
<a class="btn btn-line arrow" href="{{CAREERS:talent-suite/career/|hero}}">Free Career Toolkit</a>
</div>
</div>
</section>

<section class="sec">
<div class="wrap">
<span class="kick">The Talent Suite</span>
<h2 class="h2">Everything you need to land the role</h2>
<p class="lead">Start free. Add expert help from our recruiters when you want a second pair of eyes.</p>
<div class="g3 mt">
<div class="card rv-in"><div class="num">Free</div><h3>Career Toolkit</h3><p>CV and application tools that help you sharpen your CV, tailor it to a role and prepare before you apply.</p><div class="price">Free to use</div><a class="btn btn-ink arrow" href="{{CAREERS:talent-suite/career/|tiers}}">Try it free</a></div>
<div class="card rv-in"><div class="num">Expert</div><h3>Expert CV Review</h3><p>One of our recruiters reviews your CV and tells you exactly what to change, returned within 3 working days.</p><div class="price">£25</div><a class="btn btn-ink arrow" href="{{CAREERS:talent-suite/|tiers}}">Get a CV review</a></div>
<div class="card dk rv-in"><div class="num">Best value</div><h3>CV Review and Interview Coaching</h3><p>Your CV review plus interview coaching, so you walk in prepared for the questions that matter.</p><div class="price">£49</div><a class="btn btn-gold arrow" href="{{CAREERS:talent-suite/|tiers}}">Get the full package</a></div>
</div>
</div>
</section>

<section class="sec paper line-top">
<div class="wrap split">
<div class="rv-in">
<span class="kick">When we represent you</span>
<h2 class="h2">You are never just a CV to us</h2>
<p class="lead">When you apply for one of our roles, you get a recruiter who prepares you properly and keeps you informed.</p>
</div>
<ul class="ticks rv-in">
<li><i class="dot"></i><div>An honest conversation first<small>We check the role genuinely fits before we put you forward.</small></div></li>
<li><i class="dot"></i><div>A written submission to the employer<small>Your strengths matched to their brief, not lost in a pile of CVs.</small></div></li>
<li><i class="dot"></i><div>A tailored interview prep pack<small>Built around that employer's interview format, round by round.</small></div></li>
<li><i class="dot"></i><div>Feedback, whatever the outcome<small>We tell you where you stand and keep you in mind for the next role.</small></div></li>
<li><i class="dot"></i><div>Support after you start<small>Week 1 and Month 1 check-ins so your new job starts well.</small></div></li>
</ul>
</div>
</section>

<section class="sec dark">
<div class="wrap center">
<span class="kick">Not seeing the right role?</span>
<h2 class="h2">Join our talent pool</h2>
<p class="lead">Upload your CV once and we will match you to new roles as they open across the UK.</p>
<div class="btns mt"><a class="btn btn-gold arrow" href="{{CAREERS:talent-pool/|talent_pool}}">Upload your CV</a></div>
</div>
</section>

{reviews_block('What candidates say about us')}'''

def sectors_page():
    cards = []
    for slug, name, desc, roles in SECTORS:
        cards.append(f'<article class="sector rv-in" id="{slug}"><h3><i class="dot"></i>{name}</h3><p>{desc}</p><div class="roles"><b>Typical roles</b>{roles}</div></article>')
    return f'''<section class="dark page-hero">
<div class="wrap">
<span class="kick">Sectors</span>
<h1>Twelve sectors.<br><em class="gold-t" style="font-style:normal">One standard.</em></h1>
<p class="lead">Whether you are hiring one specialist or scaling an entire team, every brief gets the same rigorous process, with particular depth in engineering, industrial, procurement, commercial and technical roles.</p>
<div class="btns"><a class="btn btn-gold arrow" href="{{R}}contact/?type=employer">Send us a vacancy</a><a class="btn btn-line arrow" href="{{CAREERS:|hero}}">View live roles</a></div>
</div>
</section>
<section class="sec paper">
<div class="wrap">
<div class="g3">{''.join(cards)}</div>
<p class="center" style="margin-top:44px">Hiring for a role that is not listed here? <a class="tlink" href="{{R}}contact/?type=employer">Tell us about it</a> and we will tell you honestly whether we can help.</p>
</div>
</section>
{FINAL_CTA}'''

ABOUT = f'''<section class="dark page-hero">
<div class="wrap">
<span class="kick">About us</span>
<h1>We are not a volume agency.<br><em class="gold-t" style="font-style:normal">We never will be.</em></h1>
<p class="lead">Live 2 Help Recruitment was built on a simple belief: the right hire is not about matching a CV to a job description. It is about understanding what your business actually needs, and finding the person who delivers it from day one.</p>
</div>
</section>

<section class="sec">
<div class="wrap split">
<div class="rv-in">
<span class="kick">Our story</span>
<h2 class="h2">Founder-led and deliberately boutique</h2>
<p class="lead">We have been trading for over nine years, recruiting across engineering, procurement, commercial, technical and industrial sectors across the UK.</p>
<p>Being small is a choice. Your brief gets personal attention from people who understand your sector, rather than a bulk send to an unqualified list. You always know exactly who is working on your role.</p>
<p>We have also built our own tools around the way we work: a free Hiring Toolkit for employers, a Talent Suite that helps candidates get seen, and the systems behind every submission pack and prep pack we produce.</p>
</div>
<div class="g2 rv-in" style="gap:16px">
<div class="card dk"><div class="num">9+ years</div><h3>Recruiting</h3><p style="margin:0">Across commercial, engineering and technical roles.</p></div>
<div class="card"><div class="num">UK-wide</div><h3>Coverage</h3><p style="margin:0">Remote, hybrid and on-site roles.</p></div>
<div class="card"><div class="num">2 weeks</div><h3>Target</h3><p style="margin:0">From first conversation to placement.</p></div>
<div class="card dk"><div class="num">3 months</div><h3>Guarantee</h3><p style="margin:0">On every permanent placement.</p></div>
</div>
</div>
</section>

<section class="sec paper line-top">
<div class="wrap split">
<div class="rv-in">
<span class="kick">The team</span>
<h2 class="h2">You get people, not a ticket queue</h2>
<p class="lead">Your brief is handled by a small team of highly experienced recruiters who understand your sector, ask the right questions and take personal responsibility for the outcome.</p>
</div>
<ul class="ticks rv-in">
<li><i class="dot"></i><div>One named contact for every brief<small>You always know who is working on your role and how to reach them.</small></div></li>
<li><i class="dot"></i><div>Sector knowledge, not scripts<small>Experience across engineering, industrial, procurement, commercial and technical hiring.</small></div></li>
<li><i class="dot"></i><div>Founder-led<small>The person who built the business stays close to every partnership.</small></div></li>
<li><i class="dot"></i><div>No handoffs, no call centres<small>The people who take your brief are the people who deliver it.</small></div></li>
</ul>
</div>
</section>

<section class="sec dark" id="values">
<div class="wrap">
<span class="kick">Our values</span>
<h2 class="h2">What we stand for</h2>
<p class="lead">Six values that guide every conversation, every shortlist and every tool we build.</p>
<div class="g3 mt values">
<div class="card rv-in"><h3>Help first</h3><p>Our name is our promise. Every conversation should leave someone better off, whether or not a fee ever follows.</p><small>Free tools for employers and candidates. Honest feedback for every applicant.</small></div>
<div class="card rv-in"><h3>Open doors</h3><p>Anyone. Anywhere. Anytime. Opportunity should not depend on your postcode, your background or your budget.</p><small>UK-wide coverage. Free Career Toolkit. Expert help priced for real job seekers.</small></div>
<div class="card rv-in"><h3>Straight talk</h3><p>We show our working. Clear terms, figures you can check and honest answers, even when they are not the ones people hoped for.</p><small>No small print. Real reviews only. Every number in our toolkit explained.</small></div>
<div class="card rv-in"><h3>Fit over volume</h3><p>The right person, not the most CVs. Every introduction we make is one we would put our own name to.</p><small>Written submission packs. Every candidate spoken to before you see them.</small></div>
<div class="card rv-in"><h3>In it for the long run</h3><p>Partnerships, not transactions. A hire only counts if it works, so we stay close long after the start date.</p><small>Week 1 and Month 1 check-ins. 3-month replacement guarantee.</small></div>
<div class="card rv-in"><h3>Build better</h3><p>We keep improving how recruitment is done, and we build our own tools when the old way is not good enough.</p><small>Hiring Toolkit, Talent Suite and our own systems behind every shortlist.</small></div>
</div>
</div>
</section>

{reviews_block()}

{FINAL_CTA}'''

CONTACT = '''<section class="dark page-hero">
<div class="wrap">
<span class="kick">Contact</span>
<h1>Let's talk.</h1>
<p class="lead">Send us a vacancy, ask a question or tell us what you are looking for. We reply within one working day.</p>
</div>
</section>

<section class="sec">
<div class="wrap split">
<div>
<form class="form" id="contact-form" action="https://l2h-api.onrender.com/api/website-enquiry" method="POST" novalidate>
<div class="hp" aria-hidden="true"><label for="website">Leave this empty</label><input id="website" type="text" name="website" tabindex="-1" autocomplete="off"></div>
<div>
<label for="enquiry_type">I am</label>
<select id="enquiry_type" name="enquiry_type" required>
<option value="employer">An employer looking to hire</option>
<option value="candidate">A candidate looking for work</option>
<option value="other">Something else</option>
</select>
</div>
<div class="two">
<div><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required></div>
<div><label for="company">Company (if hiring)</label><input id="company" name="company" autocomplete="organization"></div>
</div>
<div class="two">
<div><label for="email">Email</label><input id="email" type="email" name="email" autocomplete="email" required></div>
<div><label for="phone">Phone (optional)</label><input id="phone" type="tel" name="phone" autocomplete="tel"></div>
</div>
<div><label for="message">How can we help?</label><textarea id="message" name="message" required placeholder="For a vacancy, tell us the role, location and salary range."></textarea></div>
<label class="consent"><input type="checkbox" id="consent" name="consent" value="yes" required><span>I agree to Live 2 Help Recruitment using these details to reply to my enquiry, as set out in the <a class="tlink" href="{R}legal/privacy-policy/">privacy policy</a>.</span></label>
<div><button class="btn btn-gold" type="submit">Send message</button></div>
<div class="form-msg" id="form-msg" role="status" aria-live="polite"></div>
</form>
</div>
<aside class="contact-card">
<h3>Get in touch directly</h3>
<div class="item"><b>Email</b><a href="mailto:office@live2helprecruitment.co.uk">office@live2helprecruitment.co.uk</a></div>
<div class="item"><b>Phone</b><a href="tel:+441902945444">01902 945444</a></div>
<div class="item"><b>Coverage</b>UK-wide. Remote, hybrid and on-site roles.</div>
<div class="item" style="border:0"><b>Prefer to start with a tool?</b>Employers: <a href="{CAREERS:hire/|contact}">free Hiring Toolkit</a><br>Candidates: <a href="{CAREERS:talent-suite/career/|contact}">free Career Toolkit</a></div>
</aside>
</div>
</section>'''

NOT_FOUND = '''<section class="dark page-hero center">
<div class="wrap">
<span class="kick">Page not found</span>
<h1>This page has moved.</h1>
<p class="lead">We have rebuilt our website. Pick where you were heading and we will get you there.</p>
<div class="btns"><a class="btn btn-gold" href="{R}">Home</a><a class="btn btn-line" href="{R}employers/">Employers</a><a class="btn btn-line" href="{CAREERS:|404}">Live roles</a><a class="btn btn-line" href="{R}contact/">Contact</a></div>
</div>
</section>'''

PAGES = [
    dict(path='', title='Live 2 Help Recruitment | Specialist UK Recruitment Agency',
         desc='UK-wide specialist recruitment across engineering, technical, commercial and professional roles, with a free Hiring Toolkit for employers and a Talent Suite for candidates.',
         body=HOME, active='', medium='homepage'),
    dict(path='employers/', title='For Employers | Live 2 Help Recruitment',
         desc='Permanent, retained and temporary recruitment with written submission packs, a two-week placement target and a 3-month replacement guarantee.',
         body=EMPLOYERS, active='employers/'),
    dict(path='candidates/', title='For Candidates | Live 2 Help Recruitment',
         desc='Live roles, a free Career Toolkit and expert CV reviews from our recruiters. Get past the filter and in front of the hiring manager.',
         body=CANDIDATES, active='candidates/'),
    dict(path='sectors/', title='Sectors We Recruit For | Live 2 Help Recruitment',
         desc='Twelve sectors including engineering, manufacturing, procurement, commercial, finance, IT, construction, care, HR, executive and logistics.',
         body=sectors_page(), active='sectors/'),
    dict(path='about/', title='About Us | Live 2 Help Recruitment',
         desc='A founder-led, boutique recruitment agency trading for over nine years, and the values behind every hire we make.',
         body=ABOUT, active='about/'),
    dict(path='contact/', title='Contact Us | Live 2 Help Recruitment',
         desc='Send us a vacancy or ask a question. Email office@live2helprecruitment.co.uk or call 01902 945444.',
         body=CONTACT, active='contact/'),
    dict(path='404/', file='404.html', root='/', noindex=True, title='Page not found | Live 2 Help Recruitment',
         desc='This page has moved.', body=NOT_FOUND, medium='404'),
]
