Scenario 7: Image Augmentation
Python
import tensorflow as tf
from tensorflow.keras import layers

data_augmentation = tf.keras.Sequential([
    layers.RandomRotation(0.11),   # ~20 degrees
    layers.RandomFlip("horizontal"),
    layers.RandomZoom(0.2)
])
