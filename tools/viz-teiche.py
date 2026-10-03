"""Draw assets/viz/teiche.svg: the water cascade of the Oberharz after Calvör (1763),
from the Bruchberg over Clausthal and Zellerfeld down to Wildemann and Lautenthal,
with St. Andreasberg apart, and below it a timeline of the works and breaches.
Every label links to the unit that documents it.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "teiche.svg"
T = "#/text/teiche/"
W, H = 900, 640


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="te-t te-d" font-family="var(--serif)">',
         '<title id="te-t">Das Wasser fließt von Stadt zu Stadt</title>',
         '<desc id="te-d">Oben eine Treppe von links oben nach rechts unten: der Bruchberg mit dem Dammgraben, dann Clausthal mit 32 Teichen, Zellerfeld mit 31 Teichen, Wildemann und Lautenthal an der Innerste, die das Wasser von oben erhalten. Abseits St. Andreasberg mit dem Rehberger Graben und dem Oderteich. Unten eine Zeitleiste: 1565 der erste Teichwärter, 1572 brechen etliche Teiche, 1611 bis 1614 der Schwarzenbacher Teich, 1644 der Bärenbrucher Teich, 1686 bis 1703 der Rehberger Graben, 1714 der Oderteich, 1732 bis 1734 der Dammgraben, 1733 bricht der untere Schalker Teich.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Das Wasser fließt von Stadt zu Stadt</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Nach Calvör (1763). Dasselbe Wasser treibt oben die Räder und unten die nächsten; sind die Teiche oben leer, versiegt der Fluss unten auch.</text>']
    steps = [(95, 90, "Bruchberg", "Dammgraben 1732–1734", T + "graeben/1"),
             (265, 160, "Clausthal", "32 Teiche", T + "verzeichnis/1"),
             (440, 230, "Zellerfeld", "31 Teiche; der Schalker Teich", T + "verzeichnis/2"),
             (610, 300, "Wildemann", "Innerste, von oben gespeist", T + "verzeichnis/3"),
             (790, 360, "Lautenthal", "Aufschlag- und Stollenwasser", T + "verzeichnis/3")]
    prev = None
    for x, y, name, line, href in steps:
        o.append(f'<rect x="{x - 75}" y="{y}" width="150" height="46" rx="8" fill="var(--panel)" stroke="var(--wasser)" stroke-width="1.8"/>')
        o.append(a(x, y + 20, name, href, size=14.5, colour="wasser", bold=True))
        o.append(a(x, y + 37, line, href, size=11.5))
        if prev:
            px, py = prev
            o.append(f'<path d="M {px + 75} {py + 30} C {px + 110} {py + 30}, {x - 110} {y + 16}, {x - 77} {y + 16}" fill="none" stroke="var(--wasser)" stroke-width="3" opacity="0.8" marker-end="url(#te-a)"/>')
        prev = (x, y)
    o.insert(5, '<defs><marker id="te-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--wasser)"/></marker></defs>')
    # St. Andreasberg apart
    o.append('<rect x="560" y="80" width="300" height="70" rx="10" fill="var(--wasser)" opacity="0.08"/>')
    o.append(a(710, 104, "St. Andreasberg, ‚des Wassers am bedürftigsten‘", T + "verzeichnis/4", size=12.5, colour="wasser", bold=True))
    o.append(a(710, 124, "Rehberger Graben 1686–1703, Oderteich 1714", T + "verzeichnis/4", size=12))
    o.append(a(710, 141, "Damm aus gestampftem Sand, ‚noch nie versucht‘", T + "verzeichnis/4", size=11.5))
    # timeline
    y0, x0, x1 = 500, 60, 860
    lo, hi = 1560, 1740
    X = lambda yr: x0 + (yr - lo) / (hi - lo) * (x1 - x0)
    o.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="var(--ink2)" stroke-width="1.5"/>')
    for yr in range(1560, 1741, 20):
        o.append(f'<line x1="{X(yr):.0f}" y1="{y0 - 4}" x2="{X(yr):.0f}" y2="{y0 + 4}" stroke="var(--ink2)"/>')
        o.append(f'<text x="{X(yr):.0f}" y="{y0 + 20}" text-anchor="middle" font-size="11" fill="var(--ink2)">{yr}</text>')
    events = [(1565, 1565, "erster Teichwärter", "bau/1", "wasser", -1),
              (1572, 1572, "Teiche brechen", "bau/2", "red", 1),
              (1611, 1614, "Schwarzenbacher Teich", "verzeichnis/1", "wasser", -1),
              (1644, 1644, "Bärenbrucher Teich", "verzeichnis/1", "wasser", 1),
              (1686, 1703, "Rehberger Graben", "verzeichnis/4", "wasser", -1),
              (1714, 1714, "Oderteich", "verzeichnis/4", "wasser", 1),
              (1732, 1734, "Dammgraben", "graeben/1", "wasser", -1),
              (1733, 1733, "Schalker Teich bricht", "verzeichnis/2", "red", 2)]
    for a0, a1, label, href, c, side in events:
        xa, xb = X(a0), X(a1)
        if a1 > a0:
            o.append(f'<rect x="{xa:.0f}" y="{y0 - 5}" width="{max(4, xb - xa):.0f}" height="10" fill="var(--{c})" opacity="0.7"/>')
        else:
            o.append(f'<circle cx="{xa:.0f}" cy="{y0}" r="6" fill="var(--{c})"/>')
        ly = y0 - 26 if side < 0 else (y0 + 44 if side == 1 else y0 + 66)
        o.append(f'<line x1="{(xa + xb) / 2:.0f}" y1="{y0 + (-8 if side < 0 else 8)}" x2="{(xa + xb) / 2:.0f}" y2="{ly + (6 if side < 0 else -14)}" stroke="var(--{c})" stroke-width="1"/>')
        o.append(a((xa + xb) / 2, ly, label, T + href, size=12, colour="red" if c == "red" else "ink"))
    o.append('<text x="60" y="610" font-size="12" fill="var(--ink2)">Rot: Dammbrüche, die Calvör überliefert (1572 nach Häcke; 1733 ‚that großen Schaden‘). Die Jahre der übrigen Teiche nennt er nicht.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
