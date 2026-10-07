---
layout: about
title: Home
permalink: /
nav: true
nav_order: 0.3

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # TEMPORANEO: news spente in home. Per riattivarle: true (e togli 'news' da 'off' in admin/admin.js + class="off" in admin/index.html)
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
seo_title: "Lavori su fune a Roma e Lazio | Italfuni"
seo_description: "Lavori edili su fune senza ponteggi: pulizia vetri e grondaie, tinteggiature, impermeabilizzazioni, canne fumarie e molto altro. Preventivo gratuito senza impegno, risparmio fino al 40%."
---

<style>
.post-header{display:none}
.rete-box{position:relative;overflow:visible;isolation:isolate;text-align:center;width:100%;max-width:none;margin:0;padding:3rem 0}
.rete-box canvas{position:absolute;inset:0;width:100%;height:100%;z-index:-1;display:block;pointer-events:none}
.rete-box > *{position:relative}
.rete-box h2{margin-top:0}
/* ===== HERO FOTO (Italfuni): foto in dissolvenza lenta DIETRO il testo della home =====
   COME FUNZIONA: .hero-bg riempie il box (position:absolute, z-index:0); dentro ci sono le <img class="hero-slide"> sovrapposte e un velo scuro (.hero-vel) che tiene il testo leggibile.
   Ogni foto resta N secondi, poi sfuma sulla successiva (crossfade) con un lento zoom (Ken Burns). SOLO CSS, nessuna libreria (PageSpeed).
   LE FOTO E I SECONDI SI GESTISCONO DA ADMIN > Sito > Tema > 'Foto della home': salvano _data/hero.yml (chiavi 'secondi' e 'foto').
   Il numero di foto e' libero: il blocco <style> generato da Liquid sotto (prima del box) calcola da solo durata del ciclo, ritardi e percentuali dei keyframes.
   Se _data/hero.yml non esiste o la lista e' vuota si usano le 5 foto di partenza scritte nel blocco Liquid. Per togliere tutto: cancella questo CSS, il blocco Liquid e il div .hero-bg. */
