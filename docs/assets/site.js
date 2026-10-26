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

  // Contact form (Formspree, emails office@)
  var f = document.getElementById('contact-form');
  if(f){
    var msg = document.getElementById('form-msg');
    // Pre-select enquiry type from ?type=employer or ?type=candidate
    try{
      var t = new URLSearchParams(location.search).get('type');
      if(t){ var s = f.querySelector('[name="enquiry_type"]'); if(s){ for(var i=0;i<s.options.length;i++){ if(s.options[i].value.toLowerCase().indexOf(t.toLowerCase()) === 0){ s.selectedIndex = i; } } } }
      var src = f.querySelector('[name="source"]'); if(src) src.value = location.search.replace(/^\?/,'') || 'direct';
    }catch(e){}
    f.addEventListener('submit', function(e){
      e.preventDefault();
      msg.className = 'form-msg'; msg.textContent = '';
      if(f.querySelector('[name="_gotcha"]').value){ return; }
      var btn = f.querySelector('button[type="submit"]'); btn.disabled = true; btn.textContent = 'Sending...';
      fetch(f.action, {method:'POST', body:new FormData(f), headers:{'Accept':'application/json'}})
        .then(function(r){ return r.ok ? r.json() : Promise.reject(r); })
        .then(function(){ f.reset(); msg.className = 'form-msg ok'; msg.textContent = 'Thank you. Your message is with us and we will reply within one working day.'; })
        .catch(function(){ msg.className = 'form-msg err'; msg.textContent = 'Sorry, that did not send. Please email office@live2helprecruitment.co.uk or call 01902 945444.'; })
        .then(function(){ btn.disabled = false; btn.textContent = 'Send message'; });
    });
  }
})();
