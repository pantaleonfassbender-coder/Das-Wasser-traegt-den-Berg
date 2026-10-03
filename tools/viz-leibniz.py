"""Draw assets/viz/leibniz.svg: two machines after Calvör (1763). Left the plan Leibniz
explained in July 1680 (the wind pumps the spent water back up, the wheel drives the
pumps as before), which was never built; right the windmill the Bergamt demanded,
which pumped directly and broke. Below a timeline of the trial 1678–1686.
Every label links to the unit that documents it.
"""
import math
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "leibniz.svg"
T = "#/text/leibniz/"
W, H = 900, 680


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def mill(x, y, r=34, colour="besucher", broken=False):
    """A post mill: a body on a trestle with four sails around the hub at (x, y)."""
    o = [f'<rect x="{x - 14}" y="{y - 6}" width="28" height="36" fill="var(--panel)" stroke="var(--{colour})" stroke-width="1.6"/>',
         f'<path d="M {x - 16} {y + 52} L {x} {y + 30} L {x + 16} {y + 52}" fill="none" stroke="var(--{colour})" stroke-width="1.6"/>']
    for k in range(4):
        ang = math.radians(25 + 90 * k)
        if broken and k == 1:
            ang += math.radians(30)
        x2, y2 = x + r * math.cos(ang), y + r * math.sin(ang)
        o.append(f'<line x1="{x}" y1="{y}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="var(--{colour})" stroke-width="3"/>')
    o.append(f'<circle cx="{x}" cy="{y}" r="4" fill="var(--{colour})"/>')
    return o


