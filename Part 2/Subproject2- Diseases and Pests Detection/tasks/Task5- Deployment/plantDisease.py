# Importing Libraries
import streamlit as st
from PIL import Image 
import tensorflow as tf
#from keras.models import load_model
import os
import numpy as np
import pandas as pd
import time
import cv2

# Title and Description

st.title('Omdena - Algeria Chapter Green')
st.markdown('## Plant Disease Detection 🍁🍃🍂🍀')
st.write("Just Upload your Plant's Leaf Image and Get Predictions if Your Plant is Healthy or Not!")
st.write("")

# Loading Model
model = tf.keras.models.load_model("/content/plantdisease500.h5")
# model = load_model("model.h5")

# Upload the image
uploaded_file = st.file_uploader("Choose a Image file", type=[ 'jpg', 'jpeg', 'png', 'webp', 'jfif' ])

class_names = [ 'Apple Apple scab ', 'Apple Black rot ', 'Apple Cedar apple rust ', 'Apple healthy ',
                'Bacterial leaf blight in rice leaf ', 'Blight in corn Leaf ', 'Blueberry healthy ',
                'Brown spot in rice leaf ', 'Cercospora leaf spot ', 'Cherry (including sour) Powdery mildew ',
                'Cherry (including_sour) healthy ', 'Common Rust in corn Leaf ', 'Corn (maize) healthy ', 'Garlic ',
                'Grape Black rot ', 'Grape Esca Black Measles ', 'Grape Leaf blight Isariopsis Leaf Spot ',
                'Grape healthy ', 'Gray Leaf Spot in corn Leaf ', 'Leaf smut in rice leaf ',
                'Orange Haunglongbing Citrus greening ', 'Peach healthy ', 'Pepper bell Bacterial spot ',
                'Pepper bell healthy ', 'Potato Early blight ', 'Potato Late blight ', 'Potato healthy ',
                'Raspberry healthy ', 'Sogatella rice ', 'Soybean healthy ', 'Strawberry Leaf scorch ',
                'Strawberry healthy ', 'Tomato Bacterial spot ', 'Tomato Early blight ', 'Tomato Late blight ',
                'Tomato Leaf Mold ', 'Tomato Septoria leaf spot ', 'Tomato Spider mites Two spotted spider mite ',
                'Tomato Target Spot ', 'Tomato Tomato mosaic virus ', 'Tomato healthy ', 'algal leaf in tea ',
                'anthracnose in tea ', 'bird eye spot in tea ', 'brown blight in tea ', 'cabbage looper ', 'corn crop ',
                'ginger ', 'healthy tea leaf ', 'lemon canker ', 'onion ', 'potato crop ', 'potato hollow heart ',
                'red leaf spot in tea ' ]

# healthy classes.
healthy_cls = [ 'Apple healthy ', 'Blueberry healthy ', 'Cherry (including_sour) healthy ', 'Corn (maize) healthy ',
                'Grape healthy ', 'Peach healthy ', 'Pepper bell healthy ', 'Potato healthy ', 'Raspberry healthy ',
                'Soybean healthy ', 'Strawberry healthy ', 'Tomato healthy ', 'healthy tea leaf ' ]

if st.button("Process"):
    test_image = Image.open(uploaded_file)
    test_image = np.array(test_image.convert('RGB'))
    test_image_r = cv2.resize(test_image, (224, 224), interpolation=cv2.INTER_NEAREST)
    st.image(test_image, caption="Your input image")
    test_image_r = np.expand_dims(test_image_r, axis=0)
    st.write("Processing the image for prediction...")

    progress = st.progress(0)
    progress_text = st.empty()

    for i in range(101):
        time.sleep(0.2)
        progress.progress(i)
        progress_text.text(f"Progress:{i}%")

    probs = model.predict(test_image_r)
    pred_class = np.argmax(probs)

    pred_class_name = class_names[ pred_class ]

    if pred_class_name in healthy_cls:
        msg = f'Your crop-leaf is healthy and predicted class is "{pred_class_name}" with probability of {int(probs[ 0 ][ pred_class ] * 100)}%'
        st.success(msg)
    else:
        msg = f'Your crop-leaf is not healthy and predicted class is "{pred_class_name}" with probability of {int(probs[ 0 ][ pred_class ] * 100)}%'
        st.error(msg)

    st.write("👋 Thank you for using our App👋")
