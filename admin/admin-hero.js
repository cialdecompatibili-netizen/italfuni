/* Foto della home (admin > Sito > Tema). Gestisce lo slider di foto in dissolvenza dietro il testo della home (hero).
   COME FUNZIONA: l'elenco sta in _data/hero.yml, due chiavi:
        secondi: 6                      (quanto resta ogni foto, da 3 a 20)
        foto:
          - assets/img/nome.jpg         (una riga per foto, nell'ordine di comparsa)
   _pages/home.md legge site.data.hero e genera da solo durata del ciclo, ritardi e keyframes (blocco Liquid sopra il box): il numero di foto e' libero.
   Se il file non esiste (o la lista e' vuota) la home usa le 5 foto di partenza: qui si parte da quelle, cosi' al primo Salva il file nasce con lo stesso aspetto.
   COME SI AGGIUNGE ALLA VISTA TEMA: questo file AVVOLGE A.views.tema (admin-tema.js, che deve essere caricato PRIMA) e aggiunge una seconda scheda sotto la favicon.
   La favicon non viene toccata. Le foto si scelgono con lo stesso selettore degli articoli (A.imgPick: carica dal PC o scegli da assets/img).
   PUNTI CRITICI
     (1) I percorsi si scrivono COMPLETI (assets/img/nome.jpg), diversamente dalla favicon: la home li prefissa con baseurl da sola.
     (2) Salvando si rilegge il file (sha fresco) e lo si riscrive per intero: il file contiene solo queste due chiavi, nessun commento da conservare.
     (3) Massimo MAXF foto: piu' foto = piu' peso da scaricare nella home (le altre sono lazy, ma pesano comunque).
     (4) Nomi file con spazi, due punti, # o virgolette non sono ammessi (romperebbero il YAML): il selettore normalizza i nomi, ma se ne incontra uno strano lo segnala.
     (5) Dopo Salva il sito si aggiorna in 2-3 minuti (deploy: _data/hero.yml e' un .yml, quindi parte da solo). */
