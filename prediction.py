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

        # Preprocess the image (e.g., normalization, resizing, etc.)
        # You may need to preprocess the image to match the preprocessing applied during training
        # For example, if you normalized the training images, you should normalize the test image as well
        #image = image / 255.0  # Example normalization

        # Reshape the image to match the input shape of your model
        self.image = np.expand_dims(self.image, axis=0)  # Add batch dimension

        # Make a prediction
        self.prediction = self.model.predict(self.image)

        # Get the predicted class label
        self.predicted_class_index = np.argmax(self.prediction, axis=1)

        self.class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  
        self.predicted_class_name = self.class_names[self.predicted_class_index[0]]
    def getPrediction(self):
        return self.predicted_class_name    

