import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import random
'''
This script can be modified to generate the csvs
Note that it is not necessary due to image names containing all labels

[age] is an integer from 0 to 116, indicating the age
[gender] is either 0 (male) or 1 (female)
[race] is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).
[date&time] is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace
'''

def main():
    print("Starting")
    path1 = r'D:\Faces\crop_part1'
    path = r'D:\Faces\UTKFace'

    age = []
    gender = []
    race = []
    
    files = []
    
    for f in os.listdir(path):
        files.append(f)
        
        result = f.split("_")
        if(not len(result) == 4):
            print(f)
        age.append(int(result[0]))
        gender.append(int(result[1]))
        race.append(int(result[2]))
        
        #img = cv2.imread(path + "/" + f)

    d = {'Image': files, 'Age': age, 'Gender': gender, 'Race': race}
    df = pd.DataFrame(data=d)
    df.set_index('Image')
    
    
    imgSet = []
    for i in range(len(files)):
        imgSet.append(i)
        #if (age[i] < 25 and age[i] > 14) and gender[i] == 1 and race[i] == 0:
            #imgSet.append(i)
    print(len(imgSet), "images selected")
    '''
    labels = []
    r = 0
    while r < len(imgSet):
        #r = int(random.uniform(0, len(imgSet)))
        f = df['Image'][imgSet[r]]
        img = cv2.imread(path + "/" + f)
        print(age[imgSet[r]])
        
        cv2.imshow("preview", img)
        key = cv2.waitKey(0)
        #print(key)
        if key == 48:
            labels.append(0)
        elif key == 49:
            labels.append(1)
        elif key == 0:
            r = r - 2
            labels.pop()
        elif key == -1:
            r = r - 2
        
        #print(labels)
        
        r = r + 1
    '''
    f= open("raceDataValidation.csv","w")
    for i in range(len(imgSet)):
        if i % 100 == 0:
            index = imgSet[i]
            f.write(str(df['Image'][index]) + "," + str(df['Race'][index]) + "\n")
    f.close()
        
if __name__ == "__main__":
    main()