.rete-box{overflow:hidden;border-radius:16px;color:#fff;padding:4.5rem 1.5rem;min-height:clamp(430px,62vh,620px);display:flex;flex-direction:column;justify-content:center;align-items:center;background:#0d1b2a}
/* z-index 1 + position relative: il testo sta SOPRA .hero-bg (z-index 0). Senza, le foto coprirebbero il testo. max-width tiene la riga di testo stretta (il box la centra col flex). */
.rete-box > *:not(.hero-bg){position:relative;z-index:1;max-width:760px}
.rete-box h2{color:#fff}
.rete-box strong{color:#fff}
.hero-bg{position:absolute;inset:0;z-index:0;overflow:hidden}
/* opacity 0 di base + animation fill backwards: prima del proprio turno la foto e' invisibile (il ritardo e' inline sull'img). will-change = animazione sulla GPU. width/height 100% + object-fit cover riempiono il box qualunque sia il formato della foto. */
.hero-slide{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1);will-change:opacity,transform;animation:hero-fade 30s linear infinite backwards}
@media (prefers-reduced-motion:reduce){.hero-slide{animation-name:hero-fade-soft}}
@media (max-width:600px){.rete-box{padding:3rem 1rem;border-radius:12px}}
/* TESTO EVIDENZIATO al posto del velo scuro: ogni riga di testo ha il suo fondo blu notte semi-opaco (stile evidenziatore), cosi' si legge su qualunque foto
   e le foto restano luminose. box-decoration-break:clone ripete angoli e margini a ogni riga. Il colore e' un rgba: cambia l'ultimo numero (.82) per piu'/meno copertura.
   PUNTI CRITICI: (a) line-height sta nel MARK e NON sul contenitore: un'interlinea larga sul contenitore (2.05, provata e tolta) faceva crescere tutto il box. (b) il padding verticale del mark e'
   minuscolo (.08em): su un elemento inline non sposta le righe ma ingrossa la striscia, se lo alzi le strisce si toccano. (c) padding e min-height di .rete-box sono quelli originali: l'altezza della home
   non deve cambiare. (d) il velo scuro .hero-vel e' stato tolto: non rimetterlo. */
.rete-box mark.hero-hl{background:rgba(10,22,38,.82);color:#fff;padding:.08em .55em;border-radius:7px;line-height:1.7;box-decoration-break:clone;-webkit-box-decoration-break:clone;text-shadow:none}
.rete-box h2 mark.hero-hl{padding:.05em .5em;line-height:1.5}
/* ===== HERO FOTO END ===== */
/* ===== MARTE START (css) - INTERRUTTORE: home_marte in _config.yml (admin > Impostazioni, CLAUDE.md punto 27). HTML e JS sono dentro una condizione Liquid su site.home_marte: tieni START/END e i relativi if/endif in coppia, altrimenti la home si rompe senza errori. Per rimuovere Marte del tutto: cancella da qui a MARTE END (css), il blocco MARTE nell'HTML, lo script MARTE (js) e assets/img/marte.webp ===== */
.rete-box .marte-orbita{position:absolute;z-index:-2;pointer-events:none;left:50%;top:50%;width:0;height:0;will-change:transform}
.rete-box .marte-orbita .marte-y{position:absolute;left:0;top:0;width:0;height:0;will-change:transform}
.rete-box .marte{position:absolute;--mt:clamp(72px,10vw,104px);width:var(--mt);height:var(--mt);
  left:calc(var(--mt) / -2);top:calc(var(--mt) / -2);border-radius:50%;display:block;
  opacity:.6;filter:saturate(.85);box-shadow:0 0 34px 10px rgba(150,150,158,.10)}
html[data-theme=dark] .rete-box .marte{opacity:.66;box-shadow:0 0 34px 10px rgba(150,150,160,.07)}
@media (max-width:600px){.rete-box .marte{--mt:17vw}}
/* ===== MARTE END (css) ===== */

/* ===== SERVIZI HOME (nuova sezione, sotto il box costellazione) =====
   Semplice griglia di 6 card che riprendono i PRIMI 6 servizi di _pages/servizi.md,
   con link "Vedi tutti i servizi" verso /servizi/. Nessun altro blocco esistente toccato.
   Per aggiungere/rimuovere una card: duplica/elimina un .srv-home-card qui sotto e nell'HTML. */
.srv-home{margin:2.5rem 0}
.srv-home h2{text-align:center;margin-bottom:1.4rem}
.srv-home-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;max-width:900px;margin:0 auto}
.srv-home-card{display:block;color:inherit;text-decoration:none;padding:16px 18px;border:1px solid rgba(0,0,0,.12);border-radius:12px;background:#fffdf5;text-align:left}
.srv-home-card b{display:block;margin-bottom:4px}
.srv-home-card small{opacity:.65;display:block}
html[data-theme="dark"] .srv-home-card{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.15)}
.srv-home-more{text-align:center;margin-top:1.6rem}
.srv-home-more a{display:inline-block;padding:.55rem 1.4rem;border-radius:999px;border:1px solid rgba(0,0,0,.2);text-decoration:none;font-weight:600}
html[data-theme="dark"] .srv-home-more a{border-color:rgba(255,255,255,.3)}
@media (max-width:700px){.srv-home-grid{grid-template-columns:1fr}}

/* ===== PROGETTI HOME (sotto i servizi) =====
   Stesso aspetto della griglia servizi, classi separate (prj-home*) di proposito: gli script che riallineano le card
   dei servizi (pubblica_servizi.py) lavorano su .srv-home-card e non devono mai toccare queste.
   Le card NON sono scritte a mano: le genera il ciclo Liquid nell'HTML qui sotto dai file di _projects/. */
.prj-home{margin:2.5rem 0}
.prj-home h2{text-align:center;margin-bottom:1.4rem}
.prj-home-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;max-width:900px;margin:0 auto}
.prj-home-card{display:block;color:inherit;text-decoration:none;padding:16px 18px;border:1px solid rgba(0,0,0,.12);border-radius:12px;background:#fffdf5;text-align:left}
.prj-home-card b{display:block;margin-bottom:4px}
.prj-home-card small{opacity:.65;display:block}
html[data-theme="dark"] .prj-home-card{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.15)}
.prj-home-more{text-align:center;margin-top:1.6rem}
.prj-home-more a{display:inline-block;padding:.55rem 1.4rem;border-radius:999px;border:1px solid rgba(0,0,0,.2);text-decoration:none;font-weight:600}
html[data-theme="dark"] .prj-home-more a{border-color:rgba(255,255,255,.3)}
@media (max-width:700px){.prj-home-grid{grid-template-columns:1fr}}
</style>

{%- comment -%}
  HERO FOTO (Italfuni) - BLOCCO LIQUID. PUNTI CRITICI
  1) FONTE: _data/hero.yml (admin > Sito > Tema > Foto della home). Chiavi: secondi e foto (lista di percorsi COMPLETI, es. assets/img/nome.jpg).
     Se il file manca o la lista e' vuota si usa il ripiego: le 5 foto di partenza scritte qui sotto. Il controllo "unless hf.size > 0" regge anche quando hf non esiste (nil).
  2) SECONDI: forzato fra 3 e 20. "plus: 0" lo rende numero anche se nel file e' testo; at_least/at_most fanno da limite. Un valore sballato nel file non rompe la home.
  3) DURATA CICLO hd = numero foto x secondi. Le percentuali dei keyframes (hp1 = fine dissolvenza in entrata, hp2 = fine permanenza, hp3 = fine dissolvenza in uscita) si
     calcolano QUI perche' il CSS non puo' ricavarle dal numero di foto. Devono essere DECIMALI: si moltiplica per 100.0 PRIMA di divided_by, altrimenti Liquid divide fra
     interi e arrotonda (il 4% diventerebbe 0 e la dissolvenza sparirebbe).
  4) RITARDI: ogni foto parte con animation-delay = posizione x secondi, scritto inline sull'img. Niente regole nth-child: cosi' il numero di foto e' libero (il tetto di 10 lo
     mette l'admin, non il CSS).
  5) UNA SOLA FOTO: animation none e resta ferma (con il ciclo normale sparirebbe e riapparirebbe).
  6) hog = punti di partenza dello zoom (transform-origin): si ripetono ogni 5 foto, servono solo a variare il movimento.
  7) NON scrivere graffe con percentuale dentro un commento Liquid: il commento si chiuderebbe a meta' e la home si rompe senza errori.
{%- endcomment -%}
{%- assign hf = site.data.hero.foto -%}
{%- unless hf.size > 0 -%}{%- assign hf = "assets/img/italfuni/pulizia-vetri-su-fune-1200x630.jpg|assets/img/italfuni/window-cleaner-4593185_1280-1030x686.jpg|assets/img/italfuni/bogota-4490438_1280-1-1030x685.jpg|assets/img/italfuni/rope-access-window-cleaning.jpg|assets/img/italfuni/operai-balconi.jpg" | split: "|" -%}{%- endunless -%}
{%- assign hs = site.data.hero.secondi | default: 6 | plus: 0 | at_least: 3 | at_most: 20 -%}
{%- assign hn = hf.size -%}
{%- assign hd = hn | times: hs -%}
{%- assign hfd = hs | times: 0.2 -%}
{%- assign hp1 = hfd | times: 100.0 | divided_by: hd -%}
{%- assign hp2 = hs | times: 100.0 | divided_by: hd -%}
{%- assign hp3 = hs | plus: hfd | times: 100.0 | divided_by: hd -%}
{%- assign hog = "30% 40%|70% 35%|50% 60%|25% 55%|65% 50%" | split: "|" -%}
<style>
.hero-slide{animation-duration:{{ hd }}s}
@keyframes hero-fade{0%{opacity:0;transform:scale(1)}{{ hp1 }}%{opacity:1}{{ hp2 }}%{opacity:1}{{ hp3 }}%{opacity:0;transform:scale(1.1)}100%{opacity:0;transform:scale(1.1)}}
@keyframes hero-fade-soft{0%{opacity:0}{{ hp1 }}%{opacity:1}{{ hp2 }}%{opacity:1}{{ hp3 }}%{opacity:0}100%{opacity:0}}
{%- if hn == 1 %}
.hero-slide{animation:none;opacity:1}
{%- endif %}
</style>
<div class="rete-box" id="rete-box" markdown="1">
<!-- ===== MARTE START (html) - interruttore: home_marte in _config.yml (admin > Impostazioni). Se false non esce ne' l'HTML ne' lo script ===== -->
<!-- Marte tolto da questa home (Italfuni usa le foto in dissolvenza qui sotto). Per rimetterlo: ripristina la riga con if site.home_marte != false e il div .marte-orbita > .marte-y > canvas.marte (vedi MARTE START/END css e js) -->
<!-- ===== MARTE END (html) ===== -->
{% comment %}
  PUNTO CRITICO: il ciclo delle foto sta su UNA SOLA RIGA. Il box e' markdown="1": una riga vuota dentro l'HTML fa chiudere il blocco a kramdown e le foto uscirebbero come testo.
  Le img sono decorative (alt vuoto + aria-hidden sul contenitore). La prima ha fetchpriority high (e' quella che si vede subito), le altre lazy. Niente width/height: l'img e'
  assoluta e riempie il box con object-fit cover, quindi non genera spostamenti di layout. Il velo scuro NON c'e' piu' (tolto di proposito: faceva sembrare le foto di notte).
{% endcomment %}
<div class="hero-bg" aria-hidden="true">{% for ph in hf %}{% assign hk = forloop.index0 | modulo: 5 %}<img class="hero-slide" src="{{ ph | prepend: '/' | replace: '//', '/' | relative_url }}" alt="" {% if forloop.first %}fetchpriority="high"{% else %}loading="lazy"{% endif %} decoding="async" style="animation-delay:{{ forloop.index0 | times: hs }}s;transform-origin:{{ hog[hk] }}">{% endfor %}</div>

{% comment %}
  TESTO EVIDENZIATO - PUNTI CRITICI
  1) Titolo e paragrafi sono avvolti in mark class hero-hl (fondo blu notte riga per riga, stile evidenziatore). Se modifichi o aggiungi un paragrafo avvolgilo anche tu:
     senza mark il testo resta bianco SENZA fondo e sulle foto chiare non si legge.
  2) Il titolo e' "## <mark>...</mark>": il mark sta DENTRO l'h2 (resta un vero titolo, conta per la SEO). Non invertire.
  3) Il grassetto dentro il mark e' scritto col tag strong, NON con gli asterischi: dentro HTML inline kramdown non garantisce di interpretarli e si vedrebbero i ** a schermo.
  4) Una riga vuota fra un paragrafo e l'altro, come ora.
{% endcomment %}

## <mark class="hero-hl">Lavori in quota su fune, senza ponteggi e con costi più bassi.</mark>

<mark class="hero-hl">Italfuni esegue lavori edili e di manutenzione su fune: pulizia vetri e grondaie, tinteggiature, impermeabilizzazioni, ristrutturazioni di balconi, facciate e tetti, canne fumarie e rimozione di materiale pericolante. Le tecniche derivano da speleologia e alpinismo e permettono di raggiungere punti altrimenti inaccessibili.</mark>

<mark class="hero-hl">Evitare ponteggi, piattaforme aeree e permessi comunali rende l'intervento più rapido e fa risparmiare fino al 40%. Sopralluogo e preventivo sono gratuiti e senza impegno.</mark>

<mark class="hero-hl"><strong>Hai bisogno di un intervento in quota?</strong> Richiedi un preventivo gratuito: ti rispondiamo con una soluzione su misura.</mark>

</div>

<!-- ===== FN HOME START (1): perche' su fune + preventivo ===== -->
<style>
/* ===== FN HOME (testi dal sito originale italfuni.it: perche' su fune, preventivo, perche' noi, lavora con noi) ===== */
.fn-sec{max-width:900px;margin:2.5rem auto;padding:0 8px}
.fn-sec h2{text-align:center;margin-bottom:1rem}
.fn-sec > p{text-align:center;max-width:720px;margin:0 auto 1rem}
.fn-list{max-width:760px;margin:0 auto;padding-left:1.2rem;line-height:1.6}
.fn-list li{margin-bottom:.45rem}
.fn-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:1.2rem}
.fn-card{padding:16px 18px;border:1px solid rgba(0,0,0,.12);border-radius:12px;background:#fffdf5;text-align:left}
.fn-card b{display:block;margin-bottom:4px}
.fn-card p{margin:0;opacity:.85}
html[data-theme="dark"] .fn-card{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.15)}
.fn-nota{font-size:.85rem;opacity:.65;text-align:center;margin-top:.6rem}
@media (max-width:700px){.fn-grid{grid-template-columns:1fr}}
/* PERCHE' SU FUNE: 9 vantaggi in card bianche (cornice sottile, angoli molto arrotondati, ombra morbida), 3 colonne (2 sotto 900px, 1 sotto 600px).
   Layout in RIGA: testo a sinistra, icona SVG a DESTRA (card bassa, non piu' icona sopra). Le card di una riga hanno la STESSA altezza (grid stretch) e il testo e'
   centrato in verticale, con font un po' piu' piccolo e text-wrap:pretty per equilibrare righe corte e lunghe. Nessuna linea colorata all'hover: solo un leggero sollevamento.
   Icone (ordine dei 9 punti): fulmine, divieto, documento barrato, cartella spuntata, percentuale, calendario, frecce di ripetizione, scudo, orologio. Per cambiarne una: sostituisci il suo <svg>.
   Testo scuro FISSO anche in tema scuro, perche' la card resta bianca. color-mix ha un ripiego (la riga prima) per i browser vecchi. */
.fn-sec.fn-wide{max-width:1040px}
.fn-van-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:1.6rem;align-items:stretch}
.fn-van{display:flex;flex-direction:row;align-items:center;justify-content:space-between;gap:14px;padding:18px 18px 18px 22px;min-height:112px;background:#fff;color:#1f2933;border:1px solid #e6e8ec;border-radius:22px;box-shadow:0 1px 2px rgba(16,24,40,.04),0 8px 24px -12px rgba(16,24,40,.12);transition:transform .25s ease,box-shadow .25s ease}
.fn-van:hover{transform:translateY(-3px);box-shadow:0 2px 4px rgba(16,24,40,.05),0 16px 32px -14px rgba(16,24,40,.2)}
.fn-van-i{order:2;flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:14px;color:var(--global-theme-color,#b509ac);background:rgba(181,9,172,.09);background:color-mix(in srgb,var(--global-theme-color,#b509ac) 11%,#fff)}
.fn-van-i svg{width:23px;height:23px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.fn-van p{order:1;flex:1 1 auto;margin:0;font-size:.94rem;line-height:1.5;text-align:left;color:#3a4552;text-wrap:pretty}
.fn-van strong{color:#111827}
@media (max-width:900px){.fn-van-grid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:600px){.fn-van-grid{grid-template-columns:1fr}.fn-van{min-height:0}}
@media (prefers-reduced-motion:reduce){.fn-van{transition:none}.fn-van:hover{transform:none}}
</style>

<div class="fn-sec fn-wide">
  <h2>Perché intervenire su fune?</h2>
  <p>Al giorno d'oggi molte persone scelgono questo nuovo approccio di fare edilizia. Scopriamo insieme i motivi:</p>
  {% comment %}
    VANTAGGI SU FUNE - PUNTI CRITICI
    1) 9 card = i 9 punti del sito originale, testo identico. 2) Nel DOM l'icona (span fn-van-i) viene PRIMA del testo: e' il CSS a metterla a DESTRA con order:2. Per portarla a sinistra
       togli order:2 da .fn-van-i. 3) Le icone sono svg inline con stroke currentColor e senza fill: il colore lo da' il CSS (.fn-van-i). Sono decorative (aria-hidden). 4) Altezza uguale
       per riga = grid con align stretch + min-height: NON mettere height fissa, i testi lunghi (punti 6 e 9) sfonderebbero la card. 5) Fondo bianco e testo scuro sono FISSI e non seguono il
       tema scuro: voluto, e' una card bianca. 6) Per aggiungere un punto copia una card intera: se il totale non e' multiplo di 3 l'ultima riga resta corta.
  {% endcomment %}
  <div class="fn-van-grid">
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></svg></span><p>Risoluzione immediata di piccoli problemi strutturali ed estetici in posti inaccessibili.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/></svg></span><p>Non serve l'installazione o l'affitto di ponteggi o installazioni aeree.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="m9.5 12.5 5 5"/><path d="m14.5 12.5-5 5"/></svg></span><p>Non servono permessi*.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/></svg></span><p>Burocrazia ridotta.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m19 5-14 14"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg></span><p>Abbattimento dei prezzi <strong>fino al 40%</strong>.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></span><p>Possibilità di frazionare gli interventi in base alla necessità del cliente: senza impalcature si dà priorità agli interventi più urgenti, rateizzando i costi.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg></span><p>Interventi di manutenzione programmata con la formula <strong>ZERO PENSIERI</strong>.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg></span><p>Eliminazione del rischio intrusione agevolato dall'installazione dei classici ponteggi.</p></div>
    <div class="fn-van"><span class="fn-van-i"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><p>Operatori altamente qualificati che possono intervenire in meno di un'ora in ogni punto del palazzo o di grandi strutture, risolvendo tempestivamente il problema.</p></div>
  </div>
</div>

<div class="fn-sec">
  <h2>Come fare un preventivo?</h2>
  <p>Per un preventivo gratuito e senza impegno, con sopralluogo gratuito, basta fare click su <a href="{{ '/contatti/' | relative_url }}">contatti</a> in alto e compilare il modulo: verrai ricontattato entro 24 ore (giorni lavorativi).</p>
  <p>Sai utilizzare WhatsApp? Possiamo fare un preventivo approssimativo immediato e gratuito, senza sopralluogo: descrivi dettagliatamente il tipo di intervento da fare nel messaggio.</p>
  <p class="fn-nota"><b>Attenzione:</b> operiamo nel territorio laziale e nei paesi vicini.</p>
</div>
<!-- ===== FN HOME END (1) ===== -->

<!-- ===== SERVIZI HOME START (DINAMICO) =====
     Le card NON sono scritte a mano: il ciclo Liquid prende i documenti della collection 'servizi' con 'in_home: true' (casetta nell'admin, sezione Servizi).
     Campo SEPARATO dalla stella del blog ('featured'): non si mescolano. Ordine alfabetico per titolo (i post hanno la stessa data, per data l'ordine non sarebbe stabile).
     Titolo, descrizione (tagliata a 8 parole) e link vengono dal post. Se nessun servizio ha la casetta la sezione sparisce. NON rimettere card a mano. ===== -->
{%- assign srv_home = site.servizi | where: 'in_home', 'true' | sort: 'title' -%}
{%- if srv_home.size > 0 %}
<div class="srv-home">
  <h2>I nostri servizi</h2>
  <div class="srv-home-grid">
    {%- for p in srv_home -%}
    <a class="srv-home-card" href="{{ p.url | relative_url }}"><b>{{ p.title | escape }}</b>{% if p.description != blank %}<small>{{ p.description | truncatewords: 8 | escape }}</small>{% endif %}</a>
    {%- endfor %}
  </div>
  <div class="srv-home-more">
    <a href="{{ '/servizi/' | relative_url }}">Vedi tutti i servizi</a>
  </div>
</div>
{%- endif %}
<!-- ===== SERVIZI HOME END ===== -->

<!-- ===== PROGETTI HOME START =====
     DINAMICO: prende da solo i primi 6 progetti di _projects/ (nessuna card scritta a mano).
     Ordine = campo 'importance' del progetto (1 = per primo), come nella pagina /projects/; chi non ha 'importance' va in fondo.
     Link: se il progetto ha 'redirect:' (sito esterno) punta li', altrimenti alla sua pagina.
     Un progetto nuovo/modificato/eliminato si riflette qui al prossimo deploy, senza toccare questo file.
     Casetta nell'admin (lista Progetti, campo 'in_home: true'): se almeno un progetto ce l'ha, in home vanno SOLO quelli marcati (tutti); se nessuno e' marcato, ripiego sui primi 6 per importance. Se non ci sono progetti la sezione sparisce. ===== -->
{%- assign prj_home = site.projects | where: 'in_home', 'true' | sort: 'importance', 'last' -%}
{%- assign prj_limit = prj_home.size -%}
{%- if prj_home.size == 0 -%}{%- assign prj_home = site.projects | sort: 'importance', 'last' -%}{%- assign prj_limit = 6 -%}{%- endif -%}
{%- if prj_home.size > 0 %}
<div class="prj-home">
  <h2>I nostri progetti</h2>
  <div class="prj-home-grid">
    {%- for p in prj_home limit: prj_limit -%}
      {%- assign p_ext = false -%}
      {%- if p.redirect contains '://' -%}{%- assign p_ext = true -%}{%- endif -%}
    <a class="prj-home-card" href="{% if p_ext %}{{ p.redirect }}{% else %}{{ p.url | relative_url }}{% endif %}"{% if p_ext %} target="_blank" rel="noopener"{% endif %}><b>{{ p.title | escape }}</b>{% if p.description != blank %}<small>{{ p.description | escape }}</small>{% endif %}</a>
    {%- endfor %}
  </div>
  <div class="prj-home-more">
    <a href="{{ '/projects/' | relative_url }}">Vedi tutti i progetti</a>
  </div>
</div>
{%- endif %}
<!-- ===== PROGETTI HOME END ===== -->

<!-- ===== FN HOME START (2): perche' noi + lavora con noi ===== -->
<div class="fn-sec">
  <h2>Perché noi?</h2>
  <div class="fn-grid">
    <div class="fn-card"><b>Totale sicurezza</b><p>Ogni membro del nostro team esegue corsi e aggiornamenti da istruttori di alpinismo e speleologia.</p></div>
    <div class="fn-card"><b>Tutto è accessibile</b><p>Raggiungere e operare in punti inaccessibili è il nostro pane quotidiano: per noi non esiste un punto dell'edificio o una piattaforma aerea inaccessibile.</p></div>
    <div class="fn-card"><b>Prezzi competitivi</b><p>Questa innovazione edilizia con radici alpinistiche permette di abbattere il prezzo. Non serve installare piattaforme o ponteggi, né affittare costosi macchinari.</p></div>
    <div class="fn-card"><b>Tempistiche</b><p>Non serve installare nessun ponteggio o piattaforma: ci basta un punto solido dove ancorarci e operare il giorno stesso.</p></div>
    <div class="fn-card"><b>Zero ponteggi</b><p>Scordati l'installazione di piattaforme o ponteggi. I nostri operatori sono in grado di iniziare a lavorare dopo meno di un'ora.</p></div>
  </div>
</div>

<div class="fn-sec">
  <h2>Lavora con noi</h2>
  <p>Ti senti predisposto per questo tipo di lavoro? Inviaci la candidatura nell'area <a href="{{ '/contatti/' | relative_url }}">contatti</a>.</p>
  <p class="fn-nota"><b>Italfuni</b> - Monterotondo, Roma (RM) - Tel. <a href="tel:+393281970254">(328) 1970254</a><br>Orari ufficio: Lun-Ven 8:00-19:00, Sab 8:00-14:00, Dom chiuso.</p>
</div>
<!-- ===== FN HOME END (2) ===== -->


{%- if site.home_marte != false %}
<script>
/* ===== MARTE START (js) =====
   COME FUNZIONA (3 pezzi indipendenti):
   1. MOTO nel box: due animazioni CSS (Web Animations API) su assi diversi, con periodi diversi (PX/PY),
      cosi' il percorso non si ripete mai uguale. Solo transform -> leggero, niente reflow.
   2. ROTAZIONE: Marte e' un <canvas> disegnato a mano pixel per pixel. Non e' una foto che scorre:
      ogni pixel del disco viene mappato su una sfera 3D e colorato dalla mappa piatta di Marte (marte.webp).
   3. PERSISTENZA: un solo timestamp (t0) in localStorage. Posizione e rotazione derivano da (adesso - t0),
      quindi dopo un refresh riprendono da dove erano, senza salvare nient'altro.
   Per togliere Marte: vedi le istruzioni nel blocco CSS. */
(function(){
  var o=document.querySelector('.marte-orbita'); if(!o) return;
  var y=o.querySelector('.marte-y'), cv=o.querySelector('.marte'); if(!y||!cv) return;
  var ridotto=false /* ignorato di proposito: animazione lenta e minima, deve partire sempre (era matchMedia prefers-reduced-motion) */;
  /* PARAMETRI DA RITOCCARE (in millisecondi):
     PX = periodo del moto orizzontale (andata+ritorno = 2*PX)   PY = idem verticale (diverso da PX di proposito)
     GIRO = tempo di un giro completo di Marte su se stesso (45000 = 45 s; piu' basso = piu' veloce)
     K = chiave localStorage. ATTENZIONE: piu' sotto, dentro img.onload, c'e' un'altra variabile PX
     (array della sfera) che nel suo scope nasconde questa: e' voluto e funziona, ma non usare PX/PY
     del periodo dentro onload. */
  var PX=173000, PY=131000, GIRO=45000, K='marte_t0';
  /* t0 = istante in cui e' iniziata l'"orbita". Se manca (prima visita) lo creo ora. Il try/catch serve
     perche' in navigazione privata o con storage bloccato setItem lancia errore: in quel caso Marte
     funziona lo stesso, semplicemente riparte da zero a ogni refresh. */
  var t0=parseInt(localStorage.getItem(K),10); if(!t0||isNaN(t0)){ t0=Date.now(); try{localStorage.setItem(K,t0);}catch(e){} }
  /* ampiezza dello spostamento orizzontale in vw: ridotta su telefono per non uscire dal box */
  function amp(){ return matchMedia('(max-width:600px)').matches?26:36; }
  function moto(){
    /* prefers-reduced-motion: chi ha "riduci movimento" attivo nel sistema vede Marte fermo */
    if(ridotto) return; var el=Date.now()-t0, ax=amp()+'vw';
    /* cancello le animazioni precedenti: senza questo, dopo un resize se ne accumulerebbero di sovrapposte */
    /* Sfasamento: currentTime = tempo trascorso modulo l'intero ciclo andata+ritorno (2*periodo).
       E' il trucco che fa riprendere la posizione dopo il refresh. */
    o.getAnimations().concat(y.getAnimations()).forEach(function(a){a.cancel();});
    o.animate([{transform:'translateX(-'+ax+')'},{transform:'translateX('+ax+')'}],{duration:PX,iterations:Infinity,direction:'alternate',easing:'ease-in-out'}).currentTime=el%(PX*2);
    y.animate([{transform:'translateY(-110px)'},{transform:'translateY(110px)'}],{duration:PY,iterations:Infinity,direction:'alternate',easing:'ease-in-out'}).currentTime=el%(PY*2);
  }
  /* al resize riparto dopo 300 ms di quiete (debounce) per non ricalcolare a ogni pixel trascinato */
  moto(); var to; addEventListener('resize',function(){clearTimeout(to);to=setTimeout(moto,300);});
  /* S = raggio in pixel del canvas: il disegno e' a 208x208 (2*S) ed e' ridimensionato via CSS, cosi' resta nitido
     sugli schermi ad alta densita'. Aumentarlo migliora la qualita' ma il costo cresce col quadrato. */
  var S=104, img=new Image(); cv.width=S*2; cv.height=S*2;
  /* Tutto il resto parte solo a immagine caricata. Leggo i pixel della mappa UNA volta in un canvas
     di appoggio (getImageData): rileggerli a ogni frame sarebbe lentissimo. */
  img.onload=function(){
    var tc=document.createElement('canvas'); tc.width=img.width; tc.height=img.height; var tx=tc.getContext('2d'); tx.drawImage(img,0,0);
    var T=tx.getImageData(0,0,tc.width,tc.height).data, TW=tc.width, TH=tc.height;
    var g=cv.getContext('2d'), N=S*2, out=g.createImageData(N,N), D=out.data;
    /* sfera vera: per ogni pixel del disco calcolo il punto 3D, lo riporto nel sistema del pianeta
       (asse polare inclinato di TILT) e da li ricavo longitudine/latitudine sulla mappa. */
    /* TILT: inclinazione dell'asse polare (Marte reale ~25). 0 = poli esattamente in alto/in basso.
       cT/sT = coseno e seno precalcolati, perche' servono per ogni pixel. */
    var TILT=25*Math.PI/180, cT=Math.cos(TILT), sT=Math.sin(TILT);
    /* direzione della luce (vettore normalizzato): da alto-sinistra e leggermente frontale.
       Il lato in ombra non e' mai nero (vedi fattore k in frame): il pianeta resta leggibile. */
    var LX=-.55, LY=.45, LZ=.70, LL=Math.sqrt(LX*LX+LY*LY+LZ*LZ); LX/=LL; LY/=LL; LZ/=LL;   /* luce da alto-sinistra */
    /* PRECALCOLO (una volta sola): per ogni pixel del disco salvo il punto 3D ruotato (PX,PY,PZ) e la luce (SH).
       SH=-1 segna i pixel fuori dal cerchio (trasparenti). Cosi' frame() non rifa' la geometria a ogni giro. */
    var PX=new Float32Array(N*N), PY=new Float32Array(N*N), PZ=new Float32Array(N*N), SH=new Float32Array(N*N);
    for(var yy=0;yy<N;yy++)for(var xx=0;xx<N;xx++){
      var nx=(xx+.5-S)/S, ny=(S-yy-.5)/S, r2=nx*nx+ny*ny, i=yy*N+xx;
      if(r2>1){SH[i]=-1;continue;}
      /* nz = profondita' del punto sulla sfera (equazione della sfera: x^2+y^2+z^2=1) */
      var nz=Math.sqrt(1-r2);
      /* rotazione inversa attorno all'asse X = inclinazione dell'asse polare rispetto alla verticale dello schermo */
      PX[i]=nx; PY[i]=ny*cT+nz*sT; PZ[i]=-ny*sT+nz*cT;
      var d=nx*LX+ny*LY+nz*LZ; SH[i]=Math.max(0,d);
    }
    /* frame(ph): disegna un fotogramma. ph = fase di rotazione in radianti (0..2*PI).
       QUESTO e' il punto piu' critico per le prestazioni: gira ogni ~50 ms su ~34.000 pixel.
       Regole se lo modifichi: niente allocazioni qui dentro, niente Math.* inutili, tutto il resto va nel precalcolo. */
    function frame(ph){
      for(var i=0;i<N*N;i++){ var q=i*4;
        if(SH[i]<0){D[q+3]=0;continue;}
        /* longitudine = angolo attorno all'asse polare. Aggiungere ph e' l'UNICA cosa che fa ruotare il pianeta.
           latitudine = quanto in alto/basso; il clamp evita NaN per errori di arrotondamento oltre +-1. */
        var lon=Math.atan2(PX[i],PZ[i])+ph, lat=Math.asin(Math.max(-1,Math.min(1,PY[i])));
        /* u = coordinata orizzontale nella mappa (0..1), avvolta in modo che la mappa chiuda il ciclo senza cucitura */
        var u=lon/6.283185307; u-=Math.floor(u);
        var v=(.5-lat/Math.PI)*(TH-1);
        /* interpolazione bilineare: media pesata dei 4 pixel della mappa attorno al punto. Senza, il pianeta
           apparirebbe a scatti/pixelato mentre ruota. x1=(x0+1)%TW fa "girare" il bordo destro sul sinistro. */
        var xf=u*(TW-1), x0=xf|0, x1=(x0+1)%TW, fx=xf-x0, y0=v|0, y1=Math.min(TH-1,y0+1), fy=v-y0;
        var a=(y0*TW+x0)*4, b=(y0*TW+x1)*4, c=(y1*TW+x0)*4, e=(y1*TW+x1)*4;
        /* luminosita': minimo 30% (lato in ombra ancora visibile) fino a 100%; l'esponente .75 ammorbidisce il passaggio */
        var k=.30+.70*Math.pow(SH[i],.75);
        for(var ch=0;ch<3;ch++){
          var top=T[a+ch]*(1-fx)+T[b+ch]*fx, bot=T[c+ch]*(1-fx)+T[e+ch]*fx;
          D[q+ch]=(top*(1-fy)+bot*fy)*k;
        }
        D[q+3]=255; }
      g.putImageData(out,0,0);
    }
    /* ANIMAZIONE: requestAnimationFrame, ma ridisegno solo ogni 50 ms (~20 fps): per una rotazione lenta
       basta e dimezza il consumo di CPU/batteria. `last` = istante dell'ultimo disegno. */
    var last=0;
    (function tick(now){
      /* la fase dipende dal TEMPO REALE (Date.now()-t0), non da un contatore: e' cosi' che dopo un refresh o un
         tab in background Marte e' dove deve essere, senza scatti ne' salti */
      var ph=((Date.now()-t0)%GIRO)/GIRO*6.283185307;   /* fase legata al tempo: dopo il refresh riprende da dove era */
      /* con riduci-movimento disegno un solo fotogramma fisso (il ramo else-if) e non richiedo altri frame */
      if(!ridotto&&now-last>50){ frame(ph); last=now; } else if(!last){ frame(ph); last=now; }
      if(!ridotto) requestAnimationFrame(tick);
    })(0);
  };
  img.src="{{ '/assets/img/marte.webp' | relative_url }}";
})();
/* ===== MARTE END (js) ===== */
</script>
{%- endif %}

<script>
(function(){
  var box=document.getElementById('rete-box'), cv=document.getElementById('rete-cv'); if(!box||!cv) return;
  var ctx=cv.getContext('2d'), ridotto=false /* ignorato di proposito: animazione lenta e minima, deve partire sempre (era matchMedia prefers-reduced-motion) */;
  var punti=[], w=0, h=0, mouse={x:0,y:0,on:false}, raf=null, visibile=true;
  var DIST=140, DIST_M=190;
  function colore(){
    return document.documentElement.getAttribute('data-theme')==='dark' ? '105,105,115' : '150,150,160';
  }
  function dim(){
    var dpr=Math.min(devicePixelRatio||1,2); w=box.clientWidth; h=box.clientHeight;
    cv.width=w*dpr; cv.height=h*dpr; cv.getContext('2d').setTransform(dpr,0,0,dpr,0,0);
    var n=Math.round(Math.min(100,Math.max(34,(w*h)/7500))); punti=[];
    for(var i=0;i<n;i++) punti.push({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5,r:1.3+Math.random()*1.5});
  }
  function disegna(){
    ctx.clearRect(0,0,w,h); var c=colore();
    for(var i=0;i<punti.length;i++){
      var a=punti[i];
      if(!ridotto){ a.x+=a.vx; a.y+=a.vy; if(a.x<0||a.x>w)a.vx*=-1; if(a.y<0||a.y>h)a.vy*=-1; }
      for(var j=i+1;j<punti.length;j++){
        var b=punti[j], dx=a.x-b.x, dy=a.y-b.y, d=Math.sqrt(dx*dx+dy*dy);
        if(d<DIST){ ctx.strokeStyle='rgba('+c+','+(0.55*(1-d/DIST)).toFixed(3)+')'; ctx.lineWidth=1;
          ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke(); }
      }
      if(mouse.on){ var mx=a.x-mouse.x,my=a.y-mouse.y,md=Math.sqrt(mx*mx+my*my);
        if(md<DIST_M){ ctx.strokeStyle='rgba('+c+','+(0.75*(1-md/DIST_M)).toFixed(3)+')'; ctx.lineWidth=1.1;
          ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(mouse.x,mouse.y); ctx.stroke(); } }
      ctx.fillStyle='rgba('+c+',0.7)'; ctx.beginPath(); ctx.arc(a.x,a.y,a.r,0,6.2832); ctx.fill();
    }
  }
  function ciclo(){ disegna(); raf=(visibile&&!ridotto)?requestAnimationFrame(ciclo):null; }
  function avvia(){ if(!raf) raf=requestAnimationFrame(ciclo); }
  box.addEventListener('pointermove',function(e){ if(e.pointerType==='touch')return; var r=box.getBoundingClientRect(); mouse.x=e.clientX-r.left; mouse.y=e.clientY-r.top; mouse.on=true; });
  box.addEventListener('pointerleave',function(){ mouse.on=false; });
  document.addEventListener('visibilitychange',function(){ visibile=!document.hidden; if(visibile)avvia(); });
  if('IntersectionObserver' in window) new IntersectionObserver(function(en){ visibile=en[0].isIntersecting; if(visibile)avvia(); }).observe(box);
  var t; addEventListener('resize',function(){ clearTimeout(t); t=setTimeout(function(){dim();disegna();},120); });
  dim(); disegna(); if(!ridotto) avvia();
})();
</script>
