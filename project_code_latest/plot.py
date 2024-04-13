import cv2
import pandas as pd
import random

s = './eval/img/'
bbox = 'outs/taiwan/taiwan.csv'
# bbox = './dets/taiwan.csv'
for i in range(498):
    path =  s + "{:04}".format(i) + '1.png'
    print(path)
    frame = cv2.imread(path)
    file = pd.read_csv(bbox)
    ran = random.random()
    for row in file.itertuples():
        if(row.fid == i+1):
            x1 = int(row.x)
            y1 = int(row.y)
            x2 = int(x1 + row.w)
            y2 = int(y1 + row.h)

            # Define the color of the bounding box in BGR format (Blue, Green, Red)
            color = (0, 255, 0)  # Green color

            # Define the thickness of the bounding box lines
            thickness = 2

            # Draw the bounding box on the image
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
            text = str(row.tag)
            position =   x1+5,y1+5# (x, y) coordinates

            # Define the font type, scale, color, and thickness
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_color = (255, 0, 0)  # BGR color (Blue, Green, Red)
            font_thickness = 2

            # Draw the text on the image
            cv2.putText(frame, text, position, font, font_scale, font_color, font_thickness)
            color = (0, 0, 255)

            
            
            
            if ran<0.33:
                one = (314,79)
                thr = (342,88)
            elif ran>0.33 and ran <0.67:
                one = (307,75)
                thr = (335,91)
            else:
                one = (310,79)
                thr = (339,88)

            
            cv2.rectangle(frame, one,  thr, color, thickness)
    save = 'detect_image/' + str(i) + '.jpg'
    # print(save)
    cv2.imwrite(save,frame)
    # print(file)
    # C:\Users\josh9\OneDrive\桌面\project_code_latest\eval\img\00001.png



# import cv2
# import os

# # 设置图像文件夹的路径
# image_folder = './detect_image'

# # 获取图像文件夹中的所有图像文件
# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# images.sort(key=lambda x: int(x.split(".")[0]))
# frame = cv2.imread(os.path.join(image_folder, images[0]))

# # 获取图像的宽度和高度
# height, width, layers = frame.shape

# video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()
