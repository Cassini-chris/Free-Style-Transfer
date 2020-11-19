#Need to be working
from flask import Flask
from flask import request
from flask import render_template

#Need to be pip install in env
import tensorflow as tf

#Probaly works without pip install
import numpy as np
import PIL.Image
import time
import functools

#For Saving the image on Google Cloud Storage
from datetime import datetime
#from google.cloud import storage

## Tensor to Image function
def tensor_to_image(tensor):
tensor = tensor*255
tensor = np.array(tensor, dtype=np.uint8)
if np.ndim(tensor)>3:
assert tensor.shape[0] == 1
tensor = tensor[0]
return PIL.Image.fromarray(tensor)

###########################################################################
#FUNCTION for "Painter Image Selection"####################################
###########################################################################
def select_painter_image():

message = request.get_json(force=True)
#encoding dict / padding image string
selected_painting_number = message['painter']
if selected_painting_number == 1:
print(1)
style_path = tf.keras.utils.get_file('1.jpg','https://storage.googleapis.com/epicml/1.jpg')
print(style_path)
elif selected_painting_number == 2:
print(2)
style_path = tf.keras.utils.get_file('2.jpg','https://storage.googleapis.com/epicml/2.jpg')
print(style_path)
elif selected_painting_number == 3:
print(3)
style_path = tf.keras.utils.get_file('3.jpg','https://storage.googleapis.com/epicml/3.jpg')
print(style_path)
elif selected_painting_number == 4:
print(4)
style_path = tf.keras.utils.get_file('4.jpg','https://storage.googleapis.com/epicml/4.jpg')
print(style_path)
elif selected_painting_number == 5:
print(5)
style_path = tf.keras.utils.get_file('5.jpg','https://storage.googleapis.com/epicml/5.jpg')
print(style_path)
elif selected_painting_number == 6:
print(6)
style_path = tf.keras.utils.get_file('6.jpg','https://storage.googleapis.com/epicml/6.jpg')
print(style_path)
elif selected_painting_number == 7:
print(7)
style_path = tf.keras.utils.get_file('7.jpg','https://storage.googleapis.com/epicml/7.jpg')
print(style_path)
elif selected_painting_number == 8:
print(8)
style_path = tf.keras.utils.get_file('8.jpg','https://storage.googleapis.com/epicml/8.jpg')
print(style_path)
elif selected_painting_number == 9:
print(9)
style_path = tf.keras.utils.get_file('9.jpg','https://storage.googleapis.com/epicml/9.jpg')
print(style_path)
elif selected_painting_number == 10:
print(10)
style_path = tf.keras.utils.get_file('10.jpg','https://storage.googleapis.com/epicml/10.jpg')
print(style_path)
elif selected_painting_number == 11:
print(11)
style_path = tf.keras.utils.get_file('11.jpg','https://storage.googleapis.com/epicml/11.jpg')
print(style_path)
elif selected_painting_number == 12:
print(12)
style_path = tf.keras.utils.get_file('12.jpg','https://storage.googleapis.com/epicml/12.jpg')
print(style_path)
elif selected_painting_number == 13:
print(13)
style_path = tf.keras.utils.get_file('13.jpg','https://storage.googleapis.com/epicml/13.jpg')
print(style_path)
elif selected_painting_number == 14:
print(14)
style_path = tf.keras.utils.get_file('14.jpg','https://storage.googleapis.com/epicml/14.jpg')
print(style_path)
elif selected_painting_number == 15:
print(15)
style_path = tf.keras.utils.get_file('15.jpg','https://storage.googleapis.com/epicml/15.jpg')
print(style_path)
elif selected_painting_number == 16:
print(16)
style_path = tf.keras.utils.get_file('16.jpg','https://storage.googleapis.com/epicml/16.jpg')
print(style_path)
elif selected_painting_number == 17:
print(17)
style_path = tf.keras.utils.get_file('17.jpg','https://storage.googleapis.com/epicml/17.jpg')
print(style_path)
elif selected_painting_number == 18:
print(18)
style_path = tf.keras.utils.get_file('18.jpg','https://storage.googleapis.com/epicml/18.jpg')
print(style_path)

elif selected_painting_number == 19:
print(19)
style_path = tf.keras.utils.get_file('19.jpg','https://storage.googleapis.com/epicml/19.jpg')
print(style_path)

elif selected_painting_number == 20:
print(20)
style_path = tf.keras.utils.get_file('20.jpg','https://storage.googleapis.com/epicml/20.jpg')
print(style_path)

elif selected_painting_number == 21:
print(21)
style_path = tf.keras.utils.get_file('21.jpg','https://storage.googleapis.com/epicml/21.jpg')
print(style_path)

elif selected_painting_number == 22:
print(22)
style_path = tf.keras.utils.get_file('22.jpg','https://storage.googleapis.com/epicml/22.jpg')
print(style_path)

