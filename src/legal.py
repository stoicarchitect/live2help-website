# Policy pages for the Live 2 Help main website.
# Wording carried over from the GoDaddy site, tidied: typos fixed, contact
# emails consolidated to office@, legislation names brought up to date,
# and text copied from another company's policy removed.

UPDATED = 'Last updated October 2026'
OFFICE = '<a class="tlink" href="mailto:office@live2helprecruitment.co.uk">office@live2helprecruitment.co.uk</a>'

LEGAL_NAV = [
    ('legal/website-terms/', 'Website terms'),
    ('legal/privacy-policy/', 'Privacy policy'),
    ('legal/ethical-behaviour-policy/', 'Ethical behaviour'),
    ('legal/child-labour-policy/', 'Child labour'),
    ('legal/whistleblowing-policy/', 'Whistleblowing'),
]

def wrap(path, title, body):
    cur = ' aria-current="page"'
    nav = ''.join('<a href="{R}' + p + '"' + (cur if p == path else '') + '>' + t + '</a>' for p, t in LEGAL_NAV)
    return f'''<section class="dark page-hero">
<div class="wrap"><span class="kick">Policies</span><h1>{title}</h1></div>
</section>
<section class="sec">
<div class="wrap">
<nav class="legal-nav" aria-label="Policies">{nav}</nav>
<article class="legal">
<p class="meta">Live 2 Help Recruitment Ltd · Company no. 11731080 · {UPDATED}</p>
{body}
</article>
</div>
</section>'''

