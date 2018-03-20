from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context,loader
import datetime
#from VideoCapture import Device
#import cv2
import pygame
import pygame.camera
from .models import log_in
from django.contrib.auth.models import User
from django.http import JsonResponse
import operator
import io
import os
from google.cloud import vision
from google.cloud.vision import types
import requests

def log_in(request):

	
	template = loader.get_template('index_login.html')
	print(template)
	return  HttpResponse(template.render(request))

def homepage(request):
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/purna/gcpVisionKey.json"
	user_id = request.GET.get('user_id');
	pass_word = request.GET.get('pass_word')
	print("user_id")
	print(pass_word)
	
	#template = loader.get_template('index.html')
	#return ('<h1>i am bored<h1>')
	pygame.camera.init()
	
	#pygame.camera.list_camera() #Camera detected or not
	cam = pygame.camera.Camera("/dev/video0",(640,480))
	cam.start()
	img = cam.get_image()
	pygame.image.save(img,"filename.jpg")
	cam.stop()
	"""Detects faces in an image."""
	path = '/home/purna/final/static_cdn/son_website/filename.jpg'
	client = vision.ImageAnnotatorClient()

	with io.open(path, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)
	print('here')
	response = client.face_detection(image=image)
	faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    #likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
    #                  'LIKELY', 'VERY_LIKELY')
	emotions_list = {}
    
	for face in faces:
		emotions_list["Angry"] = face.anger_likelihood
		emotions_list["Happy"] =  face.joy_likelihood
		emotions_list['Surprise'] =  face.surprise_likelihood
		emotions_list['Sad'] =  face.sorrow_likelihood
	if len(emotions_list) == 0:
		emotions_list["Angry"] = 0
		emotions_list["Happy"] =  5
		emotions_list['Surprise'] =  0
		emotions_list['Sad'] =  0
	label = max(emotions_list.items(), key=operator.itemgetter(1))[0]    
	print(label)
	#r = requests.get('http://127.0.0.1:8000/music/check/')
	#print('tararampam')
	template_1 = loader.get_template('index.html')
	parameter = {'mood' : label}
	return render(request, 'index.html' ,parameter)
 