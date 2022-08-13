import face_recognition
import os
from dotenv import load_dotenv
import shutil

# Loading environment variables from .env file
load_dotenv()

# Function for scanning all images in the images folder
def scanDir():
    dir = os.scandir(os.getcwd() + '/images/')
    for entry in dir :
        if entry.is_dir() or entry.is_file():
            scanFaces(entry.name)

# Function for scanning all faces in an image
def scanFaces(imageName):

    # Reference image to compare against
    picture_of_me = face_recognition.load_image_file(os.getcwd() + "/images/" + os.getenv('REF_IMAGE'))
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    imageName2 = imageName

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    try:
        unknown_picture = face_recognition.load_image_file(os.getcwd() + "/images/" + imageName2)
        unknown_face = face_recognition.face_locations(unknown_picture)

        # Now we can see the two face encodings are of the same person with `compare_faces`!
        for face_location in unknown_face:
            # Declaring image to compare with
            unknownFacePresent = face_recognition.face_encodings(unknown_picture, known_face_locations = [face_location])[0]
            results = face_recognition.compare_faces([my_face_encoding], unknownFacePresent)
            if results[0] == True and imageName2 != os.getenv('REF_IMAGE'):
                shutil.move(os.getcwd() + '/images/' + imageName, os.getcwd() + '/images/pictureOfMe/' + imageName)
                print("It's a picture of me!")
                if os.path.isdir(os.getcwd() + '/images/pictureOfMe') == False:
                    os.mkdir(os.getcwd() + '/images/pictureOfMe')
                shutil.move(os.getcwd() + '/images/' + imageName, os.getcwd() + '/images/pictureOfMe/' + imageName)
            else:
                print("It's not a picture of me!")
    except:
        print("No face found")

# Calling function to scan all images in the images folder
scanDir()
