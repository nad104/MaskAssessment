#!C:\Users\Nathan Dunphy\AppData\Local\Programs\Python\Python37
from PIL import Image, ImageDraw
import cv2
import mediapipe as mp

FILEPATH = '00000/00000/00002.png'

#read image into cv
image = cv2.imread(FILEPATH)
"""
#resize to display numbers
image = cv2.resize(image, (image.shape[0] * 3, image.shape[1] * 3), interpolation = cv2.INTER_AREA)"""
height, width, _ = image.shape

#obtain face mesh
face_mesh = mp.solutions.face_mesh.FaceMesh()
result = face_mesh.process(image)

#make display for face mesh
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0, 468):
        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)

        cv2.circle(image, (x, y), 2, (100, 100, 0), -1)
        cv2.putText(image, str(i), (x,y), 0,1,(0,0,0))
"""
#display + save face mesh
cv2.imshow("Face Mesh detection", image)
cv2.imwrite("mesh.png", image)
cv2.waitKey()
"""


##construct mask
#read image into PIL
masked = Image.open(FILEPATH)

#get important features
mask_features = [0 for i in range(6)]
mask_features[0] = facial_landmarks.landmark[195]    #nose bridge
mask_features[1] = facial_landmarks.landmark[234]    #cheek below left eye
mask_features[2] = facial_landmarks.landmark[58]     #cheek above left mouth
mask_features[3] = facial_landmarks.landmark[152]    #below center mouth
mask_features[4] = facial_landmarks.landmark[435]    #cheek above right mouth
mask_features[5] = facial_landmarks.landmark[447]    #cheek below right eye

#make triangles using features
for i in range (1, len(mask_features) - 1):
    mask = ImageDraw.Draw(masked)
    mask.polygon([(int(mask_features[0].x* width), int(mask_features[0].y* height)), (int(mask_features[i].x* width), int(mask_features[i].y* height)), (int(mask_features[i+1].x* width), int(mask_features[i+1].y* height))], fill=(0, 0, 0))

#show mask + save
masked.show()
masked.save("masked.png")