import sys
from PIL import Image
CHARS = ' ░▒▓█'


def main():
    img = Image.open('input.png')
    x, y = img.size
    for c in _converter(img.resize((x, y // 2))):
        sys.stdout.buffer.write(c.encode('utf-8'))


def _converter(image):
    x, y = image.size
    pixels = image.load()
    for j in range(y):
        for i in range(x):
            r, g, b, *_ = pixels[i, j]  # *_ to ignore alpha if it is provided
            grayscale = round(0.2989 * r + 0.5870 * g + 0.1140 * b)
            yield CHARS[grayscale * len(CHARS) // 256]
        yield '\n'


if __name__ == '__main__':
    main()
