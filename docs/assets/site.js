/* Live 2 Help Recruitment - main site script */
(function(){
  // Mobile menu
  var b = document.querySelector('.burger'), n = document.getElementById('nav');
  if(b && n){
    b.addEventListener('click', function(){
      var open = n.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    n.addEventListener('click', function(e){ if(e.target.tagName === 'A'){ n.classList.remove('open'); b.setAttribute('aria-expanded','false'); } });
  }

  // Gentle reveal on scroll
  var els = document.querySelectorAll('.rv-in');
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('on'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(function(el){ el.classList.add('on'); }); }

  // Contact form: sends to the Live 2 Help ATS (Funnel Leads + a task for Ella + an alert email)
  var f = document.getElementById('contact-form');
  if(f){
    var msg = document.getElementById('form-msg');
    var source = 'website';
    try{
      var q = new URLSearchParams(location.search);
      var t = q.get('type');
      if(t){ var s = f.querySelector('[name="enquiry_type"]'); if(s){ for(var i=0;i<s.options.length;i++){ if(s.options[i].value === t.toLowerCase()){ s.selectedIndex = i; } } } }
      source = (q.get('utm_source') ? q.get('utm_source') + '/' + (q.get('utm_medium') || '') : (document.referrer ? 'website (from ' + new URL(document.referrer).hostname + ')' : 'website'));
    }catch(e){}
    function val(n){ var el = f.querySelector('[name="' + n + '"]'); return el ? el.value.trim() : ''; }
    function fail(text){ msg.className = 'form-msg err'; msg.textContent = text; }
    f.addEventListener('submit', function(e){
      e.preventDefault();
      msg.className = 'form-msg'; msg.textContent = '';
      var type = val('enquiry_type');
      var data = { type: type, name: val('name'), company: val('company'), email: val('email'), phone: val('phone'), message: val('message'), consent: f.querySelector('#consent').checked, website: val('website'), source: source };
      if(data.name.length < 2){ return fail('Please add your name.'); }
      if(!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(data.email)){ return fail('Please check your email address.'); }
      if(type === 'employer' && data.company.length < 2){ return fail('Please add your company name.'); }
      if(data.message.length < 2){ return fail('Please tell us how we can help.'); }
      if(!data.consent){ return fail('Please tick the box so we can reply to you.'); }
      var btn = f.querySelector('button[type="submit"]'); btn.disabled = true; btn.textContent = 'Sending...';
      var slow = setTimeout(function(){ msg.className = 'form-msg'; msg.style.display = 'block'; msg.textContent = 'Still sending, this can take up to a minute.'; }, 6000);
      fetch(f.action, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){ if(!r.ok){ throw new Error(j.error || 'failed'); } return j; }); })
        .then(function(){ f.reset(); msg.removeAttribute('style'); msg.className = 'form-msg ok'; msg.textContent = 'Thank you. Your message is with us and we will reply within one working day.'; })
        .catch(function(err){ msg.removeAttribute('style'); fail(err && err.message && err.message !== 'failed' && err.message !== 'Failed to fetch' ? err.message : 'Sorry, that did not send. Please email office@live2helprecruitment.co.uk or call 01902 945444.'); })
        .then(function(){ clearTimeout(slow); btn.disabled = false; btn.textContent = 'Send message'; });
    });
  }
})();
