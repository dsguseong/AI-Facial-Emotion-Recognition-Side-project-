# AI-Facial-Emotion-Recognition-Side-project-

1. Please decompress the split compressed files and combine them into one file. (The files are split due to large size.) <fer2013.z01 ~ 18>
2. Make Virtual environment 
3. Install all packages are required by the below modules
4. Execute emotion_detection.py module first in order to train the model, then VideoTest.py to monitor Facial emotion recognition.


'emotion_detection.py': 
Model Training and Saving

Data Loading and Preprocessing: Load and preprocess training and testing data from the given fer2013.csv file. Prepare the input data by using the pixel values of each image as features.

Model Design: Design a Convolutional Neural Network (CNN) model for classifying emotions in images. Use a Sequential model to stack layers sequentially.

Model Compilation and Training: Compile the model using the categorical_crossentropy loss function and the Adam optimizer. Train the model using the training data.

Model Saving: Save the trained model architecture as a fer.json file and save the weights as a fer.h5 file.

'VideoTester.py':
Model Loading and Facial Emotion Analysis

Model Loading: Load the previously saved fer.json file to restore the model architecture and initialize the model by loading the weights.

Facial Emotion Analysis: Capture video from the webcam and use OpenCV to detect faces. Extract the detected face regions, resize them, and convert them into a format that the model can predict. Then, use the model to predict emotions and display the predicted emotions around the detected faces.
