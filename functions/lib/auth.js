const enc=new TextEncoder();
function b64(bytes){return btoa(String.fromCharCode(...new Uint8Array(bytes))).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')}
async function hmac(secret,text){const key=await crypto.subtle.importKey('raw',enc.encode(secret),{name:'HMAC',hash:'SHA-256'},false,['sign']);return b64(await crypto.subtle.sign('HMAC',key,enc.encode(text)))}
export async function passwordHash(env,password){const d=await crypto.subtle.digest('SHA-256',enc.encode(`${env.AUTH_SALT}:${password}`));return b64(d)}
export function safeEqual(a,b){a=String(a||'');b=String(b||'');if(a.length!==b.length)return false;let r=0;for(let i=0;i<a.length;i++)r|=a.charCodeAt(i)^b.charCodeAt(i);return r===0}
export async function createSession(env,user){const exp=Math.floor(Date.now()/1000)+14400;const body=`${user}.${exp}`;return `${body}.${await hmac(env.SESSION_SECRET,body)}`}
export async function authenticated(request,env){const m=(request.headers.get('cookie')||'').match(/(?:^|;\s*)sk_admin=([^;]+)/);if(!m)return false;const p=m[1].split('.');if(p.length!==3)return false;const [user,exp,sig]=p;if(+exp<Math.floor(Date.now()/1000))return false;return safeEqual(sig,await hmac(env.SESSION_SECRET,`${user}.${exp}`))}
export function cookie(token){return `sk_admin=${token}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=14400`}
export function clearCookie(){return 'sk_admin=; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=0'}