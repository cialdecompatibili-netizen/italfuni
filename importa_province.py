# Importa i servizi PER PROVINCIA (Lazio) da italfuni.it nel clone Jekyll: un file in _servizi/ per articolo, gruppo = provincia.
# Usato il 05/10/2026. Procedura completa: CLAUDE.md punti 34 e 36. Legge/scrive in %TEMP%\italfuni_prov_src e italfuni_prov_out.
# L'elenco articoli si ricava dalla categoria https://italfuni.it/servizio/servizi-per-provincia/ (pagine /page/N/).
import pathlib, re, shutil, urllib.request, hashlib, time
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md

HOME = pathlib.Path.home()
REPO = HOME / "Desktop/italfuni"
W = HOME / "AppData/Local/Temp/italfuni_prov_src"; W.mkdir(parents=True, exist_ok=True)
OUT = HOME / "AppData/Local/Temp/italfuni_prov_out"
if OUT.exists(): shutil.rmtree(OUT)
(OUT / "_servizi").mkdir(parents=True); (OUT / "assets/img/italfuni").mkdir(parents=True)
BASE = "https://italfuni.it"
UA = {"User-Agent": "Mozilla/5.0"}
PROV = {"roma": "Roma e provincia", "latina": "Latina e provincia", "rieti": "Rieti e provincia",
        "viterbo": "Viterbo e provincia", "frosinone": "Frosinone e provincia"}
VECCHI = {p.stem for p in (REPO / "_servizi").glob("*.md")}  # i servizi generali gia' migrati (link interni)
STOCK = re.compile(r"(architect|modern-kitchen|construction-site|scale-ruler|cropped-hand|urban-development|modern-home|house-|team-banner|favicon|logo|envato|themeforest|dribbble|wordpress|microlancer|regione-lazio)", re.I)
SPAM = re.compile(r"casin|aams|scommess|slot|poker|betting|azzardo", re.I)
TYPO = {"dissuarossori": "dissuasori", "maggio senso": "maggior senso", "pulici": "puliti", "leder": "leader", "spedilizzata": "specializzata",
        "abbatere": "abbattere", "Impresa edie": "Impresa edile", "manutenzone": "manutenzione", "Istallazione": "Installazione", "de effettuare": "da effettuare"}

def fetch(url):
    f = W / (hashlib.md5(url.encode()).hexdigest() + ".bin")
    if f.exists(): return f.read_bytes()
    err = None
    for _ in range(3):
        try:
            d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
            f.write_bytes(d); return d
        except Exception as e:
            err = e; time.sleep(2)
    raise err

def fix(t):
    for a, b in TYPO.items(): t = t.replace(a, b)
    return t.replace("\xa0", " ")

def q(v): return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'

# 1) elenco articoli e provincia
posts = {}
for n in range(1, 12):
    url = BASE + "/servizio/servizi-per-provincia/" + ("" if n == 1 else "page/%d/" % n)
    try: s = BeautifulSoup(fetch(url), "html.parser")
    except Exception: break
    nuovi = 0
    for a in s.select("article"):
        provs = [m for l in a.find_all("a", href=True) for m in re.findall(r"/servizio/edilizia-su-fune-([a-z]+)/", l["href"])]
        t = a.select_one("h2 a, h1 a, .entry-title a")
        if not t or not provs or provs[0] not in PROV: continue
        u = t["href"].split("#")[0]
        if u not in posts: posts[u] = provs[0]; nuovi += 1
    print("pagina", n, "nuovi", nuovi)
    if nuovi == 0: break
print("TOTALE articoli:", len(posts))
SLUGS = {u.rstrip("/").rsplit("/", 1)[1] for u in posts}

def scarica(src, nome):
    dest = OUT / "assets/img/italfuni" / nome
    if not dest.exists():
        orig = re.sub(r"-\d+x\d+(?=\.\w+$)", "", src)
        for u in (orig, src):
            try: dest.write_bytes(fetch(u)); break
            except Exception: continue
        else: return None
    return "assets/img/italfuni/" + nome

