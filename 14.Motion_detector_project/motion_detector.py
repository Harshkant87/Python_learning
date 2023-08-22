import cv2, pandas
from datetime import datetime

video = cv2.VideoCapture(0)
first_frame = None
status_list = []
time_list = []
df = pandas.DataFrame(columns = ["Start", "End"])

while True:
    check, frame = video.read()
    status = 0
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
        if cv2.contourArea(countour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    status_list.append(status)

    if len(status_list) >= 2 and status_list[-1] == 1 and status_list[-2] == 0:
        time_list.append(datetime.now())
    
    if len(status_list) >= 2 and status_list[-1] == 0 and status_list[-2] == 1:
        time_list.append(datetime.now())

    cv2.imshow("Capturing ", frame)
    cv2.imshow("Gray Frame ", gray)
    cv2.imshow(" Blurred Gray Frame ", blurred_gray)
    cv2.imshow("Delta Frame ", delta_frame)
    cv2.imshow("Threhold Delta Frame ", thresh_frame)

    key = cv2.waitKey(10) 

    if key == ord('q'):
        if status == 1: # in case script stops in between the object is present
            time_list.append(datetime.now())
        break

# print(time_list)
for i in range(0, len(time_list), 2):
    df = df.append({"Start": time_list[i], "End": time_list[i + 1]}, ignore_index = True)

df.to_csv("Time_stamps.csv") # you can open this .csv file in excel as well
video.release()
cv2.destroyAllWindows()