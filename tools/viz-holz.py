"""Draw assets/viz/holz.svg: the way of the wood from the forest to the smelting works
after Calvör (1763), in four stations (forest, kiln, cart, works), with who measured at
each station and who paid when something was missing. Below, the yearly demand of two
works computed from Calvör's own figures. Every label links to the unit it comes from.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "holz.svg"
T = "#/text/holz/"
W, H = 900, 640


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def tree(x, y):
    return (f'<path d="M {x} {y - 34} L {x - 14} {y - 6} L {x - 6} {y - 6} L {x - 18} {y + 14} L {x + 18} {y + 14} L {x + 6} {y - 6} L {x + 14} {y - 6} Z" fill="var(--wald)" opacity="0.75"/>'
            f'<rect x="{x - 3}" y="{y + 14}" width="6" height="10" fill="var(--wald)"/>')


def kiln(x, y):
    return (f'<path d="M {x - 34} {y + 22} Q {x} {y - 34} {x + 34} {y + 22} Z" fill="var(--ink2)" opacity="0.55"/>'
            f'<path d="M {x - 2} {y - 10} q -8 -12 0 -22 q 8 -10 0 -20" fill="none" stroke="var(--ink2)" stroke-width="2" opacity="0.7"/>')


def cart(x, y):
    return (f'<path d="M {x - 30} {y - 12} L {x + 30} {y - 12} L {x + 22} {y + 10} L {x - 22} {y + 10} Z" fill="var(--panel)" stroke="var(--ink)" stroke-width="1.6"/>'
            f'<circle cx="{x}" cy="{y + 18}" r="9" fill="none" stroke="var(--ink)" stroke-width="1.6"/>'
            f'<path d="M {x - 22} {y - 12} q 22 -16 44 0" fill="var(--ink)" opacity="0.6"/>')


def works(x, y):
    return (f'<rect x="{x - 32}" y="{y - 8}" width="64" height="32" fill="var(--panel)" stroke="var(--bergamt)" stroke-width="1.6"/>'
            f'<path d="M {x - 38} {y - 8} L {x} {y - 30} L {x + 38} {y - 8} Z" fill="var(--bergamt)" opacity="0.5"/>'
            f'<rect x="{x + 14}" y="{y - 46}" width="10" height="30" fill="var(--bergamt)" opacity="0.7"/>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ho-t ho-d" font-family="var(--serif)">',
         '<title id="ho-t">Vom Baum zur Hütte</title>',
         '<desc id="ho-d">Vier Stationen von links nach rechts. Im Wald schlagen Holzhauer das Stammholz 5 Fuß lang und legen es in Malter von 4 mal 4 Fuß; der Revierförster misst es mit dem Malterstock. Im Meiler verkohlt der Köhler das Holz in 10 bis 14 Tagen; ein großer Meiler gibt 35 bis 40 Karren, für einen Karren Tannenkohlen braucht es 2¼ bis 3 Malter. Der Fuhrmann fährt die Kohlen in Karren zu 10 Maß, ein Maß wiegt 56 bis 64 Pfund. An der Hütte misst der Hüttenwächter Karren und Kohlen nach; was fehlt, wird Fuhrmann und Köhler vom Lohn abgezogen. Unten: Die Hütten in Clausthal und Altenau brauchen 9000 und 7000 Karren im Jahr, nach Calvörs Zahlen also rund 36 000 bis 48 000 Malter Holz.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Vom Baum zur Hütte</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Nach Calvör (1763). An jeder Station misst ein Beamter; wenn etwas fehlt, zahlt ein Arbeiter.</text>',
         '<defs><marker id="ho-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--ink2)"/></marker></defs>']
    xs = [115, 335, 560, 785]
    for k in range(3):
        o.append(f'<line x1="{xs[k] + 70}" y1="140" x2="{xs[k + 1] - 70}" y2="140" stroke="var(--ink2)" stroke-width="2" marker-end="url(#ho-a)"/>')
    stations = [
        ("Der Wald", "wald", tree, [("Stammholz 5 Fuß lang,", "koehler/2"), ("im Malter 4 × 4 Fuß", "koehler/2"), ("auch die Stubben", "huette/4")],
         ("Revierförster", "Malterstock, ‚abnehmen‘", "koehler/2"), ("Holzhauer", "8 Mgr. 4 Pf. je Malter", "koehler/2")),
        ("Der Meiler", "ink2", kiln, [("10 bis 14 Tage gar,", "koehler/8"), ("Tag und Nacht bewacht", "koehler/8"), ("35–40 Karren je großem Meiler", "koehler/4")],
         ("Förster weist das Holz an", "der Köhler nimmt, was er bekommt", "koehler/3"), ("Köhler", "2¼ bis 3 Malter je Karren", "koehler/2")),
        ("Der Karren", "ink", cart, [("10 Maß Tannenkohlen,", "huette/1"), ("9 Maß Buchenkohlen", "huette/1"), ("1 Maß: 56–64 Pfund", "huette/1")],
         ("Holzmalter", "Röstholz im Malterbock", "huette/3"), ("Fuhrmann", "‚am Lohne abgezogen‘", "huette/3")),
        ("Die Hütte", "bergamt", works, [("Clausthal: 9000 Karren", "huette/2"), ("Altenau: 7000 Karren", "huette/2"), ("im Jahr", "huette/2")],
         ("Hüttenwächter", "Stab und Kohlenmaß", "huette/2"), ("Fuhrmann und Köhler", "‚Krimpmaaße‘ vom Lohn", "huette/2")),
    ]
    for x, (name, c, icon, lines, meas, pays) in zip(xs, stations):
        o.append(f'<rect x="{x - 100}" y="70" width="200" height="404" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="1.2"/>')
        o.append(icon(x, 140))
        o.append(a(x, 196, name, T + lines[0][1], size=15, colour="wald" if c == "wald" else ("bergamt" if c == "bergamt" else "ink"), bold=True))
        for k, (t, href) in enumerate(lines):
            o.append(a(x, 222 + k * 19, t, T + href, size=12))
        o.append(f'<line x1="{x - 80}" y1="290" x2="{x + 80}" y2="290" stroke="var(--line)"/>')
        o.append(f'<text x="{x}" y="312" text-anchor="middle" font-size="11.5" font-style="italic" fill="var(--ink2)">wer misst</text>')
        o.append(a(x, 334, meas[0], T + meas[2], size=13, colour="bergamt", bold=True))
        o.append(a(x, 352, meas[1], T + meas[2], size=11.5))
        o.append(f'<text x="{x}" y="390" text-anchor="middle" font-size="11.5" font-style="italic" fill="var(--ink2)">wer arbeitet und haftet</text>')
        o.append(a(x, 412, pays[0], T + pays[2], size=13, colour="red", bold=True))
        o.append(a(x, 430, pays[1], T + pays[2], size=11.5))
    # yearly demand
    y0 = 520
    o.append(f'<text x="16" y="{y0}" font-size="14" font-weight="bold" fill="var(--ink)">Ein Jahr, zwei Hütten</text>')
    scale = 760 / 48000
    o.append(f'<rect x="120" y="{y0 + 14}" width="{9000 * scale:.0f}" height="20" fill="var(--bergamt)" opacity="0.7"/>')
    o.append(f'<rect x="{120 + 9000 * scale:.0f}" y="{y0 + 14}" width="{7000 * scale:.0f}" height="20" fill="var(--bergamt)" opacity="0.4"/>')
    o.append(a(16, y0 + 29, "16 000 Karren", T + "huette/2", size=12.5, anchor="start"))
    o.append(f'<rect x="120" y="{y0 + 48}" width="{36000 * scale:.0f}" height="20" fill="var(--wald)" opacity="0.7"/>')
    o.append(f'<rect x="{120 + 36000 * scale:.0f}" y="{y0 + 48}" width="{12000 * scale:.0f}" height="20" fill="var(--wald)" opacity="0.3"/>')
    o.append(a(16, y0 + 63, "36–48 000 Malter", T + "koehler/2", size=12.5, anchor="start"))
    o.append(f'<text x="{120 + 9000 * scale + 7000 * scale + 8:.0f}" y="{y0 + 29}" font-size="11.5" fill="var(--ink2)">Clausthal 9000 + Altenau 7000 (Calvör)</text>')
    o.append(f'<text x="16" y="{y0 + 96}" font-size="11.5" fill="var(--ink2)">Untere Leiste von uns gerechnet: 16 000 Karren × 2¼ bis 3 Malter Stammholz je Karren. Ohne Röstholz und ohne das Holz in den Gruben.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
