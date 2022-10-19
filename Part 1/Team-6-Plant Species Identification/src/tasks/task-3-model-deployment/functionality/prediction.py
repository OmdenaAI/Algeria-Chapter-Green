import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
MODEL = tf.keras.models.load_model('functionality\CNNmodel.h5')

CLASSNAMES = ['Abies Concolor',
 'Acer Rlatanoides',
 'Koelreuteria Paniculata',
 'Liquidambar Styraciflua',
 'Magnolia Soulangiana',
 'Magnolia Virginiana',
 'Malus Coronaria',
 'Metasequoia Glyptostroboides',
 'Morus Rubra',
 'Pinus Bungeana',
 'Prunus Yedoensis',
 'Quercus Acutissima',
 'Quercus Falcata',
 'Quercus Imbricaria',
 'Quercus Palustris',
 'Quercus Rubra',
 'Robinia Pseudo-acacia',
 'Sassafras Albidum',
 'Tilia Americana',
 'Ulmus Rubra']

CURRDIR = os.path.dirname(os.getcwd())
def get_prediction(filename):
    path = CURRDIR + "/task-3-model-deployment/"+filename
    img = cv2.imread(path)
    resize = tf.image.resize(img, (180,180))

    prediction = MODEL.predict(np.expand_dims(resize/255, 0))
    return CLASSNAMES[np.argmax(prediction[0])]