report = []
for url, prov in posts.items():
    slug = url.rstrip("/").rsplit("/", 1)[1]
    s = BeautifulSoup(fetch(url), "html.parser")
    e = s.select_one(".post-entry") or s.select_one("article")
    ttl = re.sub(r"\s*[-|]\s*Italfuni\s*$", "", s.title.string.strip()) if s.title else slug
    ttl = fix(ttl)
    d = s.find("meta", attrs={"name": "description"}) or s.find("meta", attrs={"property": "og:description"})
    for sel in ("#ez-toc-container", "script", "style", "form", "noscript", ".avia-button-wrap", ".avia_codeblock_section", ".sharedaddy", ".entry-footer", ".avia-slideshow-arrows", ".avia-slideshow-dots"):
        for x in e.select(sel): x.decompose()
    img = None
    for im in e.find_all("img"):
        src = im.get("src", ""); base = src.rsplit("/", 1)[-1].lower()
        if "wp-content/uploads" in src and not STOCK.search(base) and not re.search(r"-(36|80|120|180)x\d+\.", base):
            nome = re.sub(r"-\d+x\d+(?=\.\w+$)", "", base)
            p = scarica(src, nome)
            if p: img = (p, fix((im.get("alt") or ttl).strip()) or ttl); break
    for x in e.select(".avia-slideshow"): x.decompose()
    for im in e.find_all("img"): im.decompose()
    esterni = []
    for l in e.find_all("a", href=True):
        h = l["href"]; m = re.match(r"https?://(?:www\.)?italfuni\.it/(?:servizi/)?([a-z0-9-]+)/?$", h)
        if m and (m.group(1) in SLUGS or m.group(1) in VECCHI): l["href"] = "{{ '/servizi/%s/' | relative_url }}" % m.group(1)
        else:
            if h.startswith("http") and "italfuni.it" not in h: esterni.append(h)
            l.unwrap()
    for h in e.find_all(["h1", "h2", "h3", "h4", "h5"]):
        for t in h.find_all(["strong", "b", "em", "i"]): t.unwrap()
    for t in e.find_all(["strong", "b", "em", "i"]):
        n_, p_ = t.next_sibling, t.previous_sibling
        if isinstance(n_, NavigableString) and n_[:1].isalnum(): n_.replace_with(" " + str(n_))
        if isinstance(p_, NavigableString) and p_[-1:].isalnum(): p_.replace_with(str(p_) + " ")
    for h in e.find_all("h1"): h.decompose()
    hs = e.find_all(["h2", "h3"])
    if hs:
        norm = lambda x: re.sub(r"[^a-z0-9]+", " ", x.lower()).strip()
        a_, b_ = norm(hs[0].get_text()), norm(ttl)
        primo = next((x for x in e.descendants if isinstance(x, NavigableString) and x.strip()), None)
        if a_ and primo is not None and primo.strip() == hs[0].get_text().strip() and (a_ in b_ or b_ in a_): hs[0].decompose()
    t = fix(md(str(e), heading_style="ATX", bullets="-"))
    t = re.sub(r"\*\*(\s*)\*\*", r"\1", t)
    t = re.sub(r"(?im)^(?:edilizia su fune [a-z]+(?:, )?|servizi per provincia(?:, )?)+\s*$", "", t)  # elenco categorie WP in testa all'articolo
    t = re.sub(r"(?im)^\d{1,2} \w+ \d{4}\s*/\s*da .*$", "", t)  # riga data/autore
    righe = [r for r in t.split("\n")]
    tolti = [r for r in righe if SPAM.search(r)]
    t = "\n".join(r for r in righe if not SPAM.search(r))
    t = re.sub(r"[ \t]+\n", "\n", t); t = re.sub(r"\n{3,}", "\n\n", t); t = re.sub(r"^\s*-\s*$\n?", "", t, flags=re.M).strip()
    if img: t = '{%% include immagine.liquid src="%s" alt="%s" align="center" %%}\n\n' % (img[0], img[1].replace('"', "'")) + t
    prima = re.sub(r"[#*_>`\-\[\]]|\{%.*?%\}", " ", next((r for r in t.split("\n\n") if len(r) > 60 and not r.startswith("{%")), ttl))
    desc = re.sub(r"\s+", " ", prima).strip()
    if len(desc) > 155: desc = desc[:155].rsplit(" ", 1)[0] + "..."
    sd = fix(d.get("content").strip()) if d and d.get("content") else desc
    fm = ["---", "layout: servizio", "title: " + q(ttl), "description: " + q(desc), "gruppo: " + q(PROV[prov]),
          "seo_title: " + q(ttl + " - Italfuni"), "seo_description: " + q(sd), "---", ""]
    (OUT / "_servizi" / (slug + ".md")).write_bytes(("\n".join(fm) + "\n" + t + "\n").replace("\n", "\r\n").encode("utf-8"))
    flag = [k for k, c in (("SPAM-TOLTO", bool(tolti)), ("LINK-ESTERNI", bool(esterni)), ("lorem", bool(re.search("(?i)lorem", t))), ("corto", len(t) < 300), ("@@", "@@" in t)) if c]
    report.append((prov, slug, len(t), bool(img), flag, esterni[:3], [x[:90] for x in tolti[:2]]))

for r in sorted(report): print(r)
from collections import Counter
print(Counter(r[0] for r in report))
print("immagini:", sorted(p.name for p in (OUT / "assets/img/italfuni").iterdir()))
