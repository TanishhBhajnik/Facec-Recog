import cv2
import face_recognition
from simple_facerec import SimpleFacerec

# joey1 = cv2.imread("Joey1.webp")
# rgb_img = cv2.cvtColor(joey1, cv2.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)[0]
#
# chan = cv2.imread("images/chandler.jpg")
# rgb_img2 = cv2.cvtColor(chan, cv2.COLOR_BGR2RGB)
# img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
#
# joey = cv2.imread("images/joey.jpg")
# rgb_img3 = cv2.cvtColor(joey, cv2.COLOR_BGR2RGB)
# img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]
#
# result = face_recognition.compare_faces([img_encoding], img_encoding3)
# print("Result: ", result)
#
# cv2.imshow("JOEY1", joey1)
# cv2.imshow("Chandler", joey)
# cv2.waitKey(0)

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
z

cap = cv2.VideoCapture(0)
# print("Camera working")

while True:
    ret, frame = cap.read()

    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1,y1- 10), cv2.FONT_HERSHEY_DUPLEX, 1 , (0,0,200),2)
        cv2.rectangle(frame , (x1,y1), (x2,y2), (0,0,200), 4)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

