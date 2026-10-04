/* Note (admin > Sito > Note): un blocco appunti libero, salvato nella repo. Vedi CLAUDE.md punto 35.
   DOVE STA: il testo e' nel file `_data/note_admin.txt`. PUNTI CRITICI:
     (1) la cartella _data comincia con underscore e l'estensione .txt non e' letta da Jekyll come dato: il file NON finisce nel sito pubblicato.
         ATTENZIONE: la repo su GitHub e' pubblica (GitHub Pages), quindi chiunque apra la repo puo' leggerlo. Niente password, token o dati personali.
     (2) il salvataggio NON fa partire il deploy: deploy.yml scatta solo per assets, .html, .js, .liquid, .md, .yml ecc., non per .txt.
         Per questo si usa A.api('PUT') e non A.putFile: putFile chiamerebbe pollDeploy() e la barra del deploy resterebbe in attesa di una pubblicazione che non parte.
     (3) ogni salvataggio e' un commit ('admin: note'): lo sha viene riletto subito prima di scrivere (il pannello committa anche in parallelo).
     (4) se il file non esiste ancora la lettura da' 404: e' normale, si parte vuoti e il primo salvataggio lo crea.
     (5) la codifica base64 passa da encodeURIComponent per non rovinare accenti ed emoji. */
(function (A) {
  var $ = A.$, esc = A.esc;
  var PATH = '_data/note_admin.txt';
  var st = { sha: '', orig: '' };

  function b64(t) { return btoa(unescape(encodeURIComponent(t))); }
  function dirty() { var t = $('nt_txt'); return !!t && t.value !== st.orig; }
  function paint() {
    var s = $('nt_save'); if (s) s.disabled = !dirty();
    var m = $('nt_state'); if (m) m.textContent = dirty() ? 'Modifiche non salvate' : 'Salvato';
  }

  A.views.note = function () {
    return A.getFile(PATH).then(function (f) { return f; }, function (e) {
      if (e && e.status === 404) return { text: '', sha: '' };
      throw e;
    }).then(function (f) {
      st.sha = f.sha || ''; st.orig = f.text || '';
      A.main().innerHTML = '<h2>Note</h2><div class="card">' +
        '<p style="margin-top:0;color:#787c82">Appunti liberi: procedure, idee, cose da non dimenticare. Si salvano nella repo (file <b>' + esc(PATH) + '</b>), non compaiono nel sito e non fanno ripartire il deploy. ' +
        '<b>La repo e\' pubblica: niente password, token o dati personali.</b></p>' +
        '<textarea id="nt_txt" style="min-height:420px" spellcheck="true" placeholder="Scrivi qui i tuoi appunti..."></textarea>' +
        '<p style="margin-top:12px"><button type="button" class="btn primary" id="nt_save">Salva note</button> <small id="nt_state" style="color:#787c82"></small> ' +
        '<small style="color:#787c82">Scorciatoia: Ctrl+S</small></p></div>';
      $('nt_txt').value = st.orig;
      $('nt_txt').oninput = paint;
      $('nt_txt').onkeydown = function (e) { if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S')) { e.preventDefault(); if (dirty()) $('nt_save').click(); } };
      $('nt_save').onclick = A.wrap(save);
      paint();
    });
  };

  /* salva: rilegge lo sha (puo' essere cambiato), poi PUT sul file; senza sha il file viene creato */
  function save() {
    var t = $('nt_txt').value;
    return A.getFile(PATH).then(function (f) { return f.sha; }, function (e) {
      if (e && e.status === 404) return '';
      throw e;
    }).then(function (sha) {
      var body = { message: 'admin: note', content: b64(t), branch: A.branch() };
      if (sha) body.sha = sha;
      return A.api('PUT', '/contents/' + PATH, body).then(function (r) {
        st.sha = (r && r.content && r.content.sha) || ''; st.orig = t; A.toast('Note salvate'); paint();
      });
    });
  }
})(A);
