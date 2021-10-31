#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import cv2
import numpy
import string
import random
import argparse
import tensorflow as tf

def decode(characters, y):
    y = numpy.argmax(numpy.array(y), axis=2)[:,0]
    return ''.join([characters[x] for x in y])


model_name="model1"
captcha_dir="test_Images_Shriya"
output="test.csv"
symbols="symbolTrain2.txt"

symbols_file = open(symbols, 'r')
captcha_symbols = symbols_file.readline().strip()
symbols_file.close()

print("Classifying captchas with symbol set {" + captcha_symbols + "}")


with open(output, 'w') as output_file:
    model = tf.lite.Interpreter(model_path="converted_model2.tflite")
    model.allocate_tensors()
    input_details = model.get_input_details()
    output_details = model.get_output_details()

    for x in os.listdir(captcha_dir):
        # load image and preprocess it
        raw_data = cv2.imread(os.path.join(captcha_dir, x))
        rgb_data = cv2.cvtColor(raw_data, cv2.COLOR_BGR2RGB)
        image = numpy.array(rgb_data, dtype=numpy.float32) / 255.0
        (c, h, w) = image.shape
        image = image.reshape([-1, c, h, w])
        model.set_tensor(input_details[0]['index'], image)
        model.invoke()
        output_data = []
        for i in range(6):
            output_data.append(model.get_tensor(output_details[i]['index']))
        output_data = numpy.array(output_data, dtype=numpy.float32)
        output_file.write(x + ", " + decode(captcha_symbols, output_data) + "\n")

        print('Classified ' + x)

# if __name__ == '__main__':
#     main()
