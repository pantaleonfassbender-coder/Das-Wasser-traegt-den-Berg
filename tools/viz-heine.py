"""Draw assets/viz/heine.svg: Heine's way through the Carolina and the Dorothea in 1824,
as a schematic section after his own description (Reisebilder 1830, S. 117–124): down the
ladders of the Carolina beside the bucket rope, through a gallery to the Dorothea, up past
the miners leaving their shift, out into daylight. Every label links to its unit.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "heine.svg"
T = "#/text/heine/grube/"
W, H = 900, 640


def a(x, y, text, href, size=12, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def ladders(x, y0, y1, n, colour="ink"):
    """Zigzag ladders between small boards, from y0 down to y1."""
    o = []
    step = (y1 - y0) / n
    for k in range(n):
        ya, yb = y0 + k * step, y0 + (k + 1) * step
        xa, xb = (x - 10, x + 10) if k % 2 == 0 else (x + 10, x - 10)
        o.append(f'<line x1="{xa}" y1="{ya:.0f}" x2="{xb}" y2="{yb:.0f}" stroke="var(--{colour})" stroke-width="1.6"/>')
        o.append(f'<line x1="{x - 16}" y1="{yb:.0f}" x2="{x + 16}" y2="{yb:.0f}" stroke="var(--{colour})" stroke-width="2.4"/>')
    return o


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="he-t he-d" font-family="var(--serif)">',
         '<title id="he-t">Heines Fahrt, 1824</title>',
         '<desc id="he-d">Ein Schnitt, nicht maßstäblich. Links die Grube Carolina: von zwei schwärzlichen Gebäuden über Tage führt eine enge Öffnung hinab, Leitern von fünfzehn bis zwanzig Sprossen wechseln mit kleinen Brettern. Daneben läuft das Tonnenseil; am Seitenbrett ist vierzehn Tage zuvor ein Mensch abgestürzt. Unten Brausen, Wasser, Dunst, ein Bergmann klopft Erz aus der Wand; Heine wird das Atmen schwer, er steigt einige Dutzend Leitern wieder hinauf. Ein langer Gang führt nach rechts zur Grube Dorothea. Dort kommen Bergleute mit Grubenlichtern nach der Schicht herauf und grüßen „Glückauf!“. In einem Stollen stehen der Tisch und der Erzstuhl des Herzogs von Cambridge. Oben tritt Heine ins Sonnenlicht.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Heines Fahrt, 1824</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Nach Heines Beschreibung (gedruckt 1830), nicht maßstäblich. Er kam ‚bis wohin ich kam‘, nicht in die unterste Tiefe.</text>',
         '<defs><marker id="he-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--besucher)"/></marker></defs>']
    ground = 150
    o.append(f'<rect x="0" y="{ground}" width="{W}" height="{H - ground - 40}" fill="var(--ink2)" opacity="0.10"/>')
    o.append(f'<line x1="0" y1="{ground}" x2="{W}" y2="{ground}" stroke="var(--ink2)" stroke-width="1.5"/>')
    # buildings
    for x in (275, 330):
        o.append(f'<rect x="{x - 22}" y="{ground - 34}" width="44" height="34" fill="var(--ink)" opacity="0.65"/>')
        o.append(f'<path d="M {x - 26} {ground - 34} L {x} {ground - 52} L {x + 26} {ground - 34} Z" fill="var(--ink)" opacity="0.65"/>')
    o.append(a(250, ground - 30, "zwei schwärzliche Gebäude: umkleiden", T + "1", size=11.5, anchor="end"))
    # Carolina shaft
    cx = 330
    o.append(f'<rect x="{cx - 26}" y="{ground}" width="70" height="370" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1"/>')
    o += ladders(cx - 6, ground, ground + 300, 9)
    o.append(f'<line x1="{cx + 30}" y1="{ground}" x2="{cx + 30}" y2="{ground + 370}" stroke="var(--red)" stroke-width="2" stroke-dasharray="6 3"/>')
    o.append(f'<line x1="{cx + 16}" y1="{ground + 120}" x2="{cx + 40}" y2="{ground + 120}" stroke="var(--red)" stroke-width="3"/>')
    o.append(a(cx - 40, ground + 20, "Grube Carolina", T + "2", size=14, anchor="end", colour="ink", bold=True))
    o.append(a(cx - 40, ground + 40, "‚die schmutzigste und unerfreulichste‘", T + "2", size=11.5, anchor="end"))
    o.append(a(cx - 40, ground + 58, "Leitern von 15–20 Sprossen,", T + "2", size=11.5, anchor="end"))
    o.append(a(cx - 40, ground + 74, "dazwischen kleine Bretter", T + "2", size=11.5, anchor="end"))
    o.append(a(cx - 40, ground + 100, "‚kothig naß‘", T + "2", size=11.5, anchor="end"))
    o.append(a(cx + 52, ground + 102, "das Tonnenseil", T + "2", size=11.5, anchor="start", colour="red"))
    o.append(a(cx + 52, ground + 120, "das Seitenbrett: vor vierzehn Tagen", T + "2", size=12, anchor="start", colour="red", bold=True))
    o.append(a(cx + 52, ground + 136, "‚ein unvorsichtiger Mensch hinunter", T + "2", size=11.5, anchor="start", colour="red"))
    o.append(a(cx + 52, ground + 152, "gestürzt und leider den Hals gebrochen‘", T + "2", size=11.5, anchor="start", colour="red"))
    o.append(a(cx + 52, ground + 172, "der Steiger: ‚es sey gar nicht gefährlich‘", T + "2", size=11.5, anchor="start", colour="ink2"))
    # bottom of Carolina
    yb = ground + 300
    o.append(f'<rect x="{cx + 44}" y="{yb + 34}" width="90" height="22" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1"/>')
    o.append(a(cx + 144, yb + 44, "Stollen: ‚wo man das Erz wachsen sieht‘", T + "3", size=11.5, anchor="start", colour="wald"))
    o.append(a(cx + 144, yb + 60, "der Bergmann klopft mit dem Hammer", T + "3", size=11.5, anchor="start"))
    o.append(a(cx - 40, yb - 20, "Brausen, Wasser, ‚qualmig aufsteigende", T + "3", size=11.5, anchor="end", colour="wasser"))
    o.append(a(cx - 40, yb - 4, "Erddünste‘: ‚das Athmen wurde mir schwer‘", T + "3", size=11.5, anchor="end", colour="wasser"))
    # back up and gallery to Dorothea
    gy = ground + 230
    dx = 720
    o.append(f'<path d="M {cx + 6} {yb - 20} L {cx + 6} {gy + 8}" fill="none" stroke="var(--besucher)" stroke-width="2.4" marker-end="url(#he-a)"/>')
    o.append(a(cx - 40, gy - 30, "‚Nach Luft schnappend‘", T + "3", size=11.5, anchor="end", colour="besucher"))
    o.append(a(cx - 40, gy - 14, "einige Dutzend Leitern hinauf", T + "3", size=11.5, anchor="end", colour="besucher"))
    o.append(f'<rect x="{cx + 44}" y="{gy - 6}" width="{dx - cx - 70}" height="14" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1"/>')
    o.append(f'<line x1="{cx + 70}" y1="{gy + 1}" x2="{dx - 40}" y2="{gy + 1}" stroke="var(--besucher)" stroke-width="2.4" marker-end="url(#he-a)"/>')
    o.append(a((cx + dx) / 2 + 20, gy - 14, "ein schmaler, sehr langer Gang", T + "4", size=11.5, colour="besucher"))
    # Dorothea shaft
    o.append(f'<rect x="{dx - 30}" y="{ground}" width="60" height="300" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1"/>')
    o += ladders(dx, ground, ground + 280, 7)
    o.append(a(dx + 40, ground + 20, "Grube Dorothea", T + "4", size=14, anchor="start", bold=True))
    o.append(a(dx + 40, ground + 40, "‚luftiger und frischer‘,", T + "4", size=11.5, anchor="start"))
    o.append(a(dx + 40, ground + 56, "Leitern ‚länger und steiler‘", T + "4", size=11.5, anchor="start"))
    for k, y in enumerate((ground + 250, ground + 268, ground + 286)):
        o.append(f'<circle cx="{dx + (8 if k % 2 else -8)}" cy="{y}" r="5" fill="var(--gold)"/>')
    o.append(a(dx - 40, ground + 262, "Bergleute nach der Schicht", T + "4", size=12, anchor="end", colour="bergleute", bold=True))
    o.append(a(dx - 40, ground + 280, "mit Grubenlichtern: ‚Glückauf!‘", T + "4", size=11.5, anchor="end", colour="bergleute"))
    o.append(a(dx - 40, ground + 298, "‚etwas blassen‘ Gesichter", T + "4", size=11.5, anchor="end", colour="bergleute"))
    o.append(f'<path d="M {dx} {gy - 10} L {dx} {ground + 6}" fill="none" stroke="var(--besucher)" stroke-width="2.4" marker-end="url(#he-a)"/>')
    # duke's gallery
    sy = ground + 70
    o.append(f'<rect x="{dx - 170}" y="{sy - 8}" width="140" height="16" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1"/>')
    o.append(f'<rect x="{dx - 150}" y="{sy - 4}" width="60" height="5" fill="var(--bergamt)"/><rect x="{dx - 80}" y="{sy - 10}" width="10" height="14" fill="var(--bergamt)"/>')
    o.append(a(dx - 100, sy - 18, "Tisch und Erzstuhl des Herzogs von Cambridge", T + "5", size=11.5, colour="bergamt"))
    o.append(a(dx - 100, sy + 26, "‚sich gern würden todt schlagen lassen‘", T + "5", size=11.5, colour="bergamt"))
    # exit
    o.append(f'<circle cx="{dx}" cy="{ground - 40}" r="16" fill="var(--gold)" opacity="0.8"/>')
    o.append(a(dx - 24, ground - 36, "‚das Sonnenlicht strahlt‘ — Glück auf!", T + "5", size=12.5, anchor="end", colour="ink", bold=True))
    o.append('<text x="16" y="626" font-size="11.5" fill="var(--ink2)">Lage, Tiefe und Zahl der Leitern sind schematisch; Heine nennt keine Teufen. Rot: der Unfall, den der Steiger als Warnung erzählt.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