TERMS = f'''<p>This page, together with the documents referred to on it, tells you the terms on which you may access or use this website (our site), whether as a guest or a registered user. By using our site, you accept these terms of use and agree to abide by them.</p>
<h2>Information about us</h2>
<p>This site is operated by Live 2 Help Recruitment Ltd ("we", "us"), registered in England and Wales under company number 11731080.</p>
<h2>Accessing our site</h2>
<p>Access to our site is permitted on a temporary basis, and we reserve the right to withdraw or amend the service we provide on our site without notice. We will not be liable if for any reason our site is unavailable at any time or for any period.</p>
<p>From time to time, we may restrict access to some parts of our site, or our entire site, to users who have registered with us. If you are given a user identification code, password or any other piece of information as part of our security procedures, you must treat it as confidential and must not disclose it to any third party. We may disable any user identification code or password at any time if, in our opinion, you have failed to comply with these terms.</p>
<p>You are responsible for making all arrangements necessary for you to have access to our site, and for ensuring that anyone who accesses our site through your internet connection is aware of these terms and complies with them.</p>
<h2>Intellectual property rights</h2>
<p>We are the owner or the licensee of all intellectual property rights in our site and in the material published on it. Those works are protected by copyright laws and treaties around the world. All such rights are reserved.</p>
<p>You may print off one copy, and may download extracts, of any page from our site for your personal reference. You must not modify the paper or digital copies of any materials you have printed or downloaded, and you must not use any illustrations, photographs, video or audio sequences or any graphics separately from any accompanying text.</p>
<p>Our status (and that of any identified contributors) as the authors of material on our site must always be acknowledged. You must not use any part of the materials on our site for commercial purposes without obtaining a licence to do so from us or our licensors. If you print off, copy or download any part of our site in breach of these terms, your right to use our site will cease immediately and you must, at our option, return or destroy any copies of the materials you have made.</p>
<h2>Reliance on information posted</h2>
<p>Commentary and other materials posted on our site are not intended to amount to advice on which reliance should be placed. We therefore disclaim all liability and responsibility arising from any reliance placed on such materials by any visitor to our site, or by anyone who may be informed of any of its contents.</p>
<h2>Our site changes regularly</h2>
<p>We aim to update our site regularly and may change the content at any time. If the need arises, we may suspend access to our site or close it indefinitely. Any of the material on our site may be out of date at any given time, and we are under no obligation to update it.</p>
<h2>Our liability</h2>
<p>The material displayed on our site is provided without any guarantees, conditions or warranties as to its accuracy. To the extent permitted by law, we, other members of our group of companies and third parties connected to us expressly exclude:</p>
<ul>
<li>all conditions, warranties and other terms which might otherwise be implied by statute, common law or the law of equity; and</li>
<li>any liability for any direct, indirect or consequential loss or damage incurred by any user in connection with our site, or in connection with the use, inability to use or results of the use of our site, any websites linked to it and any materials posted on it, including liability for loss of income or revenue, loss of business, loss of profits or contracts, loss of anticipated savings, loss of data, loss of goodwill, wasted management or office time, and any other loss or damage of any kind, however arising and whether caused by tort (including negligence), breach of contract or otherwise, even if foreseeable.</li>
</ul>
<p>This does not affect our liability for death or personal injury arising from our negligence, our liability for fraudulent misrepresentation or misrepresentation as to a fundamental matter, or any other liability which cannot be excluded or limited under applicable law.</p>
<h2>Information about you and your visits to our site</h2>
<p>We process information about you in accordance with our <a class="tlink" href="{{R}}legal/privacy-policy/">privacy policy</a>. By using our site, you warrant that all data you provide is accurate.</p>
<h2>Uploading material to our site</h2>
<p>Where a feature allows you to upload material to our site or to our careers site, such as a CV, you warrant that the material is accurate and that you are entitled to share it. We will use it only as set out in our privacy policy. We may remove any material you upload if, in our opinion, it is inappropriate or unlawful.</p>
<h2>Viruses, hacking and other offences</h2>
<p>You must not misuse our site by knowingly introducing viruses, trojans, worms, logic bombs or other material which is malicious or technologically harmful. You must not attempt to gain unauthorised access to our site, the server on which it is stored or any server, computer or database connected to it. You must not attack our site via a denial-of-service attack or a distributed denial-of-service attack.</p>
<p>By breaching this provision, you would commit a criminal offence under the Computer Misuse Act 1990. We will report any such breach to the relevant law enforcement authorities and will co-operate with them by disclosing your identity. In the event of such a breach, your right to use our site will cease immediately.</p>
<p>We will not be liable for any loss or damage caused by a distributed denial-of-service attack, viruses or other technologically harmful material that may infect your computer equipment, computer programs, data or other proprietary material due to your use of our site or your downloading of any material posted on it, or on any website linked to it.</p>
<h2>Linking to our site</h2>
<p>You may link to our home page, provided you do so in a way that is fair and legal and does not damage our reputation or take advantage of it. You must not establish a link in such a way as to suggest any form of association, approval or endorsement on our part where none exists, and you must not establish a link from any website that is not owned by you. Our site must not be framed on any other site. We reserve the right to withdraw linking permission without notice.</p>
<p>If you wish to make any use of material on our site other than that set out above, please contact {OFFICE}.</p>
<h2>Links from our site</h2>
<p>Where our site contains links to other sites and resources provided by third parties, these links are provided for your information only. We have no control over the contents of those sites or resources and accept no responsibility for them or for any loss or damage that may arise from your use of them.</p>
<h2>Jurisdiction and applicable law</h2>
<p>The English courts will have non-exclusive jurisdiction over any claim arising from, or related to, a visit to our site, although we retain the right to bring proceedings against you for breach of these conditions in your country of residence or any other relevant country. These terms of use are governed by English law.</p>
<h2>Variations</h2>
<p>We may revise these terms of use and our privacy policy at any time by amending the appropriate page. Please check these pages from time to time to take notice of any changes we make, as they are binding on you. Some of the provisions contained in these terms may also be superseded by provisions or notices published elsewhere on our site.</p>
<h2>Your concerns</h2>
<p>If you have any concerns about material which appears on our site, please contact {OFFICE}.</p>
<p>Thank you for visiting our site.</p>'''

