from django.http import HttpResponse
from django.template import Template, Context,loader
import datetime
#from VideoCapture import Device
#import cv2
import pygame
import pygame.camera


def index(request):
	pygame.camera.init()
	#pygame.camera.list_camera() #Camera detected or not
	cam = pygame.camera.Camera("/dev/video0",(640,480))
	cam.start()
	img = cam.get_image()
	pygame.image.save(img,"filename.jpg")
	cam.stop()

	template = loader.get_template('index.html')
	print('asf')
	return HttpResponse(template.render(request))