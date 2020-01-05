# RaceClassifier
 Estimates a person's race using an image of their face

## Built Using
- Python 3.6.1
- Tensorflow 2.0
- Pandas 0.25.0
- Numpy 1.17.3
- OpenCV 4.1.1.26

Note: Built in Windows Environment

Validation and model tweaks are in progress.

Dataset used: https://susanqq.github.io/UTKFace/

## Features
- Input: 200x200 RBG image 
- Output: Array of length 5 with each element containing a probability of the corresponding race
- Array format is as follows: White, Black, Asian, Indian, and Others
- Others refers to Hispanic, Latino, Middle Eastern, etc.