(function (A) {
  var $ = A.$, esc = A.esc;
  var MAXF = 10, FILE = '_data/hero.yml';
  var DEFAULT = ['assets/img/italfuni/pulizia-vetri-su-fune-1200x630.jpg', 'assets/img/italfuni/window-cleaner-4593185_1280-1030x686.jpg',
    'assets/img/italfuni/bogota-4490438_1280-1-1030x685.jpg', 'assets/img/italfuni/rope-access-window-cleaning.jpg', 'assets/img/italfuni/operai-balconi.jpg'];
  var st = { foto: [], secondi: 6, orig: '', sha: '', nuovo: false };

  function serialize() {
    return 'secondi: ' + st.secondi + '\nfoto:\n' + st.foto.map(function (p) { return '  - ' + p; }).join('\n') + '\n';
  }
  function parse(t) {
    var s = (t.match(/^secondi:[ \t]*(\d+)/m) || [])[1], foto = [], re = /^[ \t]*-[ \t]*(\S.*?)[ \t]*$/gm, m;
    var i = t.search(/^foto:/m); if (i >= 0) { var rest = t.slice(i); while ((m = re.exec(rest))) foto.push(m[1].replace(/^["']|["']$/g, '')); }
    return { secondi: s ? Math.max(3, Math.min(20, +s)) : 6, foto: foto };
  }
  function paint() {
    var box = $('hr_list'); if (!box) return;
    box.innerHTML = st.foto.length ? st.foto.map(function (p, i) {
      return '<div class="im" style="display:flex;gap:10px;align-items:center;padding:8px;border:1px solid #e3e3e3;border-radius:6px;margin-bottom:8px;background:#fff">' +
        '<b style="width:22px;text-align:center">' + (i + 1) + '</b>' +
        '<img src="' + esc(A.rawUrl(p)) + '" style="width:110px;height:64px;object-fit:cover;border-radius:4px;border:1px solid #ccc">' +
        '<span style="flex:1;word-break:break-all"><small>' + esc(p) + '</small></span>' +
        '<button type="button" class="btn sm" data-a="su" data-i="' + i + '"' + (i === 0 ? ' disabled' : '') + ' title="Sposta prima">&#9650;</button>' +
        '<button type="button" class="btn sm" data-a="giu" data-i="' + i + '"' + (i === st.foto.length - 1 ? ' disabled' : '') + ' title="Sposta dopo">&#9660;</button>' +
        '<button type="button" class="btn sm" data-a="cambia" data-i="' + i + '">Cambia</button>' +
        '<button type="button" class="btn sm danger" data-a="togli" data-i="' + i + '" title="Togli dallo slider (il file resta in assets/img)">x</button></div>';
    }).join('') : '<p style="color:#787c82">Nessuna foto: la home usera\' le foto di partenza.</p>';
    $('hr_add').disabled = st.foto.length >= MAXF;
    $('hr_sec').value = st.secondi;
    $('hr_save').disabled = serialize() === st.orig;
  }
  function addPick(idx) {
    A.imgPick(null, { onPick: function (sel) {
      if (/[\s:#"']/.test(sel)) return A.toast('Il nome del file contiene caratteri non ammessi: rinominalo e ricaricalo', true);
      if (idx == null) st.foto.push(sel); else st.foto[idx] = sel;
      paint();
    } });
  }
  function save() {
    if (/[\s:#"']/.test(st.foto.join(''))) return Promise.resolve(A.toast('Nome file non ammesso in elenco', true));
    return A.getFile(FILE).then(function (f) { return f.sha; }, function () { return ''; }).then(function (sha) {
      return A.putFile(FILE, serialize(), sha, 'admin: foto della home (' + st.foto.length + ')').then(function () {
        st.orig = serialize(); A.toast('Salvato: il sito si aggiorna tra 2-3 minuti'); paint();
      });
    });
  }
  function build() {
    var h = '<div class="card" id="hr_card"><h3>Foto della home</h3>' +
      '<p style="margin-top:0;color:#787c82">Le foto che scorrono in dissolvenza dietro il testo in alto nella home. Si mostrano nell\'ordine della lista.</p>' +
      '<div id="hr_list"></div>' +
      '<p><button type="button" class="btn" id="hr_add">+ Aggiungi foto</button> <small style="color:#787c82">Scegli da assets/img o caricala dal PC. Massimo ' + MAXF + '.</small></p>' +
      '<p><label>Secondi per ogni foto</label><input id="hr_sec" type="number" min="3" max="20" style="width:90px"> <small style="color:#787c82">da 3 a 20</small></p>' +
      '<p style="margin-top:16px"><button type="button" class="btn primary" id="hr_save">Salva foto della home</button> <small style="color:#787c82">Il sito si aggiorna in 2-3 minuti.</small></p></div>';
    A.main().insertAdjacentHTML('beforeend', h);
    $('hr_add').onclick = function () { addPick(null); };
    $('hr_sec').oninput = function () { var v = parseInt(this.value, 10); if (v >= 3 && v <= 20) st.secondi = v; paint2(); };
    $('hr_sec').onchange = function () { var v = parseInt(this.value, 10); st.secondi = Math.max(3, Math.min(20, isNaN(v) ? 6 : v)); paint(); };
    $('hr_save').onclick = A.wrap(save);
    $('hr_list').addEventListener('click', function (e) {
      var b = e.target.closest ? e.target.closest('[data-a]') : null; if (!b) return;
      var i = +b.getAttribute('data-i'), a = b.getAttribute('data-a');
      if (a === 'togli') st.foto.splice(i, 1);
      else if (a === 'su' && i > 0) st.foto.splice(i - 1, 0, st.foto.splice(i, 1)[0]);
      else if (a === 'giu' && i < st.foto.length - 1) st.foto.splice(i + 1, 0, st.foto.splice(i, 1)[0]);
      else if (a === 'cambia') return addPick(i);
      paint();
    });
    paint();
  }
  /* aggiorna solo lo stato del pulsante Salva mentre si scrive nel campo secondi (senza ridisegnare e perdere il cursore) */
  function paint2() { var s = $('hr_save'); if (s) s.disabled = serialize() === st.orig; }

  function load() {
    return A.getFile(FILE).then(function (f) {
      var p = parse(f.text); st.foto = p.foto.length ? p.foto : DEFAULT.slice(); st.secondi = p.secondi;
      st.orig = p.foto.length ? serialize() : '';
    }, function () { st.foto = DEFAULT.slice(); st.secondi = 6; st.orig = ''; });
  }

  var orig = A.views.tema;
  A.views.tema = function () {
    var r = orig.apply(this, arguments);
    return Promise.resolve(r).then(function () { return load(); }).then(function () { if (A.main()) build(); });
  };
})(A);
