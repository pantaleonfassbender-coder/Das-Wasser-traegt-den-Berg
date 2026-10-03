"""Draw assets/viz/stollen.svg: a schematic longitudinal section from the mouth of the
Tiefer Georg-Stollen at Grund to the Grube Caroline at Clausthal, after Reden (1777)
and Lasius (1789): the older adits above, the new one 80 Lachter deeper, the light
shafts, and the pumps that need to lift water less high. Below, a timeline 1771–1800.
Every label links to the unit that documents it.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "stollen.svg"
T = "#/text/stollen/"
W, H = 900, 660


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="st-t st-d" font-family="var(--serif)">',
         '<title id="st-t">Achtzig Lachter tiefer</title>',
         '<desc id="st-d">Ein schematischer Längsschnitt von links nach rechts: links das Mundloch des Tiefen Georg-Stollens bei Grund, rechts die Grube Caroline bei Clausthal, dazwischen das ansteigende Gebirge. Hoch oben liegen der Neunzehn-Lachter- und der Dreizehn-Lachter-Stollen, die bei Wildemann austreten. 80 Lachter tiefer verläuft der neue Stollen, 4910 Lachter lang; an der Caroline liegt er 162 Lachter unter Tage. Von oben führen Lichtlöcher hinab, das tiefste 113 Lachter nach Reden, 111 nach Lasius. Im Schacht der Caroline zeigen Pumpensätze, wie viel weniger hoch das Wasser nun gehoben werden muss. Unten eine Zeitleiste von 1771 bis 1800.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Achtzig Lachter tiefer</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Schema nach Reden (1777) und Lasius (1789), nicht maßstäblich. Was unter dem Stollen liegt, muss gepumpt werden;</text>',
         '<text x="16" y="64" font-size="13" fill="var(--ink2)">was darüber liegt, fließt durch ihn von selbst ab.</text>',
         '<defs><marker id="st-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--wasser)"/></marker></defs>']
    # mountain
    o.append('<path d="M 30 330 L 120 300 L 230 220 L 380 150 L 560 120 L 720 105 L 870 100 L 870 430 L 30 430 Z" fill="var(--ink2)" opacity="0.10"/>')
    o.append('<path d="M 30 330 L 120 300 L 230 220 L 380 150 L 560 120 L 720 105 L 870 100" fill="none" stroke="var(--ink2)" stroke-width="1.6"/>')
    # old adits
    o.append('<path d="M 300 182 L 790 168" stroke="var(--ink2)" stroke-width="3" stroke-dasharray="8 5"/>')
    o.append(a(300, 176, "Neunzehn-Lachter-Stollen", T + "bau/1", size=11.5, anchor="start", colour="ink2"))
    o.append('<path d="M 260 222 L 790 205" stroke="var(--ink)" stroke-width="3.2" stroke-dasharray="10 4"/>')
    o.append(a(262, 238, "Dreizehn-Lachter-Stollen, bisher der tiefste, aus bei Wildemann", T + "bau/1", size=11.5, anchor="start"))
    # new adit
    o.append('<path d="M 70 322 L 790 300" stroke="var(--wasser)" stroke-width="7" stroke-linecap="round"/>')
    o.append('<path d="M 70 322 L 30 330" stroke="var(--wasser)" stroke-width="5" marker-end="url(#st-a)"/>')
    o.append(a(330, 334, "Tiefer Georg-Stollen: 4910 Lachter (Reden), ‚nahe an 5000‘ (Lasius)", T + "rede/4", size=13, colour="wasser", bold=True))
    o.append(a(330, 352, "gemauert ‚ohne alle Mauerspeise‘, ‚für die Ewigkeit‘", T + "bau/1", size=11.5, colour="wasser"))
    # mouth at Grund
    o.append('<circle cx="70" cy="322" r="7" fill="var(--wasser)"/>')
    o.append(a(24, 286, "Mundloch bei Grund", T + "rede/4", size=12.5, anchor="start", colour="wasser", bold=True))
    o.append(a(24, 270, "26. Juli 1777: der erste Schlag", T + "rede/5", size=11.5, anchor="start"))
    o.append(a(76, 372, "1800: junge Linden, eine Inschrift", T + "bau/3", size=11.5, anchor="start"))
    # light shafts
    for x, y_top, label in [(230, 220, None), (400, 148, "Lichtloch: 113 Lachter (Reden), 111 (Lasius)"), (560, 120, None)]:
        yb = 322 - (x - 70) * 22 / 720
        o.append(f'<line x1="{x}" y1="{y_top}" x2="{x}" y2="{yb:.0f}" stroke="var(--bergamt)" stroke-width="2.2"/>')
        if label:
            o.append(a(x + 6, y_top - 10, label, T + "rede/4", size=11.5, anchor="start", colour="bergamt"))
    o.append(a(250, 116, "Lichtlöcher: von oben zugleich vortreiben und lüften", T + "rede/4", size=11.5, colour="bergamt"))
    # Caroline shaft
    sx = 790
    o.append(f'<rect x="{sx - 12}" y="100" width="24" height="320" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1.2"/>')
    o.append(a(sx, 90, "Grube Caroline, Clausthal", T + "rede/4", size=12.5, bold=True))
    for y in (232, 258, 284):
        o.append(f'<rect x="{sx - 9}" y="{y - 6}" width="18" height="12" fill="var(--red)" opacity="0.45"/>')
    for y in (330, 360, 390):
        o.append(f'<rect x="{sx - 9}" y="{y - 6}" width="18" height="12" fill="var(--wasser)" opacity="0.65"/>')
    o.append(f'<line x1="{sx + 18}" y1="205" x2="{sx + 18}" y2="300" stroke="var(--red)" stroke-width="1.4"/>')
    o.append(f'<line x1="{sx + 14}" y1="205" x2="{sx + 22}" y2="205" stroke="var(--red)"/><line x1="{sx + 14}" y1="300" x2="{sx + 22}" y2="300" stroke="var(--red)"/>')
    o.append(a(sx + 26, 250, "80 Lachter", T + "rede/4", size=12, anchor="start", colour="red", bold=True))
    o.append(a(sx + 26, 266, "weniger", T + "rede/4", size=11.5, anchor="start", colour="red"))
    o.append(a(sx + 26, 282, "zu heben", T + "rede/4", size=11.5, anchor="start", colour="red"))
    o.append(f'<line x1="{sx + 18}" y1="108" x2="{sx + 18}" y2="296" stroke="var(--ink2)" stroke-width="0.8" stroke-dasharray="3 3"/>')
    o.append(a(sx - 18, 318, "162 Lachter unter Tage", T + "rede/4", size=11.5, anchor="end", colour="wasser"))
    o.append(a(sx - 18, 410, "die Pumpen darunter heben nur noch bis hierher", T + "rede/2", size=11.5, anchor="end"))
    # timeline
    y0, x0, x1 = 525, 70, 840
    lo, hi = 1770, 1801
    X = lambda yr: x0 + (yr - lo) / (hi - lo) * (x1 - x0)
    o.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="var(--ink2)" stroke-width="1.5"/>')
    for yr in range(1770, 1801, 5):
        o.append(f'<line x1="{X(yr):.0f}" y1="{y0 - 4}" x2="{X(yr):.0f}" y2="{y0 + 4}" stroke="var(--ink2)"/>')
        o.append(f'<text x="{X(yr):.0f}" y="{y0 + 20}" text-anchor="middle" font-size="11" fill="var(--ink2)">{yr}</text>')
    o.append(f'<rect x="{X(1777.57):.0f}" y="{y0 - 5}" width="{X(1799.5) - X(1777.57):.0f}" height="10" fill="var(--wasser)" opacity="0.35"/>')
    events = [(1771.5, "Bergamtsprotokoll", "rede/3", "bergamt", -1),
              (1777.57, "26./27. Juli 1777: Rede und Predigt", "predigt/1", "wasser", 1),
              (1789, "Lasius: ‚noch nicht ganz vollendet‘", "bau/2", "ink", -1),
              (1799.5, "Durchschlag (neuere Literatur)", "bau/3", "ink2", 1),
              (1800.75, "Horstig in Grund", "bau/3", "besucher", -1)]
    for yr, label, href, c, side in events:
        x = X(yr)
        o.append(f'<circle cx="{x:.0f}" cy="{y0}" r="6" fill="var(--{c})"/>')
        ly = y0 - 26 if side < 0 else y0 + 46
        o.append(f'<line x1="{x:.0f}" y1="{y0 + (-8 if side < 0 else 8)}" x2="{x:.0f}" y2="{ly + (6 if side < 0 else -14)}" stroke="var(--{c})" stroke-width="1"/>')
        anchor = "end" if yr > 1798 and side < 0 else ("middle" if yr > 1772 else "start")
        o.append(a(x, ly, label, T + href, size=12, anchor=anchor))
    o.append('<text x="70" y="630" font-size="11.5" fill="var(--ink2)">Ein Lachter ist knapp zwei Meter (neuere Literatur). Die Kosten des Stollens nennt keine der hier abgedruckten Quellen.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
