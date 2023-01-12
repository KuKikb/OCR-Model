import os
import cv2
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)
    
tf.config.list_physical_devices('GPU')

model_path = r"D:\snippy\models\snippyclassifier.h5"
new_model = load_model(model_path)

tokens = sorted(os.listdir(r"D:\snippy\\tokens"))
tokens_predicted = []
for i in range(len(tokens)):
    token_path = "D:\snippy\\tokens"+"\\"+str(i)+".png"
    print(token_path)
    img = cv2.imread(token_path)
    resize = tf.image.resize(img, (256,256))
    yhat = new_model.predict(np.expand_dims(resize/255, 0))
    predicted_value = np.argmax(yhat)
    tokens_predicted.append(predicted_value)
    
file = open("D:\snippy\snippy_output_file.txt",'w')
for i in tokens_predicted:
    if i >= 0 and i <= 25:
        file.write(chr(i+65))
    
    elif i >= 26 and i <= 51:
        file.write(chr(i+71))
        
    file.flush()
        
file.close()

for i in range(len(tokens)):
    token_path = "D:\snippy\\tokens"+"\\"+str(i)+".png"
    os.remove(token_path)