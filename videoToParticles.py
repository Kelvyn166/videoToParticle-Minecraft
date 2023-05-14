import cv2
import numpy as np


#function that returns an matriz of all_pixels[frame][pixel][rgb]
def extract_pixels(video_path):
    video = cv2.VideoCapture(video_path)

    all_pixels = []
    
    #width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = video.read()

        if not ret:
            break

        argb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        all_pixels.append(argb_frame)

    video.release()

    all_pixels = np.array(all_pixels)

    return all_pixels


#video pafh and function name
video_path = './nekoarc.gif'
func_name = 'nekoarc'

pixels = extract_pixels(video_path)

frames = len(pixels)

#creating all the lines of each pixel and each frame of the video
for i in range(frames): #frame
    with open(f"./func/{func_name}_{i}.mcfunction", "w") as f:
        width = len(pixels[i])
        for j in range(width): #width
            height = len(pixels[i][j])
            for k in range(height): #height

                if (pixels[i][j][k][2] == 255 and pixels[i][j][k][1] == 255 and pixels[i][j][k][0] == 255 and pixels[i][j][k][3] == 255):
                    continue

                f.write(f"particle minecraft:dust {pixels[i][j][k][2]/255} {pixels[i][j][k][1]/255} {pixels[i][j][k][0]/255} {pixels[i][j][k][3]/255} ~{(k*0.1)} ~{1+((width - j)*0.1)} ~ 0 0 0 0 0\n")
    f.close()


#creating the function that runs all frames in the right order
with open(f"./func/{func_name}_ani.mcfunction", "w") as f:
    f.write(f"""scoreboard players add frame Times 1
execute if score frame Times matches {frames}.. run scoreboard players set frame Times 0\n""")
    for i in range(frames):
        f.write(f"execute if score frame Times matches {i}..{i} run function testes:func/{func_name}_{i}\n")

f.close()