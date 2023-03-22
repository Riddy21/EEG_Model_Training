import tensorflow as tf

model = tf.keras.models.load_model('./results/trial5/experiment2/attempt1/models/2_model.h5')
tf.keras.models.save_model(model, 'saved_model', save_format='tf')
