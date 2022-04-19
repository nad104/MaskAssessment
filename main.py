#!C:\Users\Nathan Dunphy\AppData\Local\Programs\Python\Python37
from mask_gen import generate_mask
from recog_test import recog
from make_dir import make_dir
from detect_race import detect_race
import os.path
import time
import sys

MODEL_NAME = "VGG-Face"
MAX_ZEROS = 5;
SLEEP_TIME = 30;
BEGIN_FOLDER = 9;
END_FOLDER = 10;
#redo_fns = [7];

for i in range(BEGIN_FOLDER,END_FOLDER):
#for i in redo_fns:

    foldername = str(i * 1000).zfill(MAX_ZEROS);
    fn_masked = foldername + "_masked_white";
    fn_nomesh = foldername + "_no_mesh";
    fn_05 = foldername + "_05_white";
    if (not os.path.isdir(fn_masked)):
        make_dir(fn_masked);
    if (not os.path.isdir(fn_nomesh)):
        make_dir(fn_nomesh);
    if (not os.path.isdir(fn_05)):
        make_dir(fn_05);
    
    try:
        generate_mask(foldername);
        recog(foldername, MODEL_NAME);
        #detect_race(foldername);
    except:
        print("Error: " + str(sys.exc_info()[0]) + " occurred.\nMask generation halted for " + str(SLEEP_TIME) + " seconds for garbage collection.");
        time.sleep(SLEEP_TIME);
        i-=1; #try again next iteration