def wheel(cx, cy, r=26):
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--bergamt)" stroke-width="2.6"/>']
    for k in range(6):
        ang = k * math.pi / 3
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r * math.cos(ang):.1f}" y2="{cy + r * math.sin(ang):.1f}" stroke="var(--bergamt)" stroke-width="1.4"/>')
    return o


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="lz-t lz-d" font-family="var(--serif)">',
         '<title id="lz-t">Zwei Windmühlen: die gemeinte und die gebaute</title>',
         '<desc id="lz-d">Links der Plan, den Leibniz im Juli 1680 erklärte: Ein oberer Behälter gibt Wasser auf ein Kunstrad, das wie bisher die Pumpen in der Grube treibt; das abgefallene Wasser sammelt sich in einem unteren Behälter, und Windmühlen heben es wieder in den oberen. Dieser Plan wurde nie gebaut. Rechts die Windmühle, die das Bergamt verlangte und die 1681 bis 1686 auf der Grube Catharina stand: Sie pumpte unmittelbar über ein Gestänge aus dem Schacht, hob im März 1682 eine Stunde lang 11 Sätze und 1683 zwei bis drei Tage 14 Sätze, stand bei schwachem Wind still und brach bei starkem. Unten eine Zeitleiste von 1678 bis 1686: Harzingks Modell, der Vertrag vom 20. September 1679, Leibniz’ Erklärung im Juli 1680, die erste Probe 1681, die siebzehn Zweifel 1682, der Sturm 1683, die Denkschrift und der Beschluss des Hofes im April 1685, der Abbruch 1686.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Zwei Windmühlen: die gemeinte und die gebaute</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Schema nach Calvör (1763), nicht maßstäblich. Der Wind sollte speichern, nicht pumpen; gebaut wurde die Mühle, die pumpte.</text>',
         '<defs><marker id="lz-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--wasser)"/></marker></defs>']
    # panels
    for x0, title, href, c in [(16, "Was Leibniz meinte (Juli 1680)", T + "probe/1", "besucher"),
                               (462, "Was gebaut wurde (Catharina, 1681–1686)", T + "probe/3", "bergamt")]:
        o.append(f'<rect x="{x0}" y="66" width="422" height="352" rx="10" fill="var(--panel)" stroke="var(--line)" stroke-width="1.2"/>')
        o.append(a(x0 + 211, 90, title, href, size=14, colour=c, bold=True))
    # left: storage cycle
    o.append('<rect x="60" y="130" width="120" height="34" rx="6" fill="var(--wasser)" opacity="0.5"/>')
    o.append(a(120, 124, "oberer Behälter", T + "probe/1", size=12, colour="wasser"))
    o += wheel(120, 220)
    o.append('<path d="M 150 164 L 150 190" stroke="var(--wasser)" stroke-width="4" marker-end="url(#lz-a)"/>')
    o.append(a(36, 222, "Kunstrad", T + "probe/1", size=11.5, anchor="start", colour="bergamt"))
    o.append(a(140, 404, "die Pumpen wie bisher", T + "probe/1", size=11.5, anchor="start", colour="bergamt"))
    o.append('<line x1="120" y1="246" x2="120" y2="390" stroke="var(--ink)" stroke-width="2.2" stroke-dasharray="10 4"/>')
    for y in (300, 340, 380):
        o.append(f'<rect x="108" y="{y - 8}" width="24" height="16" fill="var(--wasser)" opacity="0.55"/>')
    o.append('<rect x="200" y="300" width="130" height="34" rx="6" fill="var(--wasser)" opacity="0.5"/>')
    o.append(a(265, 352, "unterer Behälter", T + "probe/1", size=12, colour="wasser"))
    o.append('<path d="M 146 236 C 180 270, 200 290, 222 300" fill="none" stroke="var(--wasser)" stroke-width="3" marker-end="url(#lz-a)"/>')
    o += mill(350, 170)
    o.append('<path d="M 320 300 C 330 250, 300 190, 186 146" fill="none" stroke="var(--wasser)" stroke-width="3" stroke-dasharray="7 4" marker-end="url(#lz-a)"/>')
    o.append(a(352, 116, "der Wind hebt es zurück,", T + "probe/1", size=12, colour="besucher"))
    o.append(a(352, 131, "‚oft in einer Stunde‘", T + "probe/1", size=12, colour="besucher"))
    o.append(a(330, 370, "nie gebaut", T + "probe/7", size=14, colour="red", bold=True))
    o.append(a(330, 388, "die Kommunion widersprach", T + "probe/7", size=11.5, colour="red"))
    # right: direct pumping mill
    sx = 640
    o.append('<path d="M 480 200 L 860 200" stroke="var(--ink2)" stroke-width="1.4"/>')
    o += mill(sx, 140, colour="bergamt", broken=True)
    o.append(f'<rect x="{sx - 16}" y="200" width="32" height="200" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1.2"/>')
    o.append(f'<line x1="{sx}" y1="170" x2="{sx}" y2="392" stroke="var(--ink)" stroke-width="2.2" stroke-dasharray="10 4"/>')
    for y in range(226, 396, 22):
        o.append(f'<rect x="{sx - 11}" y="{y - 6}" width="22" height="12" fill="var(--wasser)" opacity="0.55"/>')
    o.append(a(sx + 30, 236, "März 1682: 11 Sätze, eine Stunde", T + "probe/3", size=12, anchor="start"))
    o.append(a(sx + 30, 256, "1683: 14 Sätze, zwei bis drei Tage", T + "probe/5", size=12, anchor="start"))
    o.append(a(sx + 30, 276, "‚nicht aber auf den Stollen‘", T + "probe/5", size=11.5, anchor="start"))
    o.append(a(sx + 30, 316, "schwacher Wind: sie steht", T + "probe/5", size=12, anchor="start", colour="ink2"))
    o.append(a(sx + 30, 336, "starker Wind: sie bricht", T + "probe/5", size=12, anchor="start", colour="red"))
    o.append(a(sx + 30, 356, "Einbrüche in die Mühle", T + "probe/6", size=12, anchor="start", colour="red"))
    o.append(a(sx - 30, 236, "unmittelbar", T + "probe/2", size=12, anchor="end", colour="bergamt"))
    o.append(a(sx - 30, 252, "aus dem Schacht", T + "probe/2", size=12, anchor="end", colour="bergamt"))
    o.append(a(sx - 30, 290, "‚ein neuer Vortrag‘:", T + "probe/2", size=11.5, anchor="end"))
    o.append(a(sx - 30, 305, "das Bergamt besteht", T + "probe/2", size=11.5, anchor="end"))
    o.append(a(sx - 30, 320, "auf dieser Mühle", T + "probe/2", size=11.5, anchor="end"))
    o.append(a(sx + 120, 130, "1683 dreht ein Sturm", T + "probe/5", size=12, colour="red"))
    o.append(a(sx + 120, 146, "das ganze Dach um", T + "probe/5", size=12, colour="red"))
    # timeline
    y0, x0, x1 = 530, 60, 860
    lo, hi = 1678, 1687
    X = lambda yr: x0 + (yr - lo) / (hi - lo) * (x1 - x0)
    o.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="var(--ink2)" stroke-width="1.5"/>')
    for yr in range(lo, hi):
        o.append(f'<line x1="{X(yr):.0f}" y1="{y0 - 4}" x2="{X(yr):.0f}" y2="{y0 + 4}" stroke="var(--ink2)"/>')
        o.append(f'<text x="{X(yr):.0f}" y="{y0 + 20}" text-anchor="middle" font-size="11" fill="var(--ink2)">{yr}</text>')
    events = [(1678.25, "Harzingks Modell", "vorschlag/1", "ink", -1),
              (1679.72, "Vertrag, 1200 Taler", "vorschlag/5", "besucher", 1),
              (1680.53, "Leibniz erklärt sich", "probe/1", "besucher", -1),
              (1681.85, "erste Probe, Klappen fliegen", "probe/3", "red", 1),
              (1682.3, "17 Zweifel", "probe/4", "bergamt", -2),
              (1683.5, "Sturm; Tagebuch", "probe/5", "red", -1),
              (1685.3, "Denkschrift; Hof stoppt", "leibniz/3", "besucher", 1),
              (1686.4, "Abbruch", "probe/7", "red", -1)]
    for yr, label, href, c, side in events:
        x = X(yr)
        o.append(f'<circle cx="{x:.0f}" cy="{y0}" r="6" fill="var(--{c})"/>')
        ly = {-1: y0 - 26, -2: y0 - 52, 1: y0 + 46, 2: y0 + 68}[side]
        o.append(f'<line x1="{x:.0f}" y1="{y0 + (-8 if side < 0 else 8)}" x2="{x:.0f}" y2="{ly + (6 if side < 0 else -14)}" stroke="var(--{c})" stroke-width="1"/>')
        o.append(a(x, ly, label, T + href, size=12, colour="red" if c == "red" else "ink"))
    o.append('<text x="60" y="652" font-size="12" fill="var(--ink2)">Rot: Brüche und Abbruch. Die Probe dauerte acht Jahre; Calvör las dafür ‚fast ½ Rieß Papier‘ Akten.</text>')
    o.append("</svg>")
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


main()
