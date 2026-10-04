/* Das Wasser trägt den Berg. Silberbergbau und Wasserwirtschaft im Oberharz 1520–1866 — ein Quellenapparat. Vanilla JS, Hash-Routen. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { bergamt: "Bergamt und Landesherr", wasser: "Wasser und Maschinen", bergleute: "Bergleute und Knappschaft", wald: "Wald und Hütten", besucher: "Gelehrte und Besucher" };
const LANGS = { la: "Latein", fnhd: "Frühneuhochdeutsch", nhd: "Älteres Neuhochdeutsch", fr: "Französisch", de: "Deutsch", en: "Übertragung" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("harz_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">1520–1866 · Oberharz · Bergamt · Wasser · Bergleute</span>
      <h1>Das Wasser trägt den Berg</h1>
      <p class="lede">Um 1520 riefen die Landesherren mit Bergfreiheiten Bergleute in den Oberharz; in Clausthal, Zellerfeld und St. Andreasberg entstanden Bergstädte auf dem Silber. Je tiefer die Gruben wurden, desto mehr Wasser drang in sie ein, und gehoben werden konnte es nur mit Wasser: mit Rädern, die von Teichen und Gräben gespeist wurden, die man über drei Jahrhunderte in den Berg legte. Der Bergbau des Oberharzes war deshalb immer auch ein Kampf um Wasser, um Holz für die Hütten und um Geld für Teiche und Stollen. Gottfried Wilhelm Leibniz versuchte es in den 1680er-Jahren mit Windkraft und scheiterte. 1866 kam der Oberharz an Preußen; hier endet dieser Apparat.</p>
      <p class="readable">Der Apparat folgt dieser Geschichte durch gemeinfreie Drucke: den Bericht des Berghauptmanns Löhneyß (1617), die Chroniken des Henning Calvör (1763, 1765), Leibniz' eigene Schriften und die späteren Urteile über sie, die Rede und die Predigt zum Beginn des Tiefen Georg-Stollens (1777), die Schriften des Clausthaler Bergarztes Lentin (1774–1808), Heines Harzreise, Kerls Wegweiser (1852) und die Beschreibung der Wasserwirtschaft von 1868, jeweils das Original neben einer neuhochdeutschen Übertragung. Alle zehn Module der ersten Stufe sind erschienen.</p>
    </div>
  </div>

  <h2>Was der Apparat enthält</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">Die ersten Module sind in Arbeit; die Seite „Texte“ nennt sie mit ihren Quellen.</p>`}

  <h2>Die Fragen</h2>
  <div class="grid g2">
    <div class="panel"><h3>Trug das Erz den Berg, oder das Wasser?</h3>
      <p>Reiche Gänge machten den Oberharz berühmt. Aber jede Grube war nur so tief, wie das Wasser sich heben ließ, und gehoben wurde es mit Wasser. Der Apparat prüft, ob der Bergbau mehr an den Teichen hing als an den Gängen.</p></div>
    <div class="panel"><h3>Wer trug die Kosten, und wer die Gefahr?</h3>
      <p>Der Landesherr nahm den Zehnten, die Gewerken trugen die Zubuße, das Bergamt baute Teiche und Stollen. Die Gefahr trugen die Bergleute: Wasser, Wetter, Fahrten und Staub. Der Bergarzt von Clausthal hat aufgeschrieben, woran sie erkrankten.</p></div>
    <div class="panel"><h3>Warum scheiterte Leibniz?</h3>
      <p>Ein Universalgelehrter wollte die Gruben mit Windmühlen entwässern und bekam dafür einen Vertrag. Bergamt und Erfinder lasen ihn verschieden, der Wind war zu schwach oder zu stark, und 1686 wurde die Maschine abgebrochen. Der Apparat stellt Leibniz' eigene Worte neben Calvörs Bericht aus den Akten und die späteren Urteile über die Schuld.</p></div>
    <div class="panel"><h3>Lässt sich das spielen?</h3>
      <p>Ein Begleitspiel, <a href="https://die-last-der-grundwasser.netlify.app/"><em>Die Last der Grundwasser</em></a>, ist als Prototyp 0 spielbar: Man führt das Bergamt über Generationen, von 1521 bis 1866, zwischen Landesherr, Gewerken und Knappschaft, mit Regen und Dürre, Teichen, Gräben, Kunsträdern und Stollen. Gruben können absaufen, Bergleute verunglücken. Jede Karte verweist auf eine Stelle, die hier abgedruckt ist.</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texte</span><h1>Das Korpus</h1>
    <p class="lede">Jedes Modul ist vollständig lesbar, das Original neben der Übersetzung.</p>
    ${D.mods.shipped.length ? `<h2>Abgedruckt</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>Geplant</h2><div class="grid g2">${D.mods.planned.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">geplant</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Quelle:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">Geprüft und nicht aufgenommen</h2><div class="grid g2">${D.mods.missing.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">nicht aufgenommen</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Quelle:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Wird geladen…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const langs = [...new Set(sec.units.filter(u => u.orig).map(u => u.lang || t.orig_sprache))];
  const origName = langs.length === 1 ? (LANGS[langs[0]] || "Original") : langs.length === 2 ? langs.map(l => LANGS[l] || l).join(" oder ") : "Original";
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← Alle Texte</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · zitiert als ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${(sec.plates || []).length ? `<div class="grid g4 secplates">${sec.plates.map(plateOf).filter(Boolean).map(plateFig).join("")}</div>` : ""}
    ${sec.viz ? `<div class="viz" id="viz"><p class="fine">Wird geladen…</p></div>` : ""}
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + Übertragung`], ["orig", origName], ["en", "Übertragung"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Quelle und Editionsnotiz</span>
      <p><b>Quelle.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  bindPlates(view);
  if (sec.viz) fetch(`assets/viz/${sec.viz}.svg`).then(r => r.ok ? r.text() : "").then(svg => {
    const el = document.getElementById("viz");
    if (el) el.innerHTML = svg || "";
  });
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Zitieren als ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}${u.lang && langs.length > 1 ? ` <span class="fine">(${esc(LANGS[u.lang] || u.lang)})</span>` : ""}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(u.lang || t.orig_sprache)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("harz_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Vergleich</span><h1>Bergamt, Bergleute und Besucher</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← Alle Vergleiche</a></p><p class="fine">Wird geladen…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(sec.autor || t.autor)}</b><br><span class="fine">${esc(t.jahr)} · ${esc(sec.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← Alle Vergleiche</a></p>
    <span class="tag">Vergleich</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Zeitleiste</span><h1>1520–1866</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Tafeln</span><h1>Ansichten, Risse, Maschinen</h1>
    <p class="lede">${esc(D.plates.lede || "")}</p>
    <div class="grid g4">${D.plates.plates.map(plateFig).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  bindPlates(view);
}

function plateFig(p) {
  return `<figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`;
}

function bindPlates(root) {
  root.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Quellen, Methode, Grenzen</span><h1>Wie dieser Apparat gemacht ist</h1>
    <div class="readable">
    <p><b>Nur Gemeinfreies.</b> Jeder Text stammt aus einem Druck, dessen Schutzfrist abgelaufen ist; die Quelle steht auf seiner Seite. Moderne Editionen und Übersetzungen, die noch geschützt sind, werden nicht benutzt.</p>
    <p><b>Die Seite ist maßgeblich.</b> Die Hauptquellen sind Fraktur- und Antiquadrucke des 17. bis 19. Jahrhunderts: Löhneyß (1617, benutzt in der Ausgabe 1660), Calvör (1763, 1765), Gerlands Ausgabe der technischen Schriften von Leibniz (1906), Trebra (1789), Lentin (1774), die Rede zum Georg-Stollen (1777), Heine (1826) und Dumreicher (1868). Die maschinelle Texterkennung der Scans ist nur Hilfsmittel: Jede Stelle ist am Seitenbild gelesen, und jede Korrektur, die über das Offensichtliche hinausgeht, steht in den Anmerkungen. Die Schreibung der Drucke bleibt erhalten.</p>
    <p><b>Übertragungen.</b> Die neuhochdeutschen Übertragungen sind eigene Arbeit, nah am Original und gemeinfrei (CC0). Sie sind eine Lesehilfe, keine kritische Übersetzung; Fachwörter des Bergbaus (Gang, Stollen, Kunst, Zubuße, Ausbeute) werden in den Anmerkungen erklärt, und wo ein Wort unsicher ist, sagt es die Anmerkung.</p>
    <p><b>Stimmen und Abstände.</b> Die meisten Quellen stammen von oben: von Berghauptleuten, Bergbeamten, einem Gelehrten, einem Arzt. Die Bergleute selbst sprechen in ihnen selten. Jedes Modul nennt, wer schrieb, wann und für wen, und sagt, wessen Stimme fehlt.</p>
    <p><b>Daten.</b> Die Daten der Texte stehen wie geschrieben (Heiligentage, Wochentage) mit dem heutigen Datum daneben.</p>
    </div>
    <h2>Abgedruckte Quellen</h2>
    ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>` : `<p class="fine">Noch keine; die geplanten Module nennen ihre Quellen auf der Seite „Texte“.</p>`}
    ${(D.plates.plates || []).length ? `<h2>Tafeln</h2><p class="fine readable">${esc(D.plates.credit)}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Der Apparat konnte nicht geladen werden: ${esc(e.message)}</p>`; });