PRIVACY = f'''<p>Live 2 Help Recruitment Ltd ("the Company") is a recruitment business which provides work-finding services to its Clients and Candidates. The Company must process personal data (including sensitive personal data) so that it can provide these services, and in doing so the Company is responsible for your personal data. You may give your personal details to the Company directly, such as on an application or registration form or via our websites, or we may collect them from another source such as a jobs board. The Company must have a legal basis for processing your personal data. For the purposes of providing you with work-finding services and/or information relating to roles relevant to you, we will only use your personal data in accordance with this notice.</p>
<p>This notice will be updated as required.</p>
<h2>1. Definitions</h2>
<ul>
<li><b>Candidate(s)</b> means any individual who registers with the Company for the purposes of obtaining permanent or fixed term employment or temporary work.</li>
<li><b>Client(s)</b> means any organisation, and any individual or employee of that organisation, that the Company provides recruitment services to.</li>
<li><b>Data Protection Legislation</b> means all applicable data protection laws, including the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018.</li>
<li><b>Personal data</b> means any information relating to an individual who can be identified, such as by a name, an identification number, location data, an online identifier or one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that person.</li>
<li><b>Process / processing</b> means any operation performed on personal data, such as collection, recording, organisation, structuring, storage (including archiving), adaptation or alteration, retrieval, consultation, use, disclosure, dissemination, alignment or combination, restriction, erasure or destruction.</li>
<li><b>Sensitive personal data</b> means personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs or trade union membership, and the processing of genetic data, biometric data, data concerning health, an individual's sex life or sexual orientation, and an individual's criminal convictions. In this notice, "personal data" includes sensitive personal data except where we need to refer to sensitive personal data specifically.</li>
<li><b>Supervisory authority</b> means an independent public authority responsible for monitoring the application of data protection. In the UK this is the Information Commissioner's Office (ICO).</li>
<li><b>Supplier(s)</b> means any organisation, and any individual or employee of that organisation, that provides services to the Company.</li>
</ul>
<h2>2. Collection and use of personal data</h2>
<h3>i) Categories of personal data that may be collected</h3>
<p>The categories of personal data the Company may collect depend on the type of contact you have with us.</p>
<p><b>Candidates:</b> name; date of birth; marital status; emergency contact or next of kin; home address; email address; telephone number; CV and work history; education or training; employment history; referee details; photographic ID; nationality; right to work status; record of criminal convictions; sensitive personal data such as sex or gender, ethnicity, physical or mental disabilities, religious beliefs and sexual orientation, which may be collected for equality and diversity monitoring; details of your current salary and bank account; and any additional information that you, your referees or our Clients provide about you.</p>
<p><b>Clients:</b> contact details for you and individuals or employees of your organisation, such as name, work address, email address and telephone number; and details of previous and current job requirements.</p>
<p><b>Suppliers:</b> contact details for you and individuals or employees of your organisation, such as name, work address, email address and telephone number; and bank account details.</p>
<p>If you use our websites, we may also collect other data, such as the dates and times you used them (see section 6). These lists are not exhaustive.</p>
<h3>ii) How we use your personal data</h3>
<p><b>Candidates:</b> the Company will process your personal data to provide you with work-finding services. This includes providing you with job recommendations and submitting your application to potential employers. The Company may also use your personal data for marketing purposes, for equality and diversity monitoring, or as required by law, regulatory bodies or for tax or audit purposes.</p>
<p><b>Clients:</b> the Company will process your personal data to provide you with recruitment services under our agreed terms. The Company may also use your personal data for marketing purposes or as required by law, regulatory bodies or for tax or audit purposes.</p>
<p><b>Suppliers:</b> the Company will process your personal data so that our agreed terms of contract can be carried out efficiently and effectively, and as required by law, regulatory bodies or for tax or audit purposes.</p>
<h3>iii) Our legal basis for processing your personal data</h3>
<p>The legal basis we rely on will generally be legitimate interests.</p>
<p><b>Candidates:</b> if you have applied for a position or submitted your CV to the Company, we need to process your personal data to provide you with work-finding services. This may include carrying out reference checks needed for you to gain employment. If you obtain employment, we may need to process your personal data for payroll and other administration. We may also provide job recommendations tailored to your requirements. We regard all of this as being in our legitimate interests in running a recruitment business and providing appropriate recruitment services.</p>
<p><b>Clients:</b> the Company will store your and your employees' personal data to provide you with suitable Candidates for job positions, together with records of role requirements, meetings, emails and conversations, so that we can continue to provide relevant recruitment services. We consider this to be in our legitimate interests.</p>
<p><b>Suppliers:</b> the Company will process the personal data of your employees and store your bank account details so that you can provide your services and be paid for them. We consider this to be in our legitimate interests as one of your customers.</p>
<p><b>Consent:</b> the Company may need your consent for certain processing activities. Consent must be freely given, specific, informed and unambiguous, and you will be given a specific opt-in. You may withdraw your consent at any time (see section 5).</p>
<h3>iv) Third parties we may share your personal data with</h3>
<p>The Company may share your personal data with our third party service providers where required, such as IT and software providers, professional and business advisers, lawyers, auditors and accountants, and as required by law, regulatory bodies or for tax or audit purposes.</p>
<p><b>Candidates:</b> we may also share your personal data with potential employers or third party recruitment services to assist your search for employment, and with reference agencies where a specific form of reference is required.</p>
<p><b>Clients:</b> we may share your personal data with our Candidates or intermediary organisations (such as MSP or RPO providers) where appropriate.</p>
<p><b>Suppliers:</b> we may share your personal data with third party service providers or as required by law.</p>
<p>These lists are not exhaustive and may be updated as required.</p>
<h2>3. Online tools and payments</h2>
<p>Our careers site offers tools such as the Hiring Toolkit, the Career Toolkit and paid expert services. When you use them, we process the information you enter (for example your CV, answers or company details) to provide the tool or service. Some tools use artificial intelligence services provided by third party processors to generate suggestions; the information you submit is sent to those processors only to produce your result. Payments for paid services are handled by Stripe, our payment provider. We do not see or store your full card or bank details.</p>
<h2>4. Transfers outside the UK</h2>
<p>Some of our service providers may process personal data outside the UK. Where this happens, we take steps to make sure adequate protections are in place, as required by Data Protection Legislation.</p>
<h2>5. Data retention</h2>
<p>The Company will retain your personal data only for as long as is necessary. Different laws require us to keep different data for different periods of time.</p>
<p>The Conduct of Employment Agencies and Employment Businesses Regulations 2003 require us to keep work-seeker records for at least one year from (a) the date of their creation or (b) the date on which we last provided you with work-finding services. We must also keep payroll, holiday pay, sick pay and pensions auto-enrolment records for as long as is legally required by HMRC and associated legislation.</p>
<p>If you are a Candidate or Client and the Company has had no meaningful contact with you for a period of 3 years, your personal data will be deleted unless we are required to keep it by law, for a regulatory body or for tax or audit purposes.</p>
<h2>6. Your rights</h2>
<p>Under Data Protection Legislation, you have the following rights:</p>
<ul>
<li><b>Right to be informed:</b> we must tell you how your personal data will be stored and used, as set out in this notice.</li>
<li><b>Right of access:</b> you can ask for copies of the personal data we hold about you.</li>
<li><b>Right to rectification:</b> if any personal data we hold is inaccurate, you can have it corrected. We may also tell relevant third parties about the change.</li>
<li><b>Right to erasure:</b> you can ask for your personal data to be permanently erased from our records.</li>
<li><b>Right to restrict processing:</b> where erasure is not possible or desirable, you can ask us to stop processing your data and keep it for reference only.</li>
<li><b>Right to data portability:</b> where data is processed by automated means, we will provide it in a format that is easy to move to another system.</li>
<li><b>Right to object:</b> you can object to processing based on legitimate interests or for research purposes, giving your reason. If you object to direct marketing, we will stop immediately.</li>
<li><b>Right not to be subject to automated decision making:</b> you have the right not to be subject to decisions based solely on automated processing that have a legal or similarly significant effect on you, except where the decision is necessary for a contract between you and the Company, is authorised by law, or you have given explicit consent.</li>
<li><b>Right to withdraw consent:</b> where we rely on your consent, you can withdraw it at any time.</li>
</ul>
<p>To use any of these rights, please contact {OFFICE}.</p>
<h2>7. Use of our websites</h2>
<p><b>Cookies:</b> our websites use cookies and similar browser storage to make them work, to remember your progress in our online tools and to understand how they are used. No personal data is stored in these cookies. Most browsers let you refuse cookies, although some features may not work as a result.</p>
<p><b>Data collected:</b> this may include your IP address, the dates and times you access our websites and the pages or roles you look at.</p>
<p><b>How we use it:</b> we use this information for statistical analysis to review, develop and improve our websites. We take all reasonable steps to keep the information we hold secure, although no transmission over the internet can be guaranteed to be completely secure.</p>
<h2>8. Complaints or queries</h2>
<p>If you wish to complain about this notice or any of the procedures set out in it, please contact {OFFICE}. You also have the right to raise concerns with the Information Commissioner's Office on 0303 123 1113 or at <a class="tlink" href="https://ico.org.uk/make-a-complaint/" rel="noopener">ico.org.uk</a>, or with any other relevant supervisory authority, if you believe your data protection rights have not been respected.</p>'''

