import os, sys
import shutil
import csv


datapath = "data_remove_edge_image_denoisy"
datasetpath = "datasets"


with open("annos.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == "1":
            shutil.copytree(os.path.join(datapath,row[0]), os.path.join(datasetpath,row[0]))
