# Description: Extracts features from images using VGG16 model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.models import Model
# import tensorflow as tf
# import keras
# from keras.applications.vgg19 import VGG19, preprocess_input
# from keras.preprocessing import image
# from keras.models import Model
import numpy as np


class FeatureExtractor:
    def __init__(self):
        base_model = VGG19(weights='imagenet')
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

    def extract(self, img):
        img = img.resize((224, 224)).convert("RGB")  # VGG must take a 224x224 img as an input
        x = image.img_to_array(img)  # to np.array
        x = np.expand_dims(x, axis=0) 
        x = preprocess_input(x)  # subtract mean and normalize
        feature = self.model.predict(x)[0]  # (4096, )
        return feature / np.linalg.norm(feature)


