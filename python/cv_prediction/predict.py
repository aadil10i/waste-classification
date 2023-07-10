import numpy as np
import cv2
from keras.models import load_model
import serial

def use_model(frame):
	model = load_model('C:/Users/AADIL/Documents/models/model5.h5')
	pic = cv2.resize(frame, (30, 60))
	pic = np.expand_dims(pic, axis=0)
	classes = model.predict_classes(pic)
	return classes

ser = serial.Serial('COM5', 9600)

while True:
	if(ser.in_waiting > 0):
		line = ser.readline()
		cap = cv2.VideoCapture(0)  
		ret,frame = cap.read() 
		predict = use_model(frame)[0]
		print(predict)

		if predict == 0:
			ser.write(b'u')
		else:
			ser.write(b'd')

		cv2.imshow('image',frame)
		cv2.waitKey(0)
		cv2.destroyAllWindows()