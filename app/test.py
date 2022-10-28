import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'model_inception.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

tomato_plant = cv2.imread('D:/backup/UPES/minor project/skin dataset/Train/melanoma/ISIC_0000159.jpg')
test_image = cv2.resize(tomato_plant,(224, 224)) # load image 
  
test_image = img_to_array(test_image)/255 # convert image to np array and normalize
test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
result = model.predict(test_image) # predict diseased palnt or not
  
pred = np.argmax(result, axis=1)
print(pred)
if pred==0:
    print( "actinic keratosis")
       
elif pred==1:
    print("basal cell carcinoma")
        
elif pred==2:
    print("dermatofibroma")
        
elif pred==3:
    print("melanoma")
       
elif pred==4:
    print("nevus")
        
elif pred==5:
    print("pigmented benign keratosis")
        
elif pred==6:
    print("seborrheic keratosis")
        
elif pred==7:
      print("Tsquamous cell carcinoma")
elif pred==8:
      print("vascular lesion")
        
