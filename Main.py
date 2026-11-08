
from PIL import Image
from array import array
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE =  "./image_2.png"

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


def question4():
    img = Image.open(IMAGE).convert('RGB')
    w, h = img.size
    flou = Image.new('RGB', (w, h), 'white')

    for y in range(h):
        for x in range(w):
            somme_r, somme_g, somme_b = 0, 0, 0
            n = 0
            for yi in range(y - 5, y + 6):
                for xi in range(x - 5, x + 6):
                    if 0 <= xi < w and 0 <= yi < h:
                        r, g, b = img.getpixel((xi, yi))
                        somme_r += r
                        somme_g += g
                        somme_b += b
                        n += 1
            flou.putpixel((x, y), (somme_r // n, somme_g // n, somme_b // n))

    flou.save("./flou.png", "PNG")
    flou.show()



question1()
question2()
question3()
question4()
