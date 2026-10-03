"""Download and scale plate images into assets/plates/<id>.jpg and <id>_t.jpg.

    python tools/make-plates.py            # all plates listed below
    python tools/make-plates.py roswitha1501

Commons files are fetched as 1400-pixel renderings via the API; Internet
Archive page images are fetched directly and cropped (box in per mille).
"""
import io
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "assets" / "plates"
UA = {"User-Agent": "Mozilla/5.0 (research; Das Wasser traegt den Berg; pantaleonfassbender@gmail.com)"}

PLATES = {
    # Modul 1
    "calvoer_s215": ("ia", "https://archive.org/download/10705761bsb/page/n234_w1400.jpg", (40, 40, 980, 458)),
    "calvoer_s219": ("ia", "https://archive.org/download/10705761bsb/page/n238_w1400.jpg", (40, 280, 980, 640)),
    "merian_clausthal": ("commons", "File:Merian Clausthal.JPG", (0, 0, 1000, 495)),
    "merian_zellerfeld": ("commons", "File:Zellerfeld (Merian).jpg", None),
    # Modul 2 (e-rara, ETH-Bibliothek, Public Domain Mark)
    "loehneyss_titel": ("ia", "https://www.e-rara.ch/i3f/v20/4845037/full/1400,/0/default.jpg", None),
    "loehneyss_s193": ("ia", "https://www.e-rara.ch/i3f/v20/4845307/full/1400,/0/default.jpg", (60, 640, 1000, 880)),
    # Modul 3 (Calvör 1763, IA 10705759bsb)
    "calvoer_s35": ("ia", "https://archive.org/download/10705759bsb/page/n62_w1400.jpg", (40, 585, 1000, 830)),
    "calvoer_s97": ("ia", "https://archive.org/download/10705759bsb/page/n124_w1400.jpg", (40, 600, 1000, 905)),
    "calvoer_tab6": ("ia", "https://archive.org/download/10705759bsb/page/n244_w1400.jpg", None),
    "loehneyss_s233": ("ia", "https://www.e-rara.ch/i3f/v20/4845347/full/1400,/0/default.jpg", (60, 545, 1000, 925)),
}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()


def commons_url(title):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "imageinfo",
                                "iiprop": "url", "iiurlwidth": 1400, "format": "json"})
    data = json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))
    page = next(iter(data["query"]["pages"].values()))
    return page["imageinfo"][0]["thumburl"]


def make(pid):
    kind, src, box = PLATES[pid]
    im = Image.open(io.BytesIO(get(commons_url(src) if kind == "commons" else src))).convert("RGB")
    if box:
        W, H = im.size
        im = im.crop((W * box[0] // 1000, H * box[1] // 1000, W * box[2] // 1000, H * box[3] // 1000))
    big = im.copy()
    big.thumbnail((1400, 1600))
    big.save(DEST / f"{pid}.jpg", quality=85, optimize=True)
    t = im.copy()
    t.thumbnail((360, 480))
    t.save(DEST / f"{pid}_t.jpg", quality=82, optimize=True)
    print(pid, big.size, t.size)


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    for pid in sys.argv[1:] or PLATES:
        make(pid)