ETHICAL = f'''<h2>1. Statement</h2>
<p>Live 2 Help Recruitment is committed to the highest standards of ethical conduct and integrity in its business activities in the UK. This policy sets out our position on preventing and prohibiting bribery, in accordance with the Bribery Act 2010. We will not tolerate any form of bribery by, or of, our employees, agents or consultants or any person or body acting on our behalf. Senior management is committed to implementing effective measures to prevent, monitor and eliminate bribery.</p>
<p>Live 2 Help Recruitment may also face criminal liability for unlawful actions taken by its employees or associated persons under the Bribery Act 2010. All employees and associated persons must familiarise themselves and comply with this policy, including any future updates.</p>
<h2>2. Scope</h2>
<p>This policy applies to all employees and officers of Live 2 Help Recruitment, and to temporary workers, consultants, contractors, agents and subsidiaries acting for, or on behalf of, Live 2 Help Recruitment ("associated persons"), within the UK and overseas.</p>
<p>Every employee and associated person acting for, or on behalf of, Live 2 Help Recruitment is responsible for maintaining the highest standards of business conduct. Any breach of this policy is likely to be a serious disciplinary, contractual and criminal matter for the individual concerned and may cause serious damage to the reputation and standing of Live 2 Help Recruitment. Agents, sub-contractors and suppliers must confirm in writing that they have received this policy and will follow it, and confirm each year that it has been followed in their dealings with and on behalf of Live 2 Help Recruitment.</p>
<h2>3. Principles</h2>
<p>We expect everyone working on our behalf to act with integrity and to high standards of ethical conduct. They are expected to:</p>
<ul><li>behave honestly and fairly;</li><li>comply with all legal and regulatory requirements;</li><li>conduct themselves in a manner that enhances the reputation of Live 2 Help Recruitment;</li><li>treat others with respect; and</li><li>safeguard the assets and property of Live 2 Help Recruitment.</li></ul>
<p>They must not:</p>
<ul><li>use their authority or office for personal gain;</li><li>recruit or promote employees other than on their ability;</li><li>take unfair advantage of others through dishonest, unethical or illegal practices;</li><li>misappropriate the assets or property of Live 2 Help Recruitment; or</li><li>depart from this policy or any Live 2 Help Recruitment policy simply on the grounds of "commercial necessity".</li></ul>
<h2>4. Bribery Act 2010</h2>
<p>Under the Bribery Act 2010, a bribe is a financial or other advantage offered or requested with the intention of inducing or rewarding improper performance of a function or activity, or with the knowledge or belief that accepting it would constitute improper performance. A relevant function or activity includes public, state or business activities, or any activity performed during a person's employment or on behalf of another company or individual, where the person is expected to act in good faith, impartially or in a position of trust.</p>
<p>A criminal offence will be committed if an employee or associated person acting for, or on behalf of, Live 2 Help Recruitment offers, promises, gives, requests, receives or agrees to receive a bribe, or offers, promises or gives a bribe to a foreign public official with the intention of influencing that official in the performance of their duties, and Live 2 Help Recruitment does not have adequate procedures in place to prevent bribery.</p>
<h3>4.1 What is prohibited</h3>
<p>Live 2 Help Recruitment prohibits employees and associated persons from offering, promising, giving, soliciting or accepting any bribe. A bribe might be cash, a gift or any other inducement to or from any person or company, whether a public or government official, an official of a state-controlled industry, a political party or a private person or company, and whether the individual is in the UK or overseas. This includes bribes intended to secure any commercial, contractual or regulatory advantage for Live 2 Help Recruitment, or any personal advantage for the individual or anyone connected with them. It also applies to indirect payments, gifts or contributions made through consultants, contractors, agents, sponsors, joint-venture partners, advisers, customers, suppliers or other third parties.</p>
<h3>4.2 Record keeping</h3>
<p>Employees and, where applicable, associated persons must make sure all company records relating to contracts or business activities, including invoices and payment transactions with clients, suppliers and public officials, are accurately maintained. Due diligence should be carried out before entering into any contract, arrangement or relationship with a potential supplier, agent, consultant or representative. Accurate, detailed and up-to-date records must be kept of all corporate hospitality, entertainment or gifts accepted or offered.</p>
<h2>5. Corporate entertainment, gifts, hospitality and promotional expenditure</h2>
<p>Live 2 Help Recruitment permits corporate entertainment, gifts, hospitality and promotional expenditure undertaken to establish or maintain good business relationships, to improve its image and reputation, or to present its services effectively, provided it is arranged in good faith and is not offered, promised or accepted to secure an advantage or to influence the impartiality of the recipient. We will authorise only reasonable, appropriate and proportionate expenditure, whether in the UK or overseas.</p>
<h3>5.1 Charitable donations</h3>
<p>Live 2 Help Recruitment considers that charitable giving can form part of its wider commitment to the community. Any charitable support is given openly, in good faith and never as an inducement.</p>
<h2>6. Financial compliance and financial records</h2>
<p>Our financial records must be complete and accurate so that they reflect the true state of the business and the true nature of all transactions. All books, records, accounts and financial statements must be maintained in reasonable detail, must appropriately reflect our transactions and must conform to applicable legal requirements and generally accepted accounting principles. It is prohibited to:</p>
<ul>
<li>make or approve any payment on the understanding that any part of it will be used for a purpose other than that recorded in our accounts;</li>
<li>establish undisclosed funds or assets, make false or misleading entries in any accounting records, or destroy accounting records within statutory retention periods;</li>
<li>use company funds or assets for any unlawful purpose; or</li>
<li>knowingly make false or inaccurate statements to our accountants or auditors.</li>
</ul>
<h2>7. Confidentiality</h2>
<p>Directors and staff must keep confidential any non-public information entrusted to them by Live 2 Help Recruitment, its clients, candidates or anyone else we do business with. Confidential information should never be disclosed outside the business unless authorised or legally required. This includes business and marketing plans, pricing, contract terms, client, candidate and supplier data, personal data under data protection law, and unpublished financial information. Confidential information must not be improperly collected, stored, distributed, lost or destroyed.</p>
<h2>8. Conflicts of interest</h2>
<p>Everyone working for Live 2 Help Recruitment must avoid situations which may give rise to a conflict of interest. A conflict of interest occurs when the private interests or actions of an individual may interfere with the interests of the business and make it difficult for them to work objectively and effectively. It may also arise where an individual or a member of their family receives improper benefits as a result of their position.</p>
<p>All potential conflicts of interest, including any direct or indirect interest in a competitor, contractor, supplier or consultancy (such as shareholdings or family relationships), must be disclosed to the Managing Director. All corporate hospitality and gifts received in the course of work should also be disclosed.</p>
<h2>9. Responsibilities</h2>
<p><b>Management:</b> the Managing Director is accountable for compliance with this policy and for making sure adequate records are kept to demonstrate compliance. Our financial statements are prepared and reviewed by independent external accountants.</p>
<p><b>Employees:</b> employees and associated persons must help uphold the principles in this policy by acting in a truthful, lawful and ethical manner in all their working practices.</p>
<h2>10. Suspected breaches of this policy</h2>
<p>We encourage an open door culture, so that any queries and concerns can be raised with management. Employees and associated persons should stay vigilant and report any concern as soon as possible to the Managing Director, including:</p>
<ul><li>any suspected or actual attempt at bribery;</li><li>concerns that other employees or associated persons may be being bribed;</li><li>concerns that other employees or associated persons may be bribing third parties, such as clients or officials; or</li><li>any suspected theft or misappropriation of company property.</li></ul>
<p>Anyone who reports suspected bribery or misconduct in good faith will be supported and will not be subjected to detrimental treatment as a result. Detrimental treatment of someone who has made a report will be treated as a disciplinary offence, as will any instruction to cover up wrongdoing. If told not to raise or pursue a concern, even by someone in authority, employees and associated persons should not agree to remain silent.</p>
<p>Live 2 Help Recruitment will fully investigate any alleged or suspected breach. Employees suspected of bribery or misconduct may be suspended while an investigation takes place, and proven allegations may result in a finding of gross misconduct and immediate dismissal. We may terminate the contracts of any associated persons found to have breached this policy and may report any matter to the relevant authorities, including the Serious Fraud Office and the police, and will assist them fully. Concerns can also be raised confidentially under our <a class="tlink" href="{{R}}legal/whistleblowing-policy/">whistleblowing policy</a> or by emailing {OFFICE}.</p>'''

