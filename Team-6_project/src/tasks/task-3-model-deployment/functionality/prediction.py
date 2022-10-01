import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np
MODEL = tf.keras.models.load_model('./funtionality/model.h5')

CLASSNAMES = ['abies_concolor',
 'acer_platanoides',
 'koelreuteria_paniculata',
 'liquidambar_styraciflua',
 'magnolia_soulangiana',
 'magnolia_virginiana',
 'malus_coronaria',
 'metasequoia_glyptostroboides',
 'morus_rubra',
 'pinus_bungeana',
 'prunus_yedoensis',
 'quercus_acutissima',
 'quercus_falcata',
 'quercus_imbricaria',
 'quercus_palustris',
 'quercus_rubra',
 'robinia_pseudo-acacia',
 'sassafras_albidum',
 'tilia_americana',
 'ulmus_rubra']


def get_prediction(filename):
    img = cv2.imread(r'filename')
    resize = tf.image.resize(img, (180,180))

    prediction = MODEL.predict(np.expand_dims(resize/255, 0))
    return CLASSNAMES[np.argmax(prediction[0])]