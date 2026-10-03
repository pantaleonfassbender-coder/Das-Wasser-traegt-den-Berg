"""Draw assets/viz/aemter.svg: the offices of the mining administration after the
Bergordnung printed by Löhneyß (1617), from the prince down to the miners'
representatives. Every box links to the unit that names it.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "aemter.svg"
T = "#/text/bergamt/"
W, H = 900, 650


def box(x, y, w, h, title, line, c, href, bold=False):
    return (f'<a href="{href}"><g><rect x="{x - w / 2}" y="{y}" width="{w}" height="{h}" rx="8" fill="var(--panel)" stroke="var(--{c})" stroke-width="{2.4 if bold else 1.5}"/>'
            f'<text x="{x}" y="{y + 22}" text-anchor="middle" font-size="14.5" font-weight="{"bold" if bold else "normal"}" fill="var(--{c})">{escape(title)}</text>'
            + (f'<text x="{x}" y="{y + 40}" text-anchor="middle" font-size="11.5" fill="var(--ink2)">{escape(line)}</text>' if line else "")
            + '</g></a>')


def line(x1, y1, x2, y2, dashed=False):
    d = ' stroke-dasharray="6 4"' if dashed else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="var(--ink2)" stroke-width="1.4"{d}/>'


def column(x, y0, title, items, c, href):
    o = [f'<text x="{x}" y="{y0}" text-anchor="middle" font-size="13" font-style="italic" fill="var(--{c})">{escape(title)}</text>']
    for i, it in enumerate(items):
        o.append(f'<a href="{href}"><text x="{x}" y="{y0 + 22 + i * 19}" text-anchor="middle" font-size="12.5" fill="var(--ink)" text-decoration="underline">{escape(it)}</text></a>')
    return o


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="am-t am-d" font-family="var(--serif)">',
         '<title id="am-t">Das Bergamt nach der Bergordnung bei Löhneyß, 1617</title>',
         '<desc id="am-d">Oben der Landesfürst, darunter der Berghauptmann an seiner Statt. Unter ihm vier Spalten: die Rechnung (Zehntner, Gegenschreiber, Bergschreiber), die Gruben (Oberbergmeister, Bergmeister, Geschworene, Einfahrer, Steiger, Schichtmeister, Markscheider), die Pochwerke und die Hütten. Daneben die Gewerken, die zahlen, und ganz unten die Ältesten der Knappschaft und die Häuslinge. Eine gestrichelte Linie führt von allen zurück zum Fürsten: die Klage ‚mit Bescheidenheit‘.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Wer das Bergwerk regiert</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Nach der Bergordnung, die Löhneyß 1617 abdruckt. Die Bergleute selbst erscheinen nur als ‚Älteste und Jüngste der Knappschaft‘.</text>']
    o.append(line(450, 122, 450, 150))
    o.append(box(450, 70, 260, 52, "Der Landesfürst", "‚Wir‘: gibt die Ordnung, hört die Klagen", "bergamt", T + "aemter/3", True))
    o.append(box(450, 150, 300, 52, "Der Berghauptmann", "‚an des Landeßfürsten statt‘", "bergamt", T + "aemter/5", True))
    o.append(line(450, 202, 450, 226))
    o.append(line(130, 226, 770, 226))
    cols = [(130, "Die Rechnung", ["Zehntner", "Zehntgegenschreiber", "Bergschreiber", "Berggegenschreiber"], "bergamt", T + "aemter/3"),
            (340, "Die Gruben", ["Oberbergmeister", "Bergmeister", "Geschworene", "Einfahrer", "Steiger", "Schichtmeister", "Markscheider"], "wasser", T + "aemter/6"),
            (560, "Die Pochwerke", ["Oberpochsteiger", "Pochsteiger"], "wald", T + "aemter/3"),
            (770, "Die Hütten", ["Hüttenreiter", "Hüttenschreiber", "Probierer", "Silberbrenner", "Hüttenmeister", "Schmelzer", "Abtreiber", "Vorläufer", "Röstbrenner", "Hüttenwächter"], "wald", T + "aemter/3")]
    for x, title, items, c, href in cols:
        o.append(line(x, 226, x, 246))
        o += column(x, 262, title, items, c, href)
    o.append(f'<rect x="250" y="250" width="180" height="170" rx="10" fill="var(--wasser)" opacity="0.08"/>')
    o.append(f'<a href="{T}aemter/6"><text x="340" y="440" text-anchor="middle" font-size="11.5" fill="var(--wasser)" text-decoration="underline">verleiht Zechen, Stollen, ‚Wassergefäll‘</text></a>')
    o.append(f'<a href="{T}aemter/6"><text x="340" y="456" text-anchor="middle" font-size="11.5" fill="var(--wasser)" text-decoration="underline">Samstags der Anschnitt</text></a>')
    o.append(box(150, 480, 220, 52, "Die Gewerken", "zahlen Zubuße, erhalten Ausbeute", "bergamt", T + "aemter/4"))
    o.append(box(450, 540, 300, 52, "Älteste und Jüngste der Knappschaft", "Einwohner und Häuslinge", "bergleute", T + "aemter/3"))
    o.append(box(770, 480, 220, 52, "Der Eid", "‚mit allen Teuffeln verbant‘", "bergleute", T + "aemter/2"))
    o.append(f'<path d="M 300 592 L 14 592 L 14 96 L 320 96" fill="none" stroke="var(--ink2)" stroke-width="1.3" stroke-dasharray="6 4"/>')
    o.append(f'<a href="{T}aemter/4"><text x="22" y="630" font-size="12" fill="var(--ink2)" text-decoration="underline">Klage nur ‚mit Bescheidenheit‘ beim Fürsten</text></a>')
    o.append(f'<a href="{T}aemter/4"><text x="620" y="630" text-anchor="middle" font-size="12" fill="var(--ink2)" text-decoration="underline">Gehorsam ‚ohn widerrede‘</text></a>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
