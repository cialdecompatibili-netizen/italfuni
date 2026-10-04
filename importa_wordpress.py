# Importa servizi e portfolio da un sito WordPress (Avada/Enfold) nel clone Jekyll.
# Usato il 04/10/2026 per italfuni.it. Le liste SERVIZI e PROG sono SPECIFICHE di quel sito: adattarle.
# Legge le pagine scaricate in %TEMP%\italfuni_src, scrive in %TEMP%\italfuni_out. Procedura completa: CLAUDE.md punto 34.
import pathlib, re, json, shutil, urllib.request
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md

W = pathlib.Path.home()/"AppData/Local/Temp/italfuni_src"
OUT = pathlib.Path.home()/"AppData/Local/Temp/italfuni_out"
if OUT.exists(): shutil.rmtree(OUT)
(OUT/"_servizi").mkdir(parents=True); (OUT/"_projects").mkdir(); (OUT/"assets/img/italfuni").mkdir(parents=True)

SERVIZI = [  # (slug originale, titolo dal menu, in_home, descrizione breve se nota)
 ("impermeabilizzazione-su-fune","Impermeabilizzazione su fune",True,"Impermeabilizzazioni di lastre d’ardesia, terrazzi e tetti."),
 ("manutenzione-e-installazione-canne-fumarie","Pulizia, manutenzione e installazione canne fumarie",False,"Pulizia, manutenzione e installazione di canne fumarie su fune, con prezzi più bassi fino al 40%."),
 ("manutenzione-e-sostituzione-grondaie","Riparazione e pulizia grondaie",True,"Le altezze sono il nostro pane quotidiano, eseguiamo manutenzione, riparazione e sostituzione grondaie."),
 ("installazione-e-manutenzione-dissuasori-volatili","Installazione e manutenzione dissuasori per piccioni",False,"Installazione e manutenzione di dissuasori per piccioni e volatili tramite corde e funi."),
 ("montaggio-isolanti","Montaggio isolanti",True,"Montaggio isolanti termici, acustici."),
 ("montaggio-sistemi-di-sicurezza-su-fune","Montaggio sistemi di sicurezza su fune",True,"Eseguiamo montaggi di sistemi di sicurezza in posti inaccessibili."),
 ("potatura-alberi","Potatura alberi",True,"Potatura alberi ad alto fusto."),
 ("pulizia-componenti-su-fune","Pulizia componenti su fune",False,"Pulizia di grondaie, serbatoi, camini, facciate, dighe, lampioni e molto altro, senza ponteggi."),
 ("pulizia-pannelli-fotovoltaici","Pulizia pannelli fotovoltaici",False,"Mantenere puliti i pannelli fotovoltaici significa mantenere inalterata la loro efficienza."),
 ("pulizia-vetri","Pulizia vetri",True,"Specializzati nella pulizia vetri di grattacieli e palazzi."),
 ("messa-in-sicurezza","Rimozione materiale pericolante su fune",True,"Interventi rapidi e mirati nella rimozione di parti o cose pericolanti che potrebbero compromettere la sicurezza di passanti, persone o cose."),
 ("ristrutturazioni-balconi-e-facciate","Ristrutturazioni balconi e facciate",True,"Ristrutturazione o manutenzione di balconi, facciate, casse camino e cornicioni."),
 ("tinteggiature-complete-su-fune","Tinteggiature complete",True,"Tinteggiatura esterna e manutenzione su tetti senza l’utilizzo di ponteggi e permessi comunali."),
 ("ristrutturazione-tetto","Ristrutturazione tetto",False,"Ristrutturazione di tetti con l’edilizia su fune, per abbattere il prezzo."),
]
SLUGS = {s[0] for s in SERVIZI}
TYPO = {"dissuarossori":"dissuasori","maggio senso":"maggior senso","Il motivi":"I motivi","pulici":"puliti","leder":"leader","spedilizzata":"specializzata",
        "abbatere":"abbattere","Impresa edie":"Impresa edile","manutenzone":"manutenzione","Istallazione":"Installazione","Nessun problemi":"Nessun problema",
        "sostituisci grondaie pluviali":"sostituisce grondaie e pluviali","fune per":"fune per"}
def fix(t):
    for a,b in TYPO.items(): t = t.replace(a,b)
    return t.replace("\xa0"," ")
