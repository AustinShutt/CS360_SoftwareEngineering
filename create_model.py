import tensorflow as tf
from tensorflow import keras
import os

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
#training parameters
epochs = 60 #number of generations
batch_size = 1 #number of images processed at once. Lower == higher detail

#Image parameters - Defines width and height images will be resized to. Increasing increases the amount of detail the model can detect, but it also increases the processing time
height = 28
width = 28

script_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(script_dir, "formatted_dataset", "Img")

training_set = tf.keras.preprocessing.image_dataset_from_directory(
    'formatted_dataset2/Img',
    labels='inferred',
    label_mode='categorical',
    #class_names=[]
    color_mode='grayscale',
    batch_size=batch_size,
    image_size=(height, width),
    seed = 123,
    validation_split=0.1,
    subset = 'training'
)
validation_set = tf.keras.preprocessing.image_dataset_from_directory(
    'formatted_dataset2/Img',
    labels='inferred',
    label_mode='categorical',
    #class_names=[]
    color_mode='grayscale',
    batch_size=batch_size,
    image_size=(height, width),
    seed = 123,
    validation_split=0.1,
    subset = 'validation'
)

model = tf.keras.Sequential([
    tf.keras.layers.Input((28,28,1), name='Input_Layer'),
    tf.keras.layers.Conv2D(8, 3, padding = 'same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(16, 3, padding = 'same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, padding = 'same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(62)
])

model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=[keras.losses.CategoricalCrossentropy(from_logits=True)],
    metrics=['accuracy']
)
#reached 100% accuracy on training set at epoch 185
model.fit(training_set, epochs=epochs, verbose= 2)


loss, accuracy = model.evaluate(validation_set)
print(f'Accuracy: {accuracy}')
print(f'Loss: {loss}')
model.save('saved_model')


