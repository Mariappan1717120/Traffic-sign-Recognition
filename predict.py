from tensorflow.python.keras.models import load_model
from skimage import transform
from skimage import exposure
from skimage import io
from imutils import paths
import numpy as np
import imutils
import random
import cv2
import os

def trafficsign(imagePath):
	model = load_model('trafficsignnet.model')
	model._make_predict_function()
	labelNames = open("signnames.csv").read().strip().split("\n")[1:]
	labelNames = [l.split(",")[1] for l in labelNames]
	image = io.imread(imagePath)
	image = transform.resize(image, (32, 32))
	image = exposure.equalize_adapthist(image, clip_limit=0.1)
	image = image.astype("float32") / 255.0
	image = np.expand_dims(image, axis=0)
	preds = model.predict(image)
	j = preds.argmax(axis=1)[0]
	label = labelNames[j]
	return label




