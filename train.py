import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

'''
[age] is an integer from 0 to 116, indicating the age
[gender] is either 0 (male) or 1 (female)
[race] is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).
[date&time] is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace
'''
#print(df)
'''
plt.hist(age,bins='auto')
plt.show()
plt.hist(race,bins=[0,1,2,3,4])
plt.show()
plt.hist(gender,bins=[0,1])
plt.show()
'''

def main():
    print("Starting")
    validationPath = r'D:\Faces\crop_part1'
    trainPath = r'D:\Faces\UTKFace'
    
    model = tf.keras.models.load_model("Classifier.h5")
    epochCount = 0
    
    age = []
    gender = []
    race = []
    
    files = []

    '''
    for f in os.listdir(trainPath):
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
    '''
    
    #validationData = pd.read_csv("raceDataValidation.csv", names = ["File", "Label"])
    print("Reading Data")
    trainData = pd.read_csv("raceData.csv", names = ["File", "Label"])
    print("Done")

    if epochCount > 0:
        inputs = []
        outputs = []

        print("Loading Data")
        length = int(len(trainData["File"]))
        for i in range(length):
            r = random.uniform(0,1)
            if r >= 0.5:
                file = trainData["File"][i]
                img = cv2.imread(trainPath + "/" + file)
                img = tf.divide(img, 255)
                inputs.append(img)
                result = trainData["Label"][i]
                if result == 0:
                    output = [1,0,0,0,0]
                elif result == 1:
                    output = [0,1,0,0,0]
                elif result == 2:
                    output = [0,0,1,0,0]
                elif result == 3:
                    output = [0,0,0,1,0]
                elif result == 4:
                    output = [0,0,0,0,1]
                
                outputs.append(output)

        print("Done")

        
        trainInput = np.array(inputs)
        trainOutput = np.array(outputs)
        
        print("Starting Training")
        model.fit(trainInput, trainOutput, batch_size = 8, epochs=epochCount, use_multiprocessing = True, verbose=2)
        model.save("Classifier.h5")

        model.evaluate(trainInput, trainOutput, verbose=2)

    '''
    inputs = []
    outputs = []
    length = len(validationData["File"])
    for i in range(length):
        file = validationData["File"][i]
        img = cv2.imread(validationPath + "/" + file)
        img = tf.divide(img, 255)
        inputs.append(img)
        result = trainData["Label"][i]
        if result == 0:
            output = [1,0]
        else:
            output = [0,1]
        outputs.append(output)

    model.evaluate(np.array(inputs), np.array(outputs), verbose=2)
    '''
    print("Evaluating Sample")
    inputs = []
    outputs = []
    for i in range(1000):
        r = random.uniform(0,1)
        if r >= 0.5:
            file = trainData["File"][i]
            img = cv2.imread(trainPath + "/" + file)
            img = tf.divide(img, 255)
            inputs.append(img)
            result = trainData["Label"][i]
            if result == 0:
                output = [1,0,0,0,0]
            elif result == 1:
                output = [0,1,0,0,0]
            elif result == 2:
                output = [0,0,1,0,0]
            elif result == 3:d
                output = [0,0,0,1,0]
            elif result == 4:
                output = [0,0,0,0,1]
                
            outputs.append(output)

    print("Done")
        
    trainInput = np.array(inputs)
    trainOutput = np.array(outputs)

    model.evaluate(trainInput, trainOutput, verbose=2)
        
    r = 0  
    while True:
        r = int(random.uniform(0, len(trainData["File"])))
        #f = validationData['File'][r]
        f = trainData["File"][r]
        race = trainData["Label"][r]
        if race == 0:
            race = "White"
        elif race == 1:
            race = "Black"
        elif race == 2:
            race = "Asian"
        elif race == 3:
            race = "Indian"
        elif race == 4:
            race = "Other"
                    
        img = cv2.imread(trainPath + "/" + f)
        inputArr = tf.divide(img, 255)
        result = model.predict(np.array([inputArr]))
        print("\n")
        print("Ideal:", race)
        print()
        print("White:", 100 * result[0][0], "%")
        print("Black:", 100 * result[0][1], "%")
        print("Asian:", 100 * result[0][2], "%")
        print("Indian:", 100 * result[0][3], "%")
        print("Other:", 100 * result[0][4], "%")
        
        cv2.imshow("preview", img)
        key = cv2.waitKey(0)
        if key == 0:
            r = r - 1
        elif key == -1:
            r = r - 1
        else:    
            r = r + 1
    
if __name__ == "__main__":
    main()
