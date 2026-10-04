"""Draw assets/viz/system.svg: the system around 1866 after Dumreicher (1868). Left, the
depth of each adit below the Grube Caroline, to scale, with the years it was built; right,
the numbers of the whole system. Every label links to the unit it comes from.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "system.svg"
T = "#/text/system/"
W, H = 900, 660


def a(x, y, text, href, size=12, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="sy-t sy-d" font-family="var(--serif)">',
         '<title id="sy-t">Fünf Stollen übereinander</title>',
         '<desc id="sy-d">Links ein maßstäblicher Schnitt durch den Schacht der Grube Caroline bei Clausthal. Von oben nach unten liegen die Stollen, die dort Tiefe einbringen: Frankenscharner Stollen 38 Lachter, Mitte des 16. Jahrhunderts; Neunzehn-Lachter-Stollen etwa 60 Lachter, 1535 bis 1685; Dreizehn-Lachter-Stollen 73 Lachter, 1526 wieder aufgenommen, 1693 zum Burgstätter Zug; Tiefer Georg-Stollen 149 Lachter, 1777 bis 1799; Ernst-August-Stollen 204 Lachter, 1851 bis 1864; darunter die Tiefste Wasserstrecke in 324 Lachter, 118 Fuß unter dem Meeresspiegel, 1868 im Bau. Rechts die Zahlen des Systems: 67 Teiche mit 382 Millionen Kubikfuß, 106 246 Lachter Gräben, 193 Wasserräder und 3 Wassersäulenmaschinen mit 2869 Pferdestärken, 14 bis 16 Wochen ohne Regen.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Fünf Stollen übereinander</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Nach Dumreicher (1868). Teufe an der Grube Caroline in Lachtern, maßstäblich; ein Lachter ist rund zwei Meter.</text>']
    top, scale = 90, 1.55   # px per Lachter
    sx = 150
    y = lambda l: top + l * scale
    o.append(f'<line x1="40" y1="{top}" x2="420" y2="{top}" stroke="var(--ink2)" stroke-width="1.5"/>')
    o.append(a(40, top - 8, "Tage: Hängebank der Grube Caroline", T + "tiefe/3", size=11.5, anchor="start"))
    o.append(f'<rect x="{sx - 14}" y="{top}" width="28" height="{324 * scale:.0f}" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1.2"/>')
    adits = [(38, "Frankenscharner Stollen", "Mitte 16. Jh.", "tiefe/1", "ink2"),
             (60, "Neunzehn-Lachter-Stollen", "1535–1685", "tiefe/1", "ink2"),
             (73, "Dreizehn-Lachter-Stollen", "1526–1693", "tiefe/1", "ink2"),
             (149, "Tiefer Georg-Stollen", "26. 7. 1777 – 5. 9. 1799", "tiefe/3", "wasser"),
             (204, "Ernst-August-Stollen", "21. 7. 1851 – 22. 6. 1864", "tiefe/4", "wasser"),
             (324, "Tiefste Wasserstrecke", "1868 im Bau", "tiefe/2", "red")]
    for k, (l, name, yrs, href, c) in enumerate(adits):
        yy = y(l)
        dash = ' stroke-dasharray="6 4"' if c == "red" else ""
        o.append(f'<line x1="{sx + 14}" y1="{yy:.0f}" x2="440" y2="{yy:.0f}" stroke="var(--{c})" stroke-width="{4 if c == "wasser" else 2.4}"{dash}/>')
        o.append(f'<line x1="{sx - 14}" y1="{yy:.0f}" x2="{sx - 40}" y2="{yy:.0f}" stroke="var(--{c})" stroke-width="1"/>')
        o.append(f'<text x="{sx - 44}" y="{yy + 4:.0f}" text-anchor="end" font-size="11" fill="var(--ink2)">{l} L.</text>')
        dy = -6 if k not in (1,) else 12
        if k == 0:
            dy = -6
        if k == 2:
            dy = 14
        if k == 5:
            dy = -8
        o.append(a(sx + 22, yy + dy, f"{name}, {yrs}", T + href, size=12, anchor="start", colour=c if c != "ink2" else "ink", bold=c == "wasser"))
    o.append(a(sx + 22, y(262), "‚nimmermehr‘ ein tieferer", T + "tiefe/1", size=11.5, anchor="start", colour="ink2"))
    o.append(a(sx + 22, y(262) + 15, "zu Tage geleiteter Stollen", T + "tiefe/1", size=11.5, anchor="start", colour="ink2"))
    o.append(f'<path d="M {sx + 210} {y(149) + 26:.0f} q 20 0 40 0" stroke="var(--wasser)" stroke-width="0" />')
    o.append(a(sx + 22, y(204) + 20, "auf gleicher Höhe die Tiefe Wasserstrecke: Kähne,", T + "tiefe/2", size=11.5, anchor="start", colour="wasser"))
    o.append(a(sx + 22, y(204) + 35, "‚1300 Fuß unter der Stadt Clausthal‘", T + "tiefe/2", size=11.5, anchor="start", colour="wasser"))
    # right: the numbers
    x0 = 500
    o.append(f'<rect x="{x0}" y="80" width="384" height="520" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="1.2"/>')
    o.append(f'<text x="{x0 + 18}" y="108" font-size="14.5" font-weight="bold" fill="var(--ink)">Das System 1868</text>')
    rows = [("67 Teiche", "382 Millionen Kubikfuß, 936 Morgen", "anlage/1", "wasser"),
            ("27½ Meilen Gräben", "Sammel- und Aufschlaggräben, Röschen", "anlage/1", "wasser"),
            ("Dammgraben", "‚der eigentliche Lebensnerv‘, seit 1732", "anlage/5", "wasser"),
            ("14 bis 16 Wochen", "ohne Regen; 1857 der letzte Teich leer", "anlage/3", "red"),
            ("193 Wasserräder", "aus Fichtenholz, dazu 3 Wassersäulenmaschinen", "raeder/1", "bergamt"),
            ("2869 Pferdestärken", "brutto, Rad für Rad nachgerechnet", "raeder/2", "bergamt"),
            ("‚Rad Wasser‘", "die alte Einheit: ‚Gefühlssache‘", "anlage/4", "ink"),
            ("Fahrkunst 1833, Drahtseil 1834", "statt Leitern und Ketten", "fahrkunst/1", "bergleute"),
            ("Pochknabe mit 10, Bergmann mit 26", "8 Gutegroschen die Woche", "fahrkunst/3", "bergleute")]
    yy = 140
    for head, line, href, c in rows:
        o.append(a(x0 + 18, yy, head, T + href, size=13.5, anchor="start", colour=c, bold=True))
        o.append(a(x0 + 18, yy + 17, line, T + href, size=11.5, anchor="start"))
        yy += 50
    o.append(a(sx + 22, y(324) + 16, "118 Fuß unter dem Spiegel der Nordsee", T + "tiefe/2", size=11.5, anchor="start", colour="red"))
    o.append('<text x="16" y="640" font-size="11.5" fill="var(--ink2)">Frühe Jahreszahlen der oberen Stollen nach Dumreicher, der Calvör folgt; der Frankenscharner Stollen ist ‚nicht der älteste in seinem Angriffe‘.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
