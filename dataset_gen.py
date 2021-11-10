
'''
@author:cvhadessun
date:2021-10-27
'''
import shutil
import os
import csv
import numpy as np 

def load_csv(csv_file):
    # load the csv file.
    # data=[]
    data_dict={}
    with open(csv_file,newline='') as fp:
        reader = csv.reader(fp,delimiter=' ')
        line = 0
        for row in reader:
            if line ==0:
                line=1
                continue
            id,clc=row[0].split(',')
            # data.append([int(id),int(clc)])
            data_dict[int(id)] = int(clc)

    return data_dict

    

# load_csv('./dataset/489/labels.csv')

