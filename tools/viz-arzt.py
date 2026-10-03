"""Draw assets/viz/arzt.svg: the year of the Clausthal physician after Lentin (1789).
Left a wheel of the twelve months with what he says about weather, food and illness;
right a column of what work did to the body, from his case notes. Every label links
to the unit it comes from.
"""
import math
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "arzt.svg"
T = "#/text/arzt/"
W, H = 900, 640


def a(x, y, text, href, size=12, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def arc(cx, cy, r0, r1, m0, m1, colour, opacity):
    """Ring segment from month m0 to m1 (0 = January at top, clockwise)."""
    a0, a1 = (m0 / 12) * 2 * math.pi - math.pi / 2, (m1 / 12) * 2 * math.pi - math.pi / 2
    p = lambda r, t: (cx + r * math.cos(t), cy + r * math.sin(t))
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p(r1, a0), p(r1, a1), p(r0, a1), p(r0, a0)
    large = 1 if (m1 - m0) > 6 else 0
    return (f'<path d="M {x0:.1f} {y0:.1f} A {r1} {r1} 0 {large} 1 {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f} '
            f'A {r0} {r0} 0 {large} 0 {x3:.1f} {y3:.1f} Z" fill="var(--{colour})" opacity="{opacity}"/>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ar-t ar-d" font-family="var(--serif)">',
         '<title id="ar-t">Das Jahr des Bergarztes</title>',
         '<desc id="ar-d">Links ein Jahreskreis von Januar oben im Uhrzeigersinn. Schnee liegt von November bis Mai; Im Frühjahr Husten, Rheuma und der Ostwind vom Brocken. Erst im Juni Wildkräuter, im Juli Möhren, dann Erdbeeren, Kirschen, Heidelbeeren und Preiselbeeren; die Heidelbeerzeit gilt als die gesündeste. Die Herbstkrankheiten sind milder als die des Frühlings. Rechts eine Spalte: was die Arbeit dem Körper tat. Pochknaben mit Krämpfen; Husten und Schwindsucht durch die Beschäftigung; die Hüttenkatze, eine Bleivergiftung, die die Hände lähmt; Fallen, Stoßen, Quetschen unter Tage; ein Bergmann, auf den ein Stück Berg stürzte; die Frauen, die Lasten tragen und Fehlgeburten haben.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Das Jahr des Bergarztes</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Nach Lentin (1789–1808). Links, was Wetter und Essen der Stadt taten; rechts, was die Arbeit dem Körper tat.</text>']
    cx, cy, r = 330, 330, 140
    # snow Nov–May (months 10..12 and 0..4.5)
    o.append(arc(cx, cy, r - 26, r, 10, 12, "ink2", 0.25))
    o.append(arc(cx, cy, r - 26, r, 0, 4.6, "ink2", 0.25))
    # fresh food June–September
    o.append(arc(cx, cy, r - 26, r, 5, 9, "wald", 0.45))
    # spring illness Mar–May inner
    o.append(arc(cx, cy, r - 52, r - 28, 2.3, 5.3, "red", 0.35))
    # healthiest: Heidelbeerzeit Jul–Aug inner
    o.append(arc(cx, cy, r - 52, r - 28, 6.3, 8.3, "wald", 0.65))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--ink2)" stroke-width="1"/>')
    months = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
    for k, mname in enumerate(months):
        t = ((k + 0.5) / 12) * 2 * math.pi - math.pi / 2
        o.append(f'<text x="{cx + (r + 14) * math.cos(t):.0f}" y="{cy + (r + 14) * math.sin(t) + 4:.0f}" text-anchor="middle" font-size="11" fill="var(--ink2)">{mname}</text>')
    o.append(a(cx, cy - 8, "Clausthal", T + "stadt/1", size=14, bold=True))
    o.append(a(cx, cy + 10, "rund 7000–8000 Einwohner", T + "stadt/6", size=11))
    o.append(a(cx, cy + 26, "700–800 Frauen mehr", T + "stadt/6", size=11, colour="red"))
    # outer labels
    labels = [(16, 150, "Schnee bis April und Mai", "stadt/2", "start", "ink2"),
              (16, 300, "Dürre 1781:", "stadt/1", "start", "wasser"),
              (16, 316, "die Brunnen versiegen", "stadt/1", "start", "wasser"),
              (16, 470, "Herbst: Krankheiten", "stadt/2", "start", "ink"),
              (16, 486, "‚gelinder‘", "stadt/2", "start", "ink"),
              (cx + r + 26, 250, "Frühjahr: Husten,", "stadt/2", "start", "red"),
              (cx + r + 26, 266, "Rheuma, Ostwind", "stadt/3", "start", "red"),
              (cx + r + 26, 282, "vom Brocken", "stadt/3", "start", "red"),
              (cx + r + 20, 420, "Juni: Wildkräuter,", "stadt/2", "start", "wald"),
              (cx + r + 20, 436, "Juli: Möhren", "stadt/2", "start", "wald"),
              (cx, cy + r + 44, "Heidelbeerzeit, ‚die gesundeste im Jahre‘", "stadt/4", "middle", "wald")]
    for x, y, text, href, anchor, c in labels:
        o.append(a(x, y, text, T + href, size=11.5, anchor=anchor, colour=c))
    # right column
    x0 = 668
    o.append(f'<rect x="{x0 - 14}" y="76" width="236" height="520" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="1.2"/>')
    o.append(f'<text x="{x0}" y="102" font-size="14" font-weight="bold" fill="var(--ink)">Was die Arbeit dem Körper tat</text>')
    rows = [("Pochknaben", "Krämpfe, ‚Würmer‘, Ausschlag", "stadt/6", "bergleute"),
            ("‚Die Beschäftigung‘", "Husten, Tuberkel, Schwindsucht", "stadt/6", "bergleute"),
            ("Hüttenleute", "‚Hüttenkatze‘: Blei, Koliken", "arbeit/1", "red"),
            ("", "Lähmung der Hände, Muskelschwund", "arbeit/3", "red"),
            ("", "Kur in Gittelde, zurück auf die Hütte", "arbeit/3", "ink"),
            ("Bergleute", "‚Fallen, Stoßen, Quetschen‘", "arbeit/5", "red"),
            ("", "‚ein großes Stück Berg‘: tot", "arbeit/4", "red"),
            ("", "Quecksilbermittel: tot", "arbeit/6", "red"),
            ("Frauen", "Lasten tragen, Fehlgeburten", "stadt/5", "bergleute"),
            ("Alle Kranken", "‚freyen Arzneygebrauch‘", "arbeit/6", "wald")]
    y = 132
    for head, text, href, c in rows:
        if head:
            y += 8
            o.append(a(x0, y, head, T + href, size=12.5, anchor="start", colour="ink", bold=True))
            y += 18
        o.append(a(x0 + 12, y, text, T + href, size=12, anchor="start", colour=c))
        y += 22
    o.append(f'<text x="{x0}" y="582" font-size="10.5" fill="var(--ink2)">Zahlen der Verunglückten: keine.</text>')
    o.append('<text x="16" y="626" font-size="11.5" fill="var(--ink2)">Grau: Schnee; grün: frische Nahrung, dunkler die Heidelbeerzeit; rot: Frühjahrskrankheiten. Monatsgrenzen nach Lentins Worten, ungefähr.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
