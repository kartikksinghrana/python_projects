import numpy
import face_recognition as fr
import cv2

video_capture = cv2.VideoCapture(0)

kartik_image = fr.load_image_file("I:\\Python_projects\\face_detection\\kartik1.jpg")
# face_encoding returns an array 
kartik_face_encoding = fr.face_encodings(kartik_image)[0]

# more names and encodings can be added
known_face_encodings = [kartik_face_encoding]
known_face_names = ["KARTIK"]

# to take frames from camera to recognice face
while True:
   ret, frame = video_capture.read()
    # frame of the camera and change the color
   rgb_frame = frame [:, :, ::-1]
    # where are the faces = location in frame
   face_locations= fr.face_locations(rgb_frame)
    # encode and compare
   face_encodings= fr.face_encodings(rgb_frame,face_locations)
   
#  iterate location into top down bottom.... and encodings into encoding
   for (top , right , bottom ,left),face_encoding in zip(face_locations,face_encodings):
    #   comparing known faceencodings and encoding that are passed for leanring
        matches=fr.compare_faces(known_face_encodings,face_encoding)

        name="Unknown"
        # how similar the face are when comparing from know face list
        face_distance = fr.face_distance(known_face_encodings,face_encoding)

        best_match_index = numpy.argmin(face_distance)
        if matches[best_match_index]:
           name = known_face_names[best_match_index]

        # Create a rectangle on top of the face
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        # create a rectangle for name
        cv2.rectangle(frame,(left,bottom -35),(right,bottom),(0,0,255),cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,(255,255,255),1)
   cv2.imshow('Webcam_facerecognition',frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

video_capture.release()
cv2.destroyAllWindows()