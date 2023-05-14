from PIL import Image
 
# creating a image object
im = Image.open("magic.png")
px = im.load()

for i in range(im.width):
    for j in range(im.height):
        coordinate = x, y = i, j
        if px[coordinate][3] == 0:
            continue

        print(f"particle minecraft:dust {px[coordinate][0]/255} {px[coordinate][1]/255} {px[coordinate][2]/255} {px[coordinate][3]/255} ~{(i*0.1)} ~{1+((im.height - j)*0.1)} ~ 0 0 0 0 0")
