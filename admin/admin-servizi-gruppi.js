/* Gruppi servizi (admin > Contenuti > Gruppi servizi): modifica l'elenco delle SEZIONI della pagina /servizi/ (le "categorie" dei servizi). Vedi CLAUDE.md punto 36.
   DOVE STA: _data/servizi_gruppi.yml, righe `- "nome"` NELL'ORDINE in cui compaiono in pagina. Ogni servizio sceglie la sua sezione col campo `gruppo`
   (tendina in admin > Servizi, che legge questo stesso file). PUNTI CRITICI:
     (1) il nome del gruppo nel servizio deve essere IDENTICO a quello dell'elenco: se RINOMINI o ELIMINI un gruppo qui, i servizi che lo usano
         restano col vecchio nome e finiscono in "Altri servizi" finche' non li riassegni da admin > Servizi (azione di gruppo 'Categoria').
     (2) le righe di commento (#) in testa al file vengono conservate; le altre righe sono rigenerate dall'elenco.
     (3) niente virgolette nei nomi (vengono tolte) ne' righe vuote o doppioni (vengono scartati).
     (4) il salvataggio e' un commit su un .yml: il sito si ripubblica (2-3 minuti). */
(function (A) {
  var $ = A.$, esc = A.esc;
  var PATH = '_data/servizi_gruppi.yml';
  var st = { orig: '' };

  function parse(text) {
    var out = [];
    String(text || '').split(/\r?\n/).forEach(function (r) { var m = r.match(/^\s*-\s+(.+?)\s*$/); if (m) out.push(m[1].replace(/^["']|["']$/g, '')); });
    return out;
  }
  function clean(v) {
    var seen = {}, out = [];
    String(v).split(/\r?\n/).forEach(function (r) {
      r = r.replace(/["\\]/g, '').replace(/\s+/g, ' ').trim();
      if (r && !seen[r.toLowerCase()]) { seen[r.toLowerCase()] = 1; out.push(r); }
    });
    return out;
  }
  function paint() {
    var t = $('sg_txt'); if (!t) return;
    var n = clean(t.value).length;
    $('sg_n').textContent = n + (n === 1 ? ' gruppo' : ' gruppi');
    $('sg_save').disabled = clean(t.value).join('\n') === st.orig || n === 0;
  }

  A.views.gruppi = function () {
    return A.getFile(PATH).then(function (f) {
      var list = parse(f.text); st.orig = list.join('\n');
      A.main().innerHTML = '<h2>Gruppi servizi</h2><div class="card">' +
        '<p style="margin-top:0;color:#787c82">Sono le sezioni della pagina <b>/servizi/</b>, nell\'ordine in cui compaiono. Scrivi <b>un gruppo per riga</b>; cambia l\'ordine spostando le righe. ' +
        'Ogni servizio sceglie il suo gruppo da <b>Servizi</b> (campo gruppo).</p>' +
        '<textarea id="sg_txt" style="min-height:220px" spellcheck="false"></textarea>' +
        '<p style="color:#787c82;margin:8px 0 0"><b>Attenzione:</b> se rinomini o togli un gruppo, i servizi che lo usano finiscono in "Altri servizi" finche\' non cambi il loro gruppo da Servizi.</p>' +
        '<p style="margin-top:12px"><button type="button" class="btn primary" id="sg_save">Salva gruppi</button> <small id="sg_n" style="color:#787c82"></small> ' +
        '<small style="color:#787c82">Il sito si aggiorna in 2-3 minuti.</small></p></div>';
      $('sg_txt').value = st.orig;
      $('sg_txt').oninput = paint;
      $('sg_save').onclick = A.wrap(save);
      paint();
    });
  };

  /* salva: rilegge il file (sha fresco), tiene le righe di commento in testa e riscrive l'elenco; stesso a capo del file letto */
  function save() {
    var list = clean($('sg_txt').value);
    if (!list.length) return Promise.resolve(A.toast('Serve almeno un gruppo', true));
    return A.getFile(PATH).then(function (f) {
      var nl = /\r\n/.test(f.text) ? '\r\n' : '\n';
      var head = f.text.split(/\r?\n/).filter(function (r) { return /^\s*#/.test(r); });
      var txt = head.concat(list.map(function (g) { return '- "' + g + '"'; })).join(nl) + nl;
      if (txt === f.text) return A.toast('Nessuna modifica');
      return A.putFile(PATH, txt, f.sha, 'admin: gruppi servizi').then(function () {
        st.orig = list.join('\n'); $('sg_txt').value = st.orig; A.toast('Salvato: il sito si aggiorna tra 2-3 minuti'); paint();
      });
    });
  }
})(A);