elif selected_painting_number == 23:
print(23)
style_path = tf.keras.utils.get_file('23.jpg','https://storage.googleapis.com/epicml/23.jpg')
print(style_path)

elif selected_painting_number == 24:
print(24)
style_path = tf.keras.utils.get_file('24.jpg','https://storage.googleapis.com/epicml/24.jpg')
print(style_path)
return style_path


###########################################################################
#FUNCTION for "Painter Image"##################################################
###########################################################################
def load_img(path_to_img):
max_dim = 512
img = tf.io.read_file(path_to_img)
img = tf.image.decode_image(img, channels=3)
img = tf.image.convert_image_dtype(img, tf.float32)
shape = tf.cast(tf.shape(img)[:-1], tf.float32)
long_dim = max(shape)
scale = max_dim / long_dim
new_shape = tf.cast(shape * scale, tf.int32)
img = tf.image.resize(img, new_shape)
img = img[tf.newaxis, :]
return img

###########################################################################
#FUNCTION for "Own Image"##################################################
###########################################################################
def load_own_img():
#Getting image JSON from HTML upload via request function
message = request.get_json(force=True)
#encoding dict / padding image string
encoded = message['image']
img_check = encoded[ 0 : 4 ]
if img_check == "/9j/":
img_check = "jpg"
else:
img_check = "png"
print(img_check)
encoded += "=="
#decode image
decoded = base64.b64decode(encoded)

#Upload to Bucket
#os.environ["GCLOUD_PROJECT"] = "bigquerytraining-232218"
# datetime object containing current date and time

# now = datetime.now()
# storage_client = storage.Client()
# bucket_name = 'neural_style_bucket'
# bucket = storage_client.get_bucket(bucket_name)
# blob = bucket.blob("neural_style_bucket/upload_" + str(now) + "." + img_check)
# blob.upload_from_string(decoded, content_type='image/' + img_check)

img = decoded
max_dim = 512
img = tf.image.decode_image(img, channels=3)
img = tf.image.convert_image_dtype(img, tf.float32)
shape = tf.cast(tf.shape(img)[:-1], tf.float32)
long_dim = max(shape)
scale = max_dim / long_dim
new_shape = tf.cast(shape * scale, tf.int32)
img = tf.image.resize(img, new_shape)
img = img[tf.newaxis, :]
return img

def load_own_img_custom():
#Getting image JSON from HTML upload via request function
message = request.get_json(force=True)
#encoding dict / padding image string
encoded = message['custom_style']

if encoded ==0:
print("Custom Style 0 -Exit Custom Style Function")
img_custom = 0
img_custom_val = 0
return img_custom, img_custom_val
else:
img_custom_val = 1
encoded += "=="
#decode image
decoded = base64.b64decode(encoded)
img = decoded
max_dim = 512

img = tf.image.decode_image(img, channels=3)
img = tf.image.convert_image_dtype(img, tf.float32)
shape = tf.cast(tf.shape(img)[:-1], tf.float32)
long_dim = max(shape)
scale = max_dim / long_dim

new_shape = tf.cast(shape * scale, tf.int32)
img = tf.image.resize(img, new_shape)
img = img[tf.newaxis, :]
img_custom = img
return img_custom, img_custom_val
###########################################################################
#FUNCTION for SENDING IMAGE back to HTML###################################
###########################################################################
## Dependencies for BASE64 encoding
from PIL import Image
from io import BytesIO
import io
import base64
from flask import jsonify
#from flask import send_file

## Function that will encode created image file to base64
def serve_pil_image(pil_img):
img_io = io.BytesIO()
pil_img.save(img_io, 'PNG', quality=100)
img_io.seek(0)
img = base64.b64encode(img_io.getvalue())
return(img)
#return send_file(img, mimetype='image/png', as_attachment=False)



###########################################################################
#FLASK APP#################################################################
###########################################################################
app = Flask(__name__)
@app.route('/')
def index():
#return("test")
return render_template('web_interface.html')
print(" * Loading Style Model")


@app.route("/transfer", methods = ["POST"])
def transfer():

#IMAGES
style_path = select_painter_image() #Select Painter Image on Cloud Storage
content_image = load_own_img() #Load Uploaded Image
style_image = load_img(style_path) #Load Painter Image

custom_style, img_custom_val = load_own_img_custom() #Load Uploaded Style

## Neutral Network
import tensorflow_hub as hub
hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
#Output as Tensor:

if img_custom_val == 0:
stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]


if img_custom_val == 1:
print(custom_style)
stylized_image = hub_module(tf.constant(content_image), tf.constant(custom_style))[0]



#Transform to Image
output_image = tensor_to_image(stylized_image)
#print("Message: ", message)
response = serve_pil_image(output_image)
# print(response)
return (response)
