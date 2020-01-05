import tensorflow as tf
import os
import cv2
import numpy as np

def main():
    path = r'C:\Users\jeffr\Desktop\RaceClassifier'
    fileName = 'trump.jpg'
    model = tf.keras.models.load_model("Classifier.h5")

    img = cv2.imread(path + "/" + fileName)

    inputArr = tf.divide(img, 255)
    result = model.predict(np.array([inputArr]))

    print("White:", 100 * result[0][0], "%")
    print("Black:", 100 * result[0][1], "%")
    print("Asian:", 100 * result[0][2], "%")
    print("Indian:", 100 * result[0][3], "%")
    print("Other:", 100 * result[0][4], "%")
            
    cv2.imshow("preview", img)
    key = cv2.waitKey(0)

if __name__ == "__main__":
    main()
