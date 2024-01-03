from PIL import Image, ImageOps
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].casefold().endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid input")
    x = sys.argv[1].casefold().split(".")
    y = sys.argv[2].casefold().split(".")
    if y[-1] != x[-1]:
        sys.exit("Input and output have different extensions")
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Could not read ", sys.argv[1])

    im = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    im = ImageOps.fit(
        im,
        size=shirt.size,
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )
    shirt = ImageOps.fit(
        shirt,
        size=shirt.size,
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )

    im.paste(shirt, box=None, mask=shirt)
    im.save(sys.argv[2], format=None)


if __name__ == "__main__":
    main()
