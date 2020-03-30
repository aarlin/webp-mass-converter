from PIL import Image
import sys

def converter(file):
    im = Image.open(file).convert("RGB")
    im.save(file.split(".")[0] + ".png", "png")

if __name__ == "__main__":
    file = sys.argv[1]
    converter(file)