CHILD = f'''<h2>1. Introduction</h2>
<p>Live 2 Help Recruitment's Statement of Principles on Child Labour and Forced Labour is based on International Labour Organisation (ILO) conventions and national laws, and recognises regional and cultural differences. It confirms our commitment to restrict employment to those aged 18 or older, or the local minimum employment age, whichever is higher. It also includes an explicit ban on the use of any forced labour or exploitative working conditions. We believe that promoting fair and appropriate employment, within our business and our supply chains, is a critical part of our commitment to our people and local communities.</p>
<h2>2. Statement of principles on child and forced labour</h2>
<p>2.1 Live 2 Help Recruitment believes it has a responsibility to engage in employment practices that meet the highest legal and ethical standards. Nowhere is this more important than in our policies on the minimum age and working conditions of our own workers and the workers of our suppliers.</p>
<p>2.2 We have developed this Statement of Principles as an expression of our own commitment and of the expectations we have of suppliers. We strongly encourage our suppliers to require their own suppliers to follow these principles too. We will keep these principles relevant and effective, and may amend them from time to time.</p>
<h2>3. Live 2 Help Recruitment's operations</h2>
<p>Live 2 Help Recruitment does not engage in or condone the unlawful employment or exploitation of children in the workplace, or the use of forced labour. In accordance with ILO conventions and national laws, we restrict employment to those aged 18 or older, or the local minimum employment age, whichever is higher. All temporary workers supplied by Live 2 Help Recruitment, and all third party workers who perform work on our behalf, must meet these minimum age requirements. We explicitly prohibit the use of forced labour, meaning any work or service that a worker performs involuntarily or under threat of penalty.</p>
<h2>4. Company suppliers</h2>
<p>Live 2 Help Recruitment will not tolerate the use of unlawful child labour or forced labour, and will not accept products or services from suppliers, subcontractors or business partners (together, "Suppliers") that employ or use child labour or forced labour in any manner. Our Suppliers must not employ or use any individual below the minimum employment age set by national law.</p>
<p>Any concern about child labour or forced labour connected with our business can be raised with {OFFICE}.</p>'''

