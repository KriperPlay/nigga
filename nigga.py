from PIL import Image
import sys
from pathlib import Path
import matplotlib.pyplot as plt

def rgb_to_hex(r, g, b):
    return '{:02x}{:02x}{:02x} '.format(r, g, b)

def hex_to_rgb(hexa):
    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

def png_to_nigga(img):
    img1 = Image.open(img).convert('L')
    width, height = img1.size

    file1 = open(f"{Path(img).stem}.nigga", 'w')

    for y in range(height):
        for x in range(width):
            gray_value = img1.getpixel((x, y))
            file1.write(rgb_to_hex(gray_value, gray_value, gray_value))
        file1.write('\n')
    
    file1.close()

def nigga_view(img):
    if Path(img).suffix == ".nigga":
        x1 = 0
        y1 = 0
        fil = open(img,'r')
        for i in fil:
            y1+=1
            x1 = i.split()
        fil.close()
        img1 = Image.new('RGB', (len(x1),y1))
        file = open(img,'r')
        for y,lines in enumerate(file):
            line = lines.split()
            for x,q in enumerate(line):
                img1.putpixel((x,y), hex_to_rgb(q))

        plt.imshow(img1)
        plt.title(img)
        plt.show()
    else:
        print(f"{img} not .nigga")

if __name__ == "__main__":
    try:
        mode = sys.argv[1]
        if mode == "-c":
            png_to_nigga(sys.argv[2])
        if mode == "-v":
            nigga_view(sys.argv[2])
    except IndexError:
        print("You forgot a argument!")
