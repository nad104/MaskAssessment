from deepface import DeepFace as df
import math
import os
import shutil

TOTAL_IMAGES = 1000;  # in folder
MAX_ZEROS = 5;
dist_list = [0] * TOTAL_IMAGES;
#FOLDER_NUM = 0;
def recog(foldername, model):
    """    #FOLDER_NUM = foldernum;

    #determine num of zeros to prepend string with
    num_verified = 0
    total_masked = TOTAL_IMAGES
    #run on each image in folder
    filename = foldername + '.png'  # begin with first file in folder
    filepath = foldername + '/' + filename
    filepath_masked = foldername + '_masked/' + filename
    for fi in range (1, 1001):
        print("Verifying: " + filename)
        #if there is no masked version
        if (not os.path.isfile(filepath_masked)):
            print(filename + " does not have masked version")
            total_masked -= 1

            filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
            filepath = foldername + '/' + filename
            filepath_masked = foldername + '_masked/' + filename
            continue

        ver = df.verify(filepath, filepath_masked, enforce_detection = False, model_name = model)

        dist_list.insert(fi, filename + "\t" + str(ver['distance']));  #add distance to list

        #add to 05 folder if person is exceptionally recognizable with mask
        if (ver['distance'] <= 0.05):
            shutil.copy(filepath, foldername + '_05/' + filename)

        filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
        filepath = foldername + '/' + filename
        filepath_masked = foldername + '_masked/' + filename

    #dist_list.insert(0, str(FOLDER_NUM) + "\t" + str(total_masked));
    out = open("dist_res_" + model + ".txt", "a");
    for i in range (0, 1001):
        if (dist_list[i] != 0):
            out.write(dist_list[i] + "\n");
    out.close();
"""
def recog(foldername, model):
    #FOLDER_NUM = foldernum;

    #determine num of zeros to prepend string with
    num_verified = 0
    total_masked = TOTAL_IMAGES
    #run on each image in folder
    filename = foldername + '.png'  # begin with first file in folder
    filepath = foldername + '/' + filename
    filepath_masked = foldername + '_masked_white/' + filename
    for fi in range (1, 1001):
        print("Verifying: " + filename)
        #if there is no masked version
        if (not os.path.isfile(filepath_masked)):
            print(filename + " does not have masked version")
            total_masked -= 1

            filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
            filepath = foldername + '/' + filename
            filepath_masked = foldername + '_masked_white/' + filename
            continue

        ver = df.verify(filepath, filepath_masked, enforce_detection = False, model_name = model)

        dist_list.insert(fi, filename + "\t" + str(ver['distance']));  #add distance to list

        #add to 05 folder if person is exceptionally recognizable with mask
        if (ver['distance'] <= 0.05):
            shutil.copy(filepath, foldername + '_05_white/' + filename)

        filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
        filepath = foldername + '/' + filename
        filepath_masked = foldername + '_masked_white/' + filename

    #dist_list.insert(0, str(FOLDER_NUM) + "\t" + str(total_masked));
    out = open("dist_res_white_" + model + ".txt", "a");
    for i in range (0, 1001):
        if (dist_list[i] != 0):
            out.write(dist_list[i] + "\n");
    out.close();

"""
out = open("res.txt", "a")
out.write('\n' + foldername + "\t" + str(thresh) + "\t" + str(num_verified) + "\t" + str(total_masked - num_verified) + "\t" + str(num_verified / (total_masked - num_verified)) ) #pos, neg, ratio  #tab delim
out.close()
"""

