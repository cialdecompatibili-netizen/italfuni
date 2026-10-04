# Aggiunge l'immagine in testa ai servizi che non ne hanno (foto scelte per tema tra quelle gia' in assets/img/italfuni).
# Uso: python aggiungi_immagini.py (dalla radice della repo). Idempotente: salta i file che hanno gia' l'include.
import pathlib, re
G = "assets/img/italfuni/img_20180118_wa0002.jpg"
M = {"impermeabilizzazione-su-fune-a-roma": "impermeabilzzazione.jpg",
     "installazione-e-manutenzione-dissuasori-volatili": G, "manutenzione-e-installazione-canne-fumarie": G,
     "messa-in-sicurezza": G, "messa-in-sicurezza-a-roma": G, "messa-in-sicurezza-a-viterbo": G, "messa-in-sicurezza-dei-lavoratori-latina": G,
     "montaggio-sistemi-di-sicurezza-su-fune": G, "pulizia-componenti-su-fune": G,
     "montaggio-isolanti": "isolanti.jpg", "montaggio-isolanti-a-roma-con-italfuni": "isolanti.jpg",
     "potatura-alberi": "potatura-albero-con-corde.jpg.jpg", "ristrutturazione-tetto": "riparazione-tetti.jpg",
     "ristrutturazioni-balconi-e-facciate": "operai-balconi.jpg", "ristrutturazioni-balconi-e-facciate-su-fune-a-roma": "operai-balconi.jpg",
     "tinteggiature-complete-a-roma": "tinteggiatura.jpg", "tinteggiature-complete-su-fune": "tinteggiatura.jpg"}
n = 0
for slug, img in M.items():
    p = pathlib.Path("_servizi") / (slug + ".md")
    b = p.read_bytes().decode("utf-8")
    if "include immagine.liquid" in b: continue
    src = img if img.startswith("assets/") else "assets/img/italfuni/" + img
    assert pathlib.Path(src).exists(), src
    nl = "\r\n" if "\r\n" in b else "\n"
    m = re.search(r'^title: "(.*)"\s*$', b, re.M)
    alt = (m.group(1) if m else slug).replace('"', "'")
    inc = '{%% include immagine.liquid src="%s" alt="%s" align="center" %%}' % (src, alt)
    fm = re.match(r"---\r?\n.*?\r?\n---\r?\n", b, re.S)
    b = b[:fm.end()] + nl + inc + nl + b[fm.end():].lstrip("\r\n").join(["", ""]) if False else b[:fm.end()] + nl + inc + nl + nl + b[fm.end():].lstrip("\r\n")
    p.write_bytes(b.encode("utf-8")); n += 1; print("ok", slug)
print("aggiornati:", n)
