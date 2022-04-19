
from PIL import Image, ImageDraw
import cv2
import mediapipe as mp
import math
import numpy as np
import shutil
from os.path import exists

MAX_ZEROS = 5
#run on each image in folder
def generate_mask(foldername):
    no_mesh = 0
    filename = foldername + '.png' #begin with first file in folder
    filepath = foldername + '/' + filename
    for fi in range (1, 1001):
        #don't construct masked if it already exists
        if (exists(foldername + '_masked_white/' + filename)):
            print(filename + " already exists.");
            filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
            filepath = foldername + '/' + filename
            continue;

        print("Processing: " + filepath)

        #read image into cv
        image = cv2.imread(filepath)
        if (type(image) is None):
            raise TypeError("Image " + filepath + " could not be read.");
        height, width, _ = image.shape

        # get face mesh
        face_mesh = mp.solutions.face_mesh.FaceMesh()
        face_mesh_processed = face_mesh.process(image)

        try:
            facial_landmarks = face_mesh_processed.multi_face_landmarks[0]
        except TypeError as err:
            print("Could not construct mesh for " + filename)
            shutil.copy(filepath, foldername + '_no_mesh/' + filename)
            no_mesh = no_mesh + 1

            filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
            filepath = foldername + '/' + filename
            continue

        ##construct mask
        #read image into PIL
        masked = Image.open(filepath)
        # get important features
        mask_features = [0 for i in range(6)]
        mask_features[0] = facial_landmarks.landmark[195]  # nose bridge
        mask_features[1] = facial_landmarks.landmark[234]  # cheek below left eye
        mask_features[2] = facial_landmarks.landmark[58]  # cheek above left mouth
        mask_features[3] = facial_landmarks.landmark[152]  # below center mouth
        mask_features[4] = facial_landmarks.landmark[435]  # cheek above right mouth
        mask_features[5] = facial_landmarks.landmark[447]  # cheek below right eye

        #make triangles using features
        for i in range (1, len(mask_features) - 1):
            mask = ImageDraw.Draw(masked)
            mask.polygon([(int(mask_features[0].x* width), int(mask_features[0].y* height)), (int(mask_features[i].x* width), int(mask_features[i].y* height)), (int(mask_features[i+1].x* width), int(mask_features[i+1].y* height))], fill=(255, 255, 255))

        #save masked
        masked.save(foldername + '_masked_white/' + filename)

        filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
        filepath = foldername + '/' + filename

    print("Total bad images (no mesh): " + str(no_mesh)); #Total bad images (no mesh)
    data = open("mesh_stats.txt", "a");
    data.write(foldername + "\t" + str(no_mesh) + "\n");
    data.close();