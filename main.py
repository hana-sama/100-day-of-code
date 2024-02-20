import cv2
import time
from datetime import datetime
from emailing import send_sns
import glob
import os
from threading import Thread
video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 1

def clean_folder():
    images = glob.glob('images/*.png')
    for image in images:
        os.remove(image)

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cv2.imshow('my_video', dil_frame)
    now = datetime.now()
    cv2.putText(img=dil_frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
    cv2.putText(img=dil_frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(244, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
    

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f'images/{count}.png', frame)
            count += 1
    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        all_images = sorted(glob.glob('images/*.png'))
        index = int(len(all_images) / 2)
        filepath = all_images[index]
        sns_thread = Thread(target=send_sns, args=(filepath,))
        sns_thread.daemon = True
        sns_thread.start()

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
clean_folder()