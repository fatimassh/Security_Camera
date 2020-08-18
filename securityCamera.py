import face_recognition
import cv2
import numpy as np
from ringPhone import *
from sendEmail import *
from lockScreen import *

def capture():
    cv2.imwrite(filename='saved_img.jpg', img=frame)

#take video from the webcam.
video_capture = cv2.VideoCapture(0)

#load the image from its path, analyze it.
fatima_image = face_recognition.load_image_file("/Users/fo6em/Desktop/securityCamera/known-ppl/Fatima.png")
fatima_encoding = face_recognition.face_encodings(fatima_image)[0]

#pass the face encodings and names to the array
known_face_encodings = [ fatima_encoding ]
known_face_names = [ "Fatima" ]

while True:
    ret, frame = video_capture.read() #take the first video frame
    rgb_frame = frame[:, :, ::-1] #change the frame colors to RGB.
    
    #look for the faces in the frame, encode them.
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        #See if the face is a match for the known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances) #take the best match face and assighn its name.
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        #create rectangle around the faces.
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        #create rectangle in the  bottom to hold the name.
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX #choose the font
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1) #write the name
        
    
        if name != "Fatima":
            capture()
            ring_phone()
            send_email()
            lock_screen()

        
    #show the video in the screen, quit if 'q' is pressed.
    cv2.imshow('Security Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()







