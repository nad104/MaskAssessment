import os
import shutil

dist_res_lines = open("race_dominant_masked_out.txt", "r").readlines();
clean_lines = ["NULL" + "\t" + "NULL" + "\n"] * 15000;

for line in dist_res_lines:
    if (line != "NULL\n"):
        filenum = int(line.split('.')[0]);
        clean_lines[filenum] = line;

out = open("race_dominant_masked_out_betterformat.txt", "w");
for line in clean_lines:
    out.write(line);
out.close();