WHISTLE = f'''<h2>Scope</h2>
<p>This policy takes account of the Public Interest Disclosure Act 1998, which protects workers making disclosures about certain matters of concern, where those disclosures are made in accordance with the Act's provisions. The Act is incorporated into the Employment Rights Act 1996, which already protects employees who act, or raise concerns, about health and safety at work.</p>
<h2>Introduction</h2>
<p>Employees are often the first to realise that something may be seriously wrong within an organisation. However, they may not express their concerns because they feel that speaking up would be disloyal to their colleagues or the organisation, or they may fear harassment or victimisation. Live 2 Help Recruitment wants to make sure that in these circumstances you do not simply ignore the issue. We are committed to the highest possible standards of openness, probity and accountability, and we encourage anyone with serious concerns about any aspect of our work to come forward and voice those concerns without fear of reprisal.</p>
<p>This policy applies to both internal and external workers of Live 2 Help Recruitment. Its purpose is to encourage and enable people to raise serious concerns within the organisation, rather than overlooking a problem or "blowing the whistle" outside the organisation.</p>
<p>This policy covers concerns that fall outside the scope of other procedures. The concern may be about something that is unlawful, falls below the standards expected of Live 2 Help Recruitment, or amounts to improper conduct. We recognise that the decision to report a concern can be difficult, not least because of the fear of reprisal from those responsible for the malpractice.</p>
<h2>How to raise a concern</h2>
<p>Wherever possible, concerns should be raised with the Managing Director, who will investigate thoroughly and sympathetically. You will receive an acknowledgement within five working days and a written response at the end of the investigation. Concerns should be raised in writing to {OFFICE} and should include a short summary of the background and history of the concern, giving names, dates and places where possible, and the reasons why you are particularly concerned.</p>
<p>If the concern relates to the Managing Director, or you are not satisfied with the outcome, you may raise it with an independent adviser nominated by the company or with the relevant external body. At all times, a colleague or companion may accompany you during any discussion of the issues you have raised. While we aim for openness, confidentiality will be maintained throughout.</p>
<h2>What happens next</h2>
<p>Depending on the nature of the concern, Live 2 Help Recruitment will try to resolve the matter as quickly as possible. In some circumstances it may need to be referred to a higher authority, in which case it will take longer to resolve. Once you have reported a concern, you will be told how we propose to deal with it and, where possible, how long it will take to give a final response.</p>
<p>If, after reporting a concern and receiving feedback, you are still not satisfied, you are entitled to report it to a relevant external body, known as a prescribed person. Free, confidential advice is available from the charity Protect at <a class="tlink" href="https://protect-advice.org.uk/" rel="noopener">protect-advice.org.uk</a>.</p>
<p>The terms of this policy do not affect your statutory rights under the Public Interest Disclosure Act 1998.</p>'''

