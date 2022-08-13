import face_recognition
import os
from dotenv import load_dotenv

load_dotenv()

def scanDir():
    dir = os.scandir(os.getcwd() + '/images/')
    print(os.getcwd() + '/images')
    for entry in dir :
        if entry.is_dir() or entry.is_file():
            print(entry.name)

def scanFaces():
    picture_of_me = face_recognition.load_image_file("./images/" + os.getenv('REF_IMAGE'))
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

imageName2 = './andy.jpg'

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("./images/" + imageName2)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")

# scanDir()
