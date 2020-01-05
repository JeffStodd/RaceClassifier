import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import random
'''
This script removes images with incorrect name formatting

[age] is an integer from 0 to 116, indicating the age
[gender] is either 0 (male) or 1 (female)
[race] is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).
[date&time] is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace
'''

def main():
    print("Starting")
    path1 = r'D:\Faces\crop_part1'
    path = r'D:\Faces\UTKFace'
    
    for f in os.listdir(path):

        try:
            img = cv2.imread(path + "/" + f)

            new = f[:len(f)-9]
            cv2.imwrite(path + "/" + new, img)
            os.remove(path + "/" + f)
        except:
            pass
        
if __name__ == "__main__":
    main()
