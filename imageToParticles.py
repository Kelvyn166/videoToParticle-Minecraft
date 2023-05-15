#pip install Pillow  
from PIL import Image

#video pafh and function name
img_path = './107678141_p0.png'
func_name = 'ai'

# creating a image object
im = Image.open(img_path)
px = im.load()

#creating a function of each pixel
with open(f"./{func_name}.mcfunction", "w") as f:
    for i in range(im.width):
        for j in range(im.height):
            coordinate = x, y = i, j


            #removing particles that have 0 transparency
            tranpencity = 255
            if len(px[coordinate]) > 3:
                tranpencity = px[coordinate][3]
                if px[coordinate][3] == 0:
                    continue

            f.write(f"particle minecraft:dust {px[coordinate][0]/255} {px[coordinate][1]/255} {px[coordinate][2]/255} {tranpencity/255} ~{(i*0.1)} ~{1+((im.height - j)*0.1)} ~ 0 0 0 0 0\n")
f.close()
