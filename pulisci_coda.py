# Toglie da _servizi/*.md la coda WordPress (url immagine, 967, 2032, italfuni, logo, date) rimasta in fondo agli articoli.
# Uso: python pulisci_coda.py   (dalla radice della repo). Mantiene CRLF. Idempotente.
import pathlib, re
RX = re.compile(r"\s*https?://italfuni\.it/wp-content/uploads/\S+\s+\d+\s+\d+\s+italfuni\b.*\Z", re.S)
n = 0
for p in sorted(pathlib.Path("_servizi").glob("*.md")):
    b = p.read_bytes().decode("utf-8")
    crlf = "\r\n" in b
    t = RX.sub("", b).rstrip() + ("\r\n" if crlf else "\n")
    if t != b:
        p.write_bytes(t.encode("utf-8")); n += 1; print("pulito", p.name)
print("file puliti:", n)
