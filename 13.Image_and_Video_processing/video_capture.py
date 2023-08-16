import cv2

video = cv2.VideoCapture(0) #using only videocam
frame_num = 0
while True:
    frame_num = frame_num + 1
    check, frame = video.read()

    cv2.imshow("Capturing ", frame)
    key = cv2.waitKey(10) # lesser the number smoother the video

    if key == ord('q'): #pressing the key 'q' will stop the execution
        break

print("Total number of frames: ", frame_num)
video.release()
cv2.destroyAllWindows()