import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys
import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten
from tensorflow.keras.layers import Conv2D,MaxPooling2D,BatchNormalization,AveragePooling2D
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from tensorflow.keras import utils
from tensorflow.keras.utils import to_categorical


df = pd.read_csv('fer2013.csv')

# print(df.info())
# print(df["Usage"].value_counts())

# print(df.head())

X_train,train_y,X_test,test_y=[],[],[],[]

for index,row in df.iterrows():
    val=row['pixels'].split(" ")
    try:
        if 'Training' in row['Usage']:
            X_train.append(np.array(val,'float32'))
            train_y.append(row['emotion'])
        elif 'PublicTest' in row['Usage']:
            X_test.append(np.array(val, 'float32'))
            test_y.append(row['emotion'])
    except:
        print(f"error occured at index:{index} and row:{row}")

# print(f"X_train sample data:{X_train[0:2]}")
# print(f"train_y sample data:{train_y[0:2]}")
# print(f"X_test sample data:{X_test[0:2]}")
# print(f"test_y sample data:{test_y[0:2]}")

X_train = np.array(X_train, 'float32')
train_y = np.array(train_y, 'float32')
X_test = np.array(X_test, 'float32')
test_y = np.array(test_y, 'float32')

# Normalizing data between 0 and 1
X_train -= np.mean(X_train,axis=0)
X_train /= np.std(X_train,axis=0)

X_test -= np.mean(X_test,axis=0)
X_test /= np.std(X_test,axis=0)

num_features = 64
num_labels = 7
batch_size = 64
epochs = 30
width, height = 48, 48

X_train = X_train.reshape(X_train.shape[0],width,height,1)

X_test = X_test.reshape(X_test.shape[0],width,height,1)

train_y = utils.to_categorical(train_y,num_classes=num_labels)
test_y = utils.to_categorical(test_y,num_classes=num_labels)

#designing in cnn

model=Sequential()
#1st layer
model.add(Conv2D(num_features,kernel_size=(3,3),activation='relu', input_shape=(X_train.shape[1:])))
model.add(Conv2D(num_features,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
model.add(Dropout(0.5))

#2nd Convolutional layer
model.add(Conv2D(num_features, (3,3), activation='relu'))
model.add(Conv2D(num_features, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
model.add(Dropout(0.5))

#3rd convolutional layer
model.add(Conv2D(2*num_features,(3,3),activation='relu'))
model.add(Conv2D(2*num_features,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Flatten())

model.add(Dense(2*2*2*2*num_features,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2*2*2*2*num_features,activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_labels,activation='softmax'))
#model.summary()
model.compile(loss=categorical_crossentropy, optimizer=Adam(),metrics=['accuracy'])

model.fit(X_train,train_y,batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=(X_test,test_y),
    shuffle=True)

#saving model
fer_json=model.to_json()
with open("fer.json","w") as json_file:
    json_file.write(fer_json)
model.save_weights("fer.weights.h5")
