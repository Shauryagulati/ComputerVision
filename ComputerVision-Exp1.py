import cv2
import time

pTime=0
cap = cv2.VideoCapture("/Users/shauryagulati/Documents/VSCode/Snowfall.mp4")

while True:
  success, img = cap.read()
  cTime=time.time()
  fps=1/(cTime-pTime)
  pTime=cTime
  cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
  cv2.imshow("Result", img)
  if cv2.waitKey(1) and 0xFF == ord('q'):
    break