def q(v):  # stringa YAML tra virgolette
    return '"' + v.replace("\\","\\\\").replace('"','\\"') + '"'
def scarica(url, nome):
    dest = OUT/"assets/img/italfuni"/nome
    if not dest.exists():
        req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
        dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return "assets/img/italfuni/"+nome

def corpo(slug, titolo):
    s = BeautifulSoup((W/f"p__servizi__{slug}.html").read_bytes(), "html.parser")
    e = s.select_one(".post-entry")
    for sel in ("#ez-toc-container","script","style","form","noscript",".avia-button-wrap",".avia_codeblock_section",".sharedaddy",".entry-footer"):
        for x in e.select(sel): x.decompose()
    STOCK = re.compile(r"(architect|modern-kitchen|construction-site|scale-ruler|cropped-hand|urban-development|modern-home|house-|team-banner|favicon|logo|envato|themeforest|dribbble|wordpress|microlancer|regione-lazio)", re.I)
    imgs = []; visti = set()
    for im in e.find_all("img"):
        src = im.get("src","")
        base = src.rsplit("/",1)[-1].lower() if src else ""
        if not src or STOCK.search(base) or re.search(r"-(36|80|120|180)x\d+\.", base) or base in visti:
            continue
        visti.add(base)
        pth = scarica(src, base); alt = fix((im.get("alt") or titolo).strip())
        imgs.append((pth, alt))
        tok = s.new_tag("p"); tok.string = f"@@IMG{len(imgs)-1}@@"
        im["data-tok"] = str(len(imgs)-1)
        in_slide = im.find_parent(class_=re.compile(r"^avia-slideshow$"))
        blocco = im.find_parent(["p","h1","h2","h3","h4","li","div","section"])
        if in_slide is not None:
            e.insert(0, tok)
        elif blocco is not None and blocco.name.startswith("h") and not blocco.get_text(strip=True).replace("\xa0","").strip():
            blocco.replace_with(tok)
        elif blocco is not None:
            blocco.insert_before(tok)
    for x in e.select(".avia-slideshow, .avia-slideshow-arrows, .avia-slideshow-dots, .avia-slideshow-controls"): x.decompose()
    for im in e.find_all("img"): im.decompose()
    for l in e.find_all("a", href=True):
        h = l["href"]; m = re.match(r"https?://(?:www\.)?italfuni\.it/servizi/([a-z0-9-]+)/?$", h)
        if m and m.group(1) in SLUGS: l["href"] = "{{ '/servizi/%s/' | relative_url }}" % m.group(1)
        elif "italfuni.it" in h or h.startswith("#") or h.startswith("tel:") and False: l.unwrap()
    for h in e.find_all(["h1","h2","h3","h4","h5"]):
        for t in h.find_all(["strong","b","em","i"]): t.unwrap()
    for t in e.find_all(["strong","b","em","i","a"]):
        n, p = t.next_sibling, t.previous_sibling
        if isinstance(n, NavigableString) and n[:1].isalnum(): n.replace_with(" "+str(n))
        if isinstance(p, NavigableString) and p[-1:].isalnum(): p.replace_with(str(p)+" ")
    # primo titolo uguale al titolo pagina -> via; h1 residui -> via
    for h in e.find_all("h1"): h.decompose()
    hs = e.find_all(["h2","h3"])
    if hs:
        norm = lambda x: re.sub(r"[^a-z0-9]+"," ",x.lower()).strip()
        a, b = norm(hs[0].get_text()), norm(titolo)
        primo_testo = next((x for x in e.descendants if isinstance(x, NavigableString) and x.strip()), None)
        if a and primo_testo is not None and primo_testo.strip() == hs[0].get_text().strip() and (a in b or b in a or len(a) < 3): hs[0].decompose()
    t = md(str(e), heading_style="ATX", bullets="-")
    t = fix(t)
    for i,(pth,alt) in enumerate(imgs):
        t = t.replace(f"@@IMG{i}@@", '{%% include immagine.liquid src="%s" alt="%s" align="center" %%}' % (pth, alt.replace('"',"'")))
    t = re.sub(r"[ \t]+\n","\n",t); t = re.sub(r"\n{3,}","\n\n",t)
    t = re.sub(r"^\s*-\s*$\n?","",t,flags=re.M)
    return t.strip(), imgs

