from flask import Flask, render_template, request,flash
import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename


model = load_model('model_inception.h5')


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def pred_skin_disease(tomato_plant):
  test_image = load_img(tomato_plant, target_size = (224, 224)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==0:
      return 'actinic keratosis.html', 'actinic keratosis'
       
  elif pred==1:
      return 'basal cell carcinoma.html', 'basal cell carcinoma'
        
  elif pred==2:
      return 'dermatofibroma.html', 'dermatofibroma'
        
  elif pred==3:
      return 'melanoma.html', 'melanoma'
       
  elif pred==4:
      return 'nevus.html', 'nevus'
        
  elif pred==5:
      return 'pigmented benign keratosis.html', 'pigmented benign keratosis'
        
  elif pred==6:
      return 'seborrheic keratosis.html', 'seborrheic keratosis'
        
  elif pred==7:
      return 'Tsquamous cell carcinoma.html', 'squamous cell carcinoma'
  elif pred==8:
      return 'vascular lesion.html', 'vascular lesion'
        
  


@app.route('/')
def home():
    return render_template('index.html')





@app.route('/resultc', methods=['POST'])
def result():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        file = request.files['file']
        if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           flash('Image successfully uploaded and displayed below')
           img = cv2.imread('static/uploads/'+filename)
           file_path='static/uploads/'+filename
           print("@@ Predicting class......")
           output_page,pred_output = pred_skin_disease(tomato_plant=file_path)
           return render_template(output_page,pred_output=pred_output,filename= filename,fn=firstname, ln=lastname, age=age,gender=gender)

        else:
            flash('Allowed image types are - png, jpg, jpeg')
            return render_template('index.html')                       


# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    app.run(debug=True,port=8000)
