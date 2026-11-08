
from PIL import Image
from array import array
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE_DIR, "image.png")

def question1():
    img = Image.open(IMAGE).convert('RGB')
    w, h = img.size
    image_green_to_red = Image.new('RGB', img.size, 'white')

    for i in range(h):
        for j in range(w):
            r, g, b = img.getpixel((j, i))

            if max(r, b) < g:
                m = min(r, b)
                image_green_to_red.putpixel((j, i), (g, m, m))
            else:
                image_green_to_red.putpixel((j, i), (r, g, b))

    image_green_to_red.save(
        os.path.join(BASE_DIR, "green_to_red.png"), "PNG"
    )
    image_green_to_red.show()


def question2():
    img1 = Image.open(IMAGE).convert('RGB')
    w, h = img1.size
    img2 = Image.new('RGB', (w, h), 'white')

    for y in range(h):
        for x in range(w):
            img2.putpixel(
                (w - 1 - x, y),
                img1.getpixel((x, y))
            )

    img2.save(os.path.join(BASE_DIR, "miroir.png"), "PNG")
    img2.show()


def delta_energie(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2

    return (
        (r1 - r2) ** 2
        + (g1 - g2) ** 2
        + (b1 - b2) ** 2
    )


def question3(seuil=200):
    img = Image.open(IMAGE).convert('RGB')
    w, h = img.size
    edges = Image.new('RGB', (w, h), 'white')

    voisinage = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),             (1, 0),
        (-1, 1),  (0, 1),   (1, 1)
    ]

    for y in range(h):
        for x in range(w):
            c = img.getpixel((x, y))

            for dx, dy in voisinage:
                x1, y1 = x + dx, y + dy

                if 0 <= x1 < w and 0 <= y1 < h:
                    if delta_energie(
                        c, img.getpixel((x1, y1))
                    ) > seuil:
                        edges.putpixel((x1, y1), (0, 0, 0))

    edges.save(os.path.join(BASE_DIR, "edges.png"), "PNG")
    edges.show()


def question4(rayon=5):
    img = Image.open(IMAGE).convert('RGB')
    w, h = img.size
    px = img.load()
    W = w + 1

    S = [
        array('q', [0]) * (W * (h + 1))
        for _ in range(3)
    ]

    for y in range(h):
        somme = [0, 0, 0]

        for x in range(w):
            p = px[x, y]

            for c in range(3):
                somme[c] += p[c]
                S[c][(y + 1) * W + x + 1] = (
                    S[c][y * W + x + 1] + somme[c]
                )

    res = Image.new('RGB', (w, h))
    out = res.load()

    for y in range(h):
        y0 = max(0, y - rayon)
        y1 = min(h, y + rayon + 1)

        for x in range(w):
            x0 = max(0, x - rayon)
            x1 = min(w, x + rayon + 1)

            n = (x1 - x0) * (y1 - y0)
            valeurs = []

            for c in range(3):
                s = S[c]

                total = (
                    s[y1 * W + x1]
                    - s[y0 * W + x1]
                    - s[y1 * W + x0]
                    + s[y0 * W + x0]
                )

                valeurs.append(total // n)

            out[x, y] = tuple(valeurs)

    res.save(os.path.join(BASE_DIR, "flou.png"), "PNG")
    res.show()


if __name__ == "__main__":
    question1()
    question2()
    question3()
    question4()
