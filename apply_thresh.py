import sys
import numpy as np

RESULT_FILE = './dist_res_clean.txt';
TOTAL_FOLDERS = 15;
thresh = [.05, .2, .3, .4];
thresh_count_total = [0] * 4;
thresh_count_per_folder = np.zeros((TOTAL_FOLDERS, 4));
files_05 = [];
dist_4 =0;

with open(RESULT_FILE) as f:
    lines = f.readlines()

for line in lines:
    dist = float(line.split("\t")[1][0:-1]);
    for i in range(0, 4):
        if (dist < thresh[i]):
            filenum = int(line.split("\t")[0].split(".")[0]);
            foldernum = int(filenum / 1000);
            thresh_count_per_folder[foldernum][i] += 1;
            thresh_count_total[i] += 1;

            #debug
            if (thresh[i] == .05):
                files_05.append(filenum);
            if (thresh[i] == 0.4 and foldernum < 10):
                dist_4+=1;

print(files_05);

print(dist_4);
"""
out_total = open("dist_res_summ_total.txt", "a");
for i in range (0, 4):
    out_total.write(str(thresh[i]) + "\t" + str(thresh_count_total[i]) + "\n");
out_total.close();

out_per = open("dist_res_summ_per_white_VGG-Face.txt", "a");
for i in range (0, TOTAL_FOLDERS):
    out_per.write(str(i));
    for j in range(0, 4):
         out_per.write("\t" + str(thresh_count_per_folder[i][j]));
    out_per.write("\n");
out_per.close();
"""
