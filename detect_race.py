from deepface import DeepFace as df
import os.path
import cv2
#dev
import matplotlib.pyplot as plt
import time

TOTAL_IMAGES = 1000;  # in folder
MAX_ZEROS = 5;
race_analysis_list = [0] * TOTAL_IMAGES;
race_dominant_list = [0] * TOTAL_IMAGES;
race_analysis_masked_list = [0] * TOTAL_IMAGES;
race_dominant_masked_list = [0] * TOTAL_IMAGES;
#FOLDER_NUM = 0;
def detect_race(foldername):
    #FOLDER_NUM = foldernum;

    #determine num of zeros to prepend string with
    num_verified = 0
    total_masked = TOTAL_IMAGES
    #run on each image in folder
    filename = foldername + '.png'  # begin with first file in folder
    filepath = foldername + '/' + filename
    filepath_masked = foldername + '_masked/' + filename
    for fi in range (1, TOTAL_IMAGES + 1):
        print("Detecting race: " + filename)
        #if there is no masked version
        if (not os.path.isfile(filepath_masked)):
            print(filename + " does not have masked version")
            total_masked -= 1

            filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
            filepath = foldername + '/' + filename
            filepath_masked = foldername + '_masked/' + filename
            continue

        #read in and convert images to workable
        img = cv2.imread(filepath);
        img_masked = cv2.imread(filepath_masked);
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);
        img_rgb_masked = cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB);

        ver = None;
        ver_masked = None;
        try:
            ver = df.analyze(img_rgb, actions = ['race', 'dominant_race']);
        except ValueError:
            print("Could not recognize unmasked face.")
        try:
            ver_masked = df.analyze(img_rgb_masked, actions = ['race', 'dominant_race']);
        except ValueError:
            print("Could not recognize masked face.")

        if (ver is not None):
            #add dominant race to list
            race_dominant_list.insert(fi, filename + "\t" + ver['dominant_race']);
            # make string to contain race info in one line
            race_analysis_str = ""
            for race in ver['race']:
                race_analysis_str += race + " " + str(ver['race'][race]) + "\t";
            race_analysis_list.insert(fi, filename + "\t" + race_analysis_str);
        else:
            race_dominant_list.insert(fi, filename + "\t" + "NULL");
            race_analysis_list.insert(fi, filename + "\t" + "NULL");

        if (ver_masked is not None):
            # add dominant race to list
            race_dominant_masked_list.insert(fi, filename + "\t" + ver_masked['dominant_race']);
            # make string to contain race info in one line
            race_analysis_masked_str = ""
            for race in ver_masked['race']:
                race_analysis_masked_str += race + " " + str(ver_masked['race'][race]) + "\t";
            race_analysis_masked_list.insert(fi, filename + "\t" + race_analysis_masked_str);
        else:
            race_dominant_masked_list.insert(fi, filename + "\t" + "NULL");
            race_analysis_masked_list.insert(fi, filename + "\t" + "NULL");

        #update for next iteration
        filename = str(int(foldername) + fi).zfill(MAX_ZEROS) + '.png'
        filepath = foldername + '/' + filename
        filepath_masked = foldername + '_masked/' + filename


    race_dominant_out = open("race_dominant_out.txt", "a");
    race_dominant_masked_out = open("race_dominant_masked_out.txt", "a");
    race_analysis_out = open("race_analysis_out.txt", "a");
    race_analysis_masked_out = open("race_analysis_masked_out.txt", "a");

    print();
    print(race_dominant_list);
    for i in range(1, TOTAL_IMAGES+1):
        if(race_dominant_list[i] != 0):
            race_dominant_out.write(race_dominant_list[i] + "\n");
        if (race_dominant_masked_list[i] != 0):
            race_dominant_masked_out.write(race_dominant_masked_list[i] + "\n");
        if (race_analysis_list[i] != 0):
            race_analysis_out.write(race_analysis_list[i] + "\n");
        if (race_analysis_masked_list[i] != 0):
            race_analysis_masked_out.write(race_analysis_masked_list[i] + "\n");

    race_dominant_out.close();
    race_dominant_masked_out.close();
    race_analysis_out.close();
    race_analysis_masked_out.close();