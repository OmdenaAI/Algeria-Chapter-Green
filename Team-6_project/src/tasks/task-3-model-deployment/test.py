import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np
model = tf.keras.models.load_model('./funtionality/model.h5')

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

img = cv2.imread(r'D:\Omdena\Algeria-Chapter-Green\Team-6_project\src\tasks\task-1-filtering-data\testing-leafsnap-random-20-merged\sassafras_albidum\wb1043-01-1.jpg')
resize = tf.image.resize(img, (180,180))

prediction = model.predict(np.expand_dims(resize/255, 0))
print(CLASSNAMES[np.argmax(prediction[0])])