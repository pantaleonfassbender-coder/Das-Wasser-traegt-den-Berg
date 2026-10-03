"""Draw assets/viz/kunst.svg: the way of the water through an Oberharz mine after
Calvör (1763). Water from the pond drives the wheel; the wheel drives the rods;
the rods drive the pumps; the pumps lift the mine water to the adit, which leads
it out. Every label links to the unit that describes it.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "kunst.svg"
T = "#/text/"
W, H = 900, 650


def label(x, y, text, href, size=12.5, anchor="middle", colour="ink"):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="var(--{colour})" '
            f'stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ku-t ku-d" font-family="var(--serif)">',
         '<title id="ku-t">Das Wasser hebt das Wasser</title>',
         '<desc id="ku-d">Ein Schnitt durch Berg und Grube. Links oben ein Teich hinter einem Damm; ein Graben führt das Aufschlagwasser auf ein Kunstrad. Vom Rad läuft ein Feldgestänge über Tage zum Schacht und bewegt dort Pumpensätze übereinander, die das Grubenwasser Satz für Satz bis auf den Stollen heben. Der Stollen führt das Wasser zum Tal hinaus, zusammen mit dem Wasser, das das Rad getrieben hat. Darunter der Sumpf. Fällt der Teich trocken, steht alles still.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Das Wasser hebt das Wasser</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Schema nach Calvör (1763), nicht maßstäblich. Fällt der Teich trocken, steht die Kunst still, und die Grube säuft ab.</text>']
    # ground and hill
    o.append('<path d="M 0 170 L 300 170 L 360 150 L 900 150 L 900 650 L 0 650 Z" fill="var(--ink2)" opacity="0.10"/>')
    o.append('<path d="M 0 170 L 300 170 L 360 150 L 900 150" fill="none" stroke="var(--ink2)" stroke-width="1.5"/>')
    # pond and dam
    o.append('<path d="M 30 170 Q 110 215 200 170 Z" fill="var(--wasser)" opacity="0.55"/>')
    o.append('<path d="M 200 170 L 215 120 L 230 170 Z" fill="var(--ink2)" opacity="0.45"/>')
    o.append(label(110, 112, "Der Teich: ein Quartal ohne Regen", T + "kuenste/mangel/1", colour="wasser"))
    o.append(label(110, 130, "im Frost gar nicht", T + "kuenste/mangel/1", size=11.5, colour="wasser"))
    # ditch to wheel
    o.append('<path d="M 215 168 L 330 175 L 400 205" fill="none" stroke="var(--wasser)" stroke-width="5" stroke-linecap="round"/>')
    o.append(label(290, 160, "Graben: Aufschlagwasser", T + "kuenste/kunstrad/1", size=11.5, colour="wasser"))
    # wheel in Radstube
    cx, cy, r = 430, 255, 52
    o.append(f'<rect x="{cx - 72}" y="{cy - 72}" width="144" height="144" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1.2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--bergamt)" stroke-width="3"/>')
    for k in range(8):
        import math
        a = k * math.pi / 4
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r * math.cos(a):.1f}" y2="{cy + r * math.sin(a):.1f}" stroke="var(--bergamt)" stroke-width="1.6"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="var(--bergamt)"/>')
    o.append(label(cx, cy + 92, "Das Kunstrad, 16 bis 36 Fuß", T + "kuenste/kunstrad/1", colour="bergamt"))
    o.append(label(cx, cy + 108, "‚an der Kraft gewinnet, was man an der Zeit verlieret‘", T + "kuenste/kunstrad/1", size=11.5, colour="bergamt"))
    # crank and field rods
    o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 34}" y2="{cy - 30}" stroke="var(--red)" stroke-width="3"/>')
    o.append(label(cx + 40, cy - 40, "krummer Zapfen (1565)", T + "kuenste/geschichte/5", size=11.5, anchor="start", colour="red"))
    o.append(f'<line x1="{cx + 34}" y1="{cy - 30}" x2="700" y2="{cy - 30}" stroke="var(--ink)" stroke-width="2.5" stroke-dasharray="14 4"/>')
    o.append(label(650, cy - 42, "Feldgestänge", T + "kuenste/geschichte/4", size=12))
    # shaft with pump sets
    sx = 720
    o.append(f'<rect x="{sx - 22}" y="150" width="44" height="430" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1.2"/>')
    o.append(f'<line x1="{sx}" y1="{cy - 30}" x2="{sx}" y2="560" stroke="var(--ink)" stroke-width="2.5"/>')
    for k, y in enumerate([300, 384, 460, 540]):
        o.append(f'<rect x="{sx - 18}" y="{y - 10}" width="36" height="20" fill="var(--wasser)" opacity="0.6"/>')
    o.append(label(sx + 32, 330, "Pumpensätze übereinander", T + "kuenste/geschichte/4", size=12, anchor="start"))
    o.append(label(sx + 32, 348, "bis ‚in die 200 Lachter‘", T + "kuenste/geschichte/4", size=11.5, anchor="start"))
    # adit
    o.append(f'<path d="M {sx - 22} 384 L 120 400 L 0 404" fill="none" stroke="var(--wasser)" stroke-width="7" opacity="0.8"/>')
    o.append(f'<line x1="{cx}" y1="{cy + 52}" x2="{cx - 4}" y2="392" stroke="var(--wasser)" stroke-width="3" stroke-dasharray="4 3"/>')
    o.append(label(250, 424, "Der Stollen führt alles Wasser zum Tal hinaus", T + "bergamt/stollen/3", colour="wasser"))
    o.append(label(250, 440, "(Erbstollen: ‚das Neundte‘, Modul ‚Das Bergamt‘)", T + "bergamt/stollen/3", size=11, colour="wasser"))
    # sump
    o.append(f'<rect x="{sx - 22}" y="560" width="44" height="20" fill="var(--wasser)" opacity="0.85"/>')
    o.append(label(sx - 40, 606, "Der Sumpf: ‚zu Sumpfe halten‘", T + "kuenste/geschichte/2", colour="wasser"))
    # failed alternatives
    o.append('<rect x="30" y="462" width="540" height="150" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="1.2"/>')
    o.append('<text x="46" y="486" font-size="13.5" font-weight="bold" fill="var(--ink)">Was man statt des Wassers versuchte</text>')
    rows = [("1549  zwölf Pferde im Göpel", "kuenste/geschichte/1"),
            ("1635  ein Schwungrad mit Gewichten: abgelehnt", "kuenste/mangel/3"),
            ("1658  ein Perpetuum mobile: ‚billig in Zweifel gezogen‘", "kuenste/mangel/4"),
            ("1670  die Maschine des Archimedes: drei Fragen, dann Schweigen", "kuenste/mangel/5"),
            ("1681  wieder Pferde: nicht versucht", "kuenste/mangel/4")]
    for k, (t, href) in enumerate(rows):
        o.append(label(46, 510 + k * 21, t, T + href, size=12.5, anchor="start"))
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
