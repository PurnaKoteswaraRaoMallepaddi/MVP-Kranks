import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/purna/gcpVisionKey.json"

def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    #likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
    #                  'LIKELY', 'VERY_LIKELY')
    emotions_list = {}
    
    for face in faces:
#        print(face)
        emotions_list["Angry"] = face.anger_likelihood
        emotions_list["Happy"] =  face.joy_likelihood
        emotions_list['Surprise'] =  face.surprise_likelihood
        emotions_list['Sad'] =  face.sorrow_likelihood
    
    import operator
    label = max(emotions_list.items(), key=operator.itemgetter(1))[0]    
    print(label)
    
    return label

detect_faces('filename.jpg')