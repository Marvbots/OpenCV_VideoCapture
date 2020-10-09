
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(5, 30)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('testing_12.avi', fourcc, 30, (1280, 720))

while True:
    ret, frame = cap.read()
    if ret is True:
        b = cv2.resize(frame, (1280, 720), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        out.write(b)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