LEGAL = [
    dict(path='legal/website-terms/', title='Website Terms of Use | Live 2 Help Recruitment', desc='The terms on which you may use the Live 2 Help Recruitment website.', body=wrap('legal/website-terms/', 'Website terms of use', TERMS), medium='legal'),
    dict(path='legal/privacy-policy/', title='Privacy Policy | Live 2 Help Recruitment', desc='How Live 2 Help Recruitment collects, uses and protects personal data for candidates, clients and suppliers.', body=wrap('legal/privacy-policy/', 'Privacy policy', PRIVACY), medium='legal'),
    dict(path='legal/ethical-behaviour-policy/', title='Ethical Behaviour Policy | Live 2 Help Recruitment', desc='Our policy on ethical conduct and the prevention of bribery under the Bribery Act 2010.', body=wrap('legal/ethical-behaviour-policy/', 'Ethical behaviour policy', ETHICAL), medium='legal'),
    dict(path='legal/child-labour-policy/', title='Child Labour and Forced Labour Policy | Live 2 Help Recruitment', desc='Our statement of principles on child labour and forced labour.', body=wrap('legal/child-labour-policy/', 'Child labour and forced labour policy', CHILD), medium='legal'),
    dict(path='legal/whistleblowing-policy/', title='Whistleblowing Policy | Live 2 Help Recruitment', desc='How to raise a serious concern about Live 2 Help Recruitment, in confidence and without fear of reprisal.', body=wrap('legal/whistleblowing-policy/', 'Whistleblowing policy', WHISTLE), medium='legal'),
]
