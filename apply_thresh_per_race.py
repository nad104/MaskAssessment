import sys
import numpy as np

from deepface import DeepFace as df #dev


RESULT_FILE = './dist_res_cleaner.txt';
RACE_INFO_FILE = './race_dominant_out.txt';
UNIQUE_RACES = ["asian", "indian", "black", "white", "middle eastern", "latino hispanic"]
thresh = [.05, .2, .3, .4];
thresh_count_per_race = np.zeros((len(UNIQUE_RACES), len(thresh)));
race_count_total =  [0] * len(UNIQUE_RACES);
files_05 = [];

race_info_list = open(RACE_INFO_FILE, "r").readlines();
with open(RESULT_FILE) as f:
    lines = f.readlines()

for line in lines:
    if (line == "NULL\n"):
        continue;
    if (line == ""):
        break;

    dist = float(line.split("\t")[1][0:-1]);
    for i in range(0, 4):
        if (dist < thresh[i]):
            filenum = int(line.split("\t")[0].split(".")[0]);
            race = race_info_list[filenum].split('\t')[1][:-1];
            if (race == "NULL"):
                break;

            thresh_count_per_race[UNIQUE_RACES.index(race)][i] += 1;
            race_count_total[UNIQUE_RACES.index(race)] += 1;

            #debug
            if (thresh[i] == .05):
                files_05.append(filenum);

print(files_05);

out_per = open("dist_res_summ_per_race.txt", "a");
for i in range(0, len(UNIQUE_RACES)):
    out_per.write(UNIQUE_RACES[i]);
    for j in range(0, 4):
         out_per.write("\t" + str(thresh_count_per_race[i][j]/ race_count_total[i]));
    out_per.write("\t" + str(1) + "\n");
out_per.close();
