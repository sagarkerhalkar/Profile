async function loadProfile(){
  const cfg = await fetch(getBase()+'assets/profile_config.json',{cache:'no-store'}).then(r=>r.json());
  document.querySelectorAll('[data-field]').forEach(el=>{const k=el.dataset.field;if(cfg[k]) el.textContent=cfg[k];});
  document.title = (cfg.name||'Sagar Kerhalkar') + ' | ' + (cfg.headline||'Profile');
  const stats=document.getElementById('stats'); if(stats && cfg.stats){stats.innerHTML=cfg.stats.map(s=>`<div class="stat"><b>${esc(s.value)}</b><span>${esc(s.label)}</span></div>`).join('')}
  const skills=document.getElementById('skillsList'); if(skills && cfg.skills){skills.innerHTML=cfg.skills.map(s=>`<span class="chip">${esc(s)}</span>`).join('')}
  const exp=document.getElementById('experienceList'); if(exp && cfg.experience){exp.innerHTML=cfg.experience.map(e=>`<article class="timeItem"><time>${esc(e.period)}</time><div><h3>${esc(e.title)} • ${esc(e.company)}</h3><p>${esc(e.location||'')}</p><p>${esc(e.details||'')}</p></div></article>`).join('')}
  const projects=document.getElementById('projectList'); if(projects && cfg.projects){projects.innerHTML=cfg.projects.map(p=>`<article class="project"><h3>${esc(p.name)}</h3><p>${esc(p.summary)}</p><div class="chips">${(p.tags||[]).slice(0,6).map(t=>`<span class="chip">${esc(t)}</span>`).join('')}</div><p><a class="btn" href="${rel(p.url||'#')}">Open Project</a></p></article>`).join('')}
  setLinks(cfg);
}
function getBase(){const p=location.pathname; if(p.includes('/projects/systemhealthmonitor/')) return '../../'; if(p.includes('/cv/')) return '../'; return '';}
function rel(url){ if(url.startsWith('/sagarkerhalkar/systemhealthmonitor')) return getBase()+'projects/systemhealthmonitor/'; if(url.startsWith('/')) return url; return url; }
function setLinks(c){
  const phone='tel:'+String(c.phone||'').replace(/\D/g,''); const mail='mailto:'+(c.email||'');
  document.querySelectorAll('#phoneLink').forEach(a=>{a.href=phone;a.innerHTML='📞 '+esc(c.phone||'')});
  document.querySelectorAll('#emailLink').forEach(a=>{a.href=mail;a.innerHTML='✉ '+esc(c.email||'')});
  document.querySelectorAll('#linkedinLink,#linkedinLink2').forEach(a=>{a.href=c.linkedin||'#'});
  document.querySelectorAll('#githubLink,#githubLink2').forEach(a=>{a.href=c.github||'#'});
}
function esc(s){return String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]))}
document.getElementById('year')?.append(new Date().getFullYear());
document.addEventListener('click',e=>{if(e.target.closest('[data-contact]')) document.getElementById('contactDialog')?.showModal(); if(e.target.closest('[data-close]')) document.getElementById('contactDialog')?.close();});
loadProfile().catch(console.error);
