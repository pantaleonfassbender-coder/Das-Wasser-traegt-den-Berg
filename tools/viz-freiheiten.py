"""Draw assets/viz/freiheiten.svg: the three mining charters of 1521, 1532 and 1554
side by side, row by row. Every cell links to the unit that documents it.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "freiheiten.svg"
T = "#/text/freiheit/"
W, X0, CW, RH, Y0 = 900, 150, 245, 64, 112
COLS = [("1521", "Hohnstein", "hohnstein"), ("1532", "Herzog Heinrich", "heinrich"), ("1554", "Clausthal", "clausthal")]
# (label, colour, [(text line 1, line 2, unit) per column])
ROWS = [
    ("Holz", "wald", [("frei aus allen Wäldern,", "‚nun und zu ewigen Zeiten‘", "hohnstein/1"),
                      ("Bauholz frei, aber", "‚nach Anweisung des Försters‘", "heinrich/3"),
                      ("nach Anweisung der Förster;", "Kohlholz nach 5 Jahren Waldzins", "clausthal/1")]),
    ("Wasser", "wasser", [("zwei Bäche zum Fischen,", "alle anderen zu meiden", "hohnstein/5"),
                          ("ein Erbstollen nimmt die", "‚Wasser-Noht‘; Wasser offen", "heinrich/1"),
                          ("Zellbach und Innerste ‚zum", "Bergwercke nothdürfftig‘", "clausthal/5")]),
    ("Zehnt", "bergamt", [("3 Jahre nur der", "fünfzehnte statt zehnte Teil", "hohnstein/3"),
                          ("3 Jahre frei", "", "heinrich/4"),
                          ("5 Jahre frei", "", "clausthal/2")]),
    ("Silber", "bergamt", [("5 Jahre freier Verkauf,", "dann an den Zehnten", "hohnstein/3"),
                           ("an die Kammer des Herzogs,", "8 Gulden 1 Ort die Mark", "heinrich/4"),
                           ("an die Zehntkammer,", "12, nach 2 Jahren 10 Gulden", "clausthal/4")]),
    ("Hütten", "wald", [("frei zu bauen; der Graf", "verzichtet auf Hütten", "hohnstein/5"),
                        ("Hütten und Pochwerke", "frei wie Wege und Wasser", "heinrich/2"),
                        ("die Hütte des Herzogs;", "nur im Land schmelzen", "clausthal/3")]),
    ("Regiment", "bergamt", [("Rat und Richter gewählt,", "vom Grafen bestätigt", "hohnstein/4"),
                             ("Amtleute des Herzogs nach", "der Joachimsthaler Ordnung", "heinrich/4"),
                             ("Berghauptmann, Bergmeister", "‚von unserntwegen‘", "clausthal/3")]),
    ("Schulden", "bergleute", [("keine Klage um Schulden", "von anderswo; freier Abzug", "hohnstein/2"),
                               ("freier Abzug, wenn die", "Schulden vor Ort bezahlt sind", "heinrich/2"),
                               ("freier Zu- und Abzug", "(Art. 17, wie 1532)", "clausthal/5")]),
]


def main():
    H = Y0 + len(ROWS) * RH + 30
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fr-t fr-d" font-family="var(--serif)">',
         '<title id="fr-t">Drei Bergfreiheiten im Vergleich</title>',
         '<desc id="fr-d">Eine Tabelle: Zeilen Holz, Wasser, Zehnt, Silber, Hütten, Regiment, Schulden; Spalten Hohnstein 1521, Herzog Heinrich 1532, Clausthal 1554. Von links nach rechts wird das Holz knapper, das Silber und die Hütten kommen unter den Landesherrn, und das Wasser wird vom Fischwasser zum Recht des Bergwerks.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Was die Bergfreiheiten versprachen</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Von 1521 nach 1554: das Holz nach Anweisung, das Silber in die Kammer, das Bergamt vom Landesherrn, und das Wasser wird ein Recht des Bergwerks.</text>']
    for i, (yr, name, sec) in enumerate(COLS):
        x = X0 + i * CW
        o.append(f'<a href="{T}{sec}/1"><text x="{x + CW / 2}" y="{Y0 - 26}" text-anchor="middle" font-size="16" font-weight="bold" fill="var(--bergamt)" text-decoration="underline">{yr}</text></a>')
        o.append(f'<text x="{x + CW / 2}" y="{Y0 - 8}" text-anchor="middle" font-size="12.5" fill="var(--ink2)">{escape(name)}</text>')
    for r, (label, c, cells) in enumerate(ROWS):
        y = Y0 + r * RH
        o.append(f'<rect x="10" y="{y + 3}" width="{W - 20}" height="{RH - 6}" rx="8" fill="var(--{c})" opacity="{0.12 if label == "Wasser" else 0.05}"/>')
        o.append(f'<text x="22" y="{y + RH / 2 + 5}" font-size="14.5" font-weight="bold" fill="var(--{c})">{escape(label)}</text>')
        for i, (a, b, unit) in enumerate(cells):
            x = X0 + i * CW + CW / 2
            sec, n = unit.split("/")
            o.append(f'<a href="{T}{sec}/{n}"><text x="{x}" y="{y + (RH / 2 - 3 if b else RH / 2 + 5)}" text-anchor="middle" font-size="12.5" fill="var(--ink)" text-decoration="underline">{escape(a)}</text>'
                     + (f'<text x="{x}" y="{y + RH / 2 + 14}" text-anchor="middle" font-size="12.5" fill="var(--ink)" text-decoration="underline">{escape(b)}</text>' if b else "") + '</a>')
        if r:
            o.append(f'<line x1="{X0 - 10}" y1="{y}" x2="{W - 14}" y2="{y}" stroke="var(--line)" stroke-width="1"/>')
    for i in range(1, 3):
        x = X0 + i * CW
        o.append(f'<line x1="{x}" y1="{Y0 + 6}" x2="{x}" y2="{Y0 + len(ROWS) * RH - 6}" stroke="var(--line)" stroke-width="1"/>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
