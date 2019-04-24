from picamera import PiCamera
import time
from darkflow.net.build import TFNet
import cv2
import pyttsx3
import glob
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24
print("DMIP")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print("Waiting for Sesor To settle")
time.sleep(2)
options = {"model": "cfg/yolov2-tiny.cfg", "load":"bin/yolov2-tiny.weights", "threshold": 0.5}
tfnet=TFNet(options)
camera=PiCamera()
engine=pyttsx3.init()
camera.start_preview()
time.sleep(5)
try:
    while True:
        camera.capture("/home/pi/darkflow/sample_img/a.jpg")
        imgcv = cv2.imread("/home/pi/darkflow/sample_img/a.jpg")
        #camera.stop_preview()
        #os.chdir("/home/darkflow/darkflow/net")
        print("Done")
        res=tfnet.return_predict(imgcv)
        print(res)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        pulse_start=time.time()
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
        pulse_end=time.time()
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration * 17150
        distance = round(distance,2)
        print("Distance:",distance,"cm")
        os.remove("/home/pi/darkflow/sample_img/a.jpg")
        engine.say(res)
        engine.say(distance)
        engine.say("centimeters")
        engine.runAndWait()
except KeyboardInterrupt:
    camera.stop_preview()
    pass
