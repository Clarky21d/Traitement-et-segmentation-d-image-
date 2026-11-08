# Mini Project: Image Processing and Segmentation with Python

University mini project for the *Programmation Python* course (2026-2027).
It uses the **Pillow** library to read, modify and analyze images pixel by pixel.

## Contents

| Question | Function | Description | Output file |
|----------|----------|-------------|-------------|
| 1 | `question1()` | Checks Pillow and turns green pixels into red ones | `green_to_red.png` |
| 2 | `question2()` | Creates the mirror image (pixel `(x, y)` goes to `(w-1-x, y)`) | `miroir.png` |
| 3 | `question3(seuil=200)` | Edge detection using `delta_energie` | `edges.png` |
| 4 | `question4()` | Blurs the image (average over an 11x11 window) | `flou.png` |

## Requirements

- Python 3
- Pillow

Check that Pillow is installed:

```python
from PIL import Image
```

If it is missing, install it with one of these commands:

```bash
pip install Pillow
pip3 install Pillow
conda install -c anaconda pillow
```

## Project structure

```
mini-projet/
├── Main.py        # the four questions
├── image.png      # source image (put your own image here)
└── README.md
```

The result images are created in the same folder as `Main.py`.

## Usage

1. Put the source image in the same folder as `Main.py`, named `image.png`
   (or change the `IMAGE` constant at the top of the script).
2. Run:

```bash
python Main.py
```

To run only one question, edit the `if __name__ == "__main__":` block at the end
of the file and keep only the call you want, for example `question3()`.

## How it works

### Question 1: green to red

Reads each pixel `(r, g, b)`. If `max(r, b) < g`, the pixel is considered green
and replaced by `(g, min(r, b), min(r, b))`. Other pixels are copied unchanged.

### Question 2: mirror image

Creates an empty image of the same size `(w, h)` and copies each pixel `(x, y)`
of the original to position `(w-1-x, y)`.

### Question 3: edge detection

The color difference between two pixels is:

```
delta_energie = (r1 - r2)² + (g1 - g2)² + (b1 - b2)²
```

For each pixel, the program compares it with its 8 neighbors. If
`delta_energie` is greater than the threshold (200 by default), the neighbor is
colored black in a white image called `edges`. Neighbor positions are checked
so they never go outside the image.

### Question 4: blur

For each pixel `(x, y)`, the program averages the R, G and B components of all
pixels `(xi, yi)` with `x-5 <= xi <= x+5` and `y-5 <= yi <= y+5`. The division
is an integer division (`//`), so the result is always an integer. On the
borders, only the neighbors that exist are counted.

## Notes

- **Speed:** `getpixel` and `putpixel` are slow. Question 4 reads 121 pixels per
  pixel, so it can take several minutes on large images (about 10 minutes for a
  2576x1449 image). Use a smaller image for quick tests.
- **`.show()` messages on Linux:** Pillow opens the image with the default
  program, which can print messages like `Broken pipe` in the terminal. They are
  harmless. The results are also saved as PNG files.
- **`FileNotFoundError`:** make sure the image name in `IMAGE` matches the real
  file name and extension (`image.png` is not `image.jpg`).
