import cv2

video = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, blurred_gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, 
                                 cv2.CHAIN_APPROX_SIMPLE)
    
    for countour in cnts:
        if cv2.contourArea(countour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Capturing ", frame)
    cv2.imshow("Gray Frame ", gray)
    cv2.imshow(" Blurred Gray Frame ", blurred_gray)
    cv2.imshow("Delta Frame ", delta_frame)
    cv2.imshow("Threhold Delta Frame ", thresh_frame)
    key = cv2.waitKey(10) 

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()