import RPi.GPIO as GPIO
from time import sleep 
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)

p3 = GPIO.PWM(16, 50)

p3.start(0)
pos=0
#p3.ChangeDutyCycle(50)
#print("hi")
a='z'
a=requests.get("http://54.160.238.67:5000/read")
print(a.json())

try:
    while True:
	print("Servo running")
	for pos in range(3,11):
		p3.ChangeDutyCycle(pos)  # turn towards 90 degree
        	sleep(0.1)
		print("catching")
	for pos in range(11,3):
		p3.ChangeDutyCycle(pos)  # turn towards 90 degree
        	sleep(0.1)
		print("opening")
        
except:
    p3.stop()
    GPIO.cleanup()