def meta(slug):
    s = BeautifulSoup((W/f"p__servizi__{slug}.html").read_bytes(), "html.parser")
    d = s.find("meta", attrs={"name":"description"})
    ttl = re.sub(r"\s*-\s*Italfuni\s*$","",s.title.string.strip())
    return fix(ttl), (fix(d.get("content").strip()) if d else "")

report = []
for i,(slug,titolo,inhome,desc) in enumerate(SERVIZI, start=1):
    testo, imgs = corpo(slug, titolo)
    ttl, mdesc = meta(slug)
    seo_t = ttl + " - Italfuni" if ttl.lower() != "pulizia vetri" else "Pulizia vetri su fune - Italfuni"
    fm = ["---","layout: servizio","title: "+q(titolo),"description: "+q(fix(desc)),"gruppo: "+q("I nostri servizi"),"ordine: %d"%i]
    if inhome: fm.append("in_home: true")
    fm += ["seo_title: "+q(seo_t),"seo_description: "+q(mdesc or fix(desc)),"---",""]
    contenuto = "\n".join(fm) + "\n" + testo + "\n"
    (OUT/"_servizi"/(slug+".md")).write_bytes(contenuto.replace("\n","\r\n").encode("utf-8"))
    flag = [k for k,rx in (("liquid-extra",r"\{\{(?! '/servizi)"),("lorem","(?i)lorem"),("url-vecchio","italfuni[.]it"),("email","protected"),("sliderResidui","Anteriore|Posteriore"),("@@","@@")) if re.search(rx, testo)]
    report.append((slug, len(testo), len(imgs), flag))
for r in report: print(r)

# ---- PORTFOLIO -> _projects
PROG = [
 ("pulizia-vetri-palestra","Pulizia vetrate palazzo",1,"https://italfuni.it/wp-content/uploads/2018/05/pulizia-vetri-su-fune-1200x630.jpg","pulizia-vetri-su-fune-1200x630.jpg","Pulizia vetrate palestra su fune"),
 ("pulizia-grondaie-roma","Pulizia grondaie",2,"https://italfuni.it/wp-content/uploads/2018/04/IMG_20180118_WA0002.jpg","img_20180118_wa0002.jpg","Pulizia delle grondaie"),
 ("titeggiatura-e-ripristino-frontalini","Tinteggiatura su fune",3,"https://italfuni.it/wp-content/uploads/2015/10/tinteggiatura-su-fune-1.jpg","tinteggiatura-su-fune-1.jpg","Tinteggiatura e ripristino frontalini"),
]
for slug,titolo,imp,url,nome,alt in PROG:
    s = BeautifulSoup((W/f"p__portfolio-articoli__{slug}.html").read_bytes(), "html.parser")
    main = s.select_one("#main") or s.body
    for sel in ("script","style","noscript"):
        for x in main.select(sel): x.decompose()
    righe = []
    for t in main.get_text("\n", strip=True).split("\n"):
        t = fix(t.strip())
        if len(t) > 40 and "Ti senti predisposto" not in t and "Copyright" not in t and t.lower() != alt.lower(): righe.append(t)
    pth = scarica(url, nome)
    d = s.find("meta", attrs={"name":"description"})
    breve = righe[0] if righe else titolo
    breve = (breve[:157].rsplit(" ",1)[0] + "…") if len(breve) > 160 else breve
    slugpulito = slug.replace("titeggiatura","tinteggiatura")
    fm = ["---","layout: page","title: "+q(titolo),"description: "+q(breve),"img: "+pth,"importance: %d"%imp,"category: Lavori","in_home: true"]
    if d: fm.append("seo_description: "+q(fix(d.get("content").strip())))
    fm += ["---",""]
    corpo_p = '{%% include immagine.liquid src="%s" alt="%s" align="center" %%}\n\n' % (pth, alt) + "\n\n".join(righe) + "\n"
    (OUT/"_projects"/(slugpulito+".md")).write_bytes(("\n".join(fm)+"\n"+corpo_p).replace("\n","\r\n").encode("utf-8"))
    print("progetto", slugpulito, len(righe), "paragrafi,", pth)
print(sorted((p.name, p.stat().st_size//1024) for p in (OUT/"assets/img/italfuni").iterdir()))