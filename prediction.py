import tensorflow as tf
from tensorflow import keras
import numpy as np

"""
@InProceedings{deCampos09,
  author    = "de Campos, T.~E. and Babu, B.~R. and Varma, M.",
  title     = "Character recognition in natural images",
  booktitle = "Proceedings of the International Conference on Computer
  Vision Theory and Applications, Lisbon, Portugal",
  month     = "February",
  year      = "2009",
}
"""

class Predictor():
    def __init__(self, imagePath):
        self.height = 28
        self.width = 28

        # Load the trained model
        self.model = keras.models.load_model('saved_model')
        # Load the image using keras.preprocessing
        self.image = keras.preprocessing.image.load_img(imagePath, target_size=(self.height, self.width), color_mode='grayscale')

        # Convert the image to a numpy array
        self.image = keras.preprocessing.image.img_to_array(self.image)

        # Reshape the image to match the input shape of your model
        self.image = np.expand_dims(self.image, axis=0)  # Add batch dimension

        # Make a prediction
        self.prediction = self.model.predict(self.image)

        # Get the predicted class label
        self.predicted_class_index = np.argmax(self.prediction, axis=1)

        #list of possible outputs. Each entry cooresponds to an output neuron
        self.class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']  
        self.predicted_class_name = self.class_names[self.predicted_class_index[0]]
    
    
    #returns predicted value
    def getPrediction(self):
        return self.predicted_class_name
