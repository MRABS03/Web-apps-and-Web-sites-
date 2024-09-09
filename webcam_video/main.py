import streamlit as st
import cv2
from datetime import datetime as dt

st.title("WEBCAM")
start = st.button("Start")

if start:
    streamlit_image = st.image([])
    video = cv2.VideoCapture(0)

    while True:
        timestamp = []
        current_datetime = dt.now()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_month = current_datetime.strftime("%B")
        check, frame = video.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        cv2.putText(frame, text=current_time, org=(25, 25), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=1, color=(255, 255, 255), thickness=2,
                    lineType=cv2.LINE_AA)
        cv2.putText(frame, text=current_month, org=(25, 60), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255, 0, 0), thickness=5,
                    lineType=cv2.LINE_AA)
        streamlit_image.image(frame)
