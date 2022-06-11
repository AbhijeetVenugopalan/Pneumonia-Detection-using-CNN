from msilib.schema import Directory
from flask import Flask, render_template, request
from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.image as mpplt
import tensorflow
app = Flask(__name__)


# import os
# import pickle
# import itertools
# import shutil
# import random
# import glob
# import warnings

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from tensorflow import keras
# from tensorflow.keras.models import Sequential, load_model
# from tensorflow.keras.layers import Activation, Dense, Flatten, Dropout, Conv2D, MaxPool2D
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.metrics import categorical_crossentropy
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.preprocessing import image
# from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay
# import keras
# from keras.models import Sequential, load_model
# from keras.layers import Activation, Dense, Flatten, Dropout, Conv2D, MaxPool2D
# from keras.optimizers import Adam
# from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing import image

@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/predict', methods = ['POST', 'GET'])
def pred():
    if(request.method == 'POST'):
        f = request.files['img']
        f.save(f.filename)

        model = load_model('cnn_model.h5')

        # image = tensorflow.keras.preprocessing.image.load_img(f.filename, target_size=(224, 224))
        # import numpy as np

        # input_arr = tensorflow.keras.preprocessing.image.img_to_array(image)
        # input_arr = np.array([input_arr])  # Convert single image to a batch.

        # input_arr = input_arr.astype('float32') / 255.  # This is VERY important
        # predictions = model.predict(input_arr)
        # print(predictions)
        # predicted_class = np.argmax(predictions, axis=-1)
        # print(predicted_class[0])

        # test = ImageDataGenerator().flow_from_directory(directory = 'C:/Users/Deepak Vaishnav/Desktop/ml model with flask/test', target_size = (224,224), classes= ['covid', 'normal'])
        # predictions = model.predict(x = test)
        # print(test.classes)

        import numpy as np
        import cv2


        class_names = ['covid', 'normal'] # fill the rest

        model = load_model('cnn_model.h5')

        model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

        img = cv2.imread(f.filename)
        img = cv2.resize(img,(224,224))
        img = np.reshape(img,(-1, 224, 224, 3) )

        classes = np.argmax(model.predict(img), axis = -1)

        print(classes)

        names = [class_names[i] for i in classes]

        print(names)

        # plt.show()


    # model = load_model('cnn_model_1.h5')
    # model.summary()
    # model.predict()
    # model = tflearn.DNN(network, tensorboard_verbose=0, checkpoint_path='./model.pkl')
    # model = pickle.load(open('./model.pkl', 'rb'))
    return "The image given is predicted to be "+ names[0]

if __name__ == '__main__':
    app.run(debug=True)