import RPi.GPIO as GPIO 
from time import sleep 
import requests

GPIO.setmode(GPIO.BCM) # GPIO numbering
GPIO.setwarnings(False) # enable warning from GPIO

AN2 = 17 # set pwm2 pin on MDDS10 to GPIO 25
AN1 = 18 # set pwm1 pin on MDDS10 to GPIO 24
DIG2 = 22 # set dir2 pin on MDDS10 to GPIO 23
DIG1 = 23 # set dir1 pin on MDDS10 to GPIO 18

GPIO.setup(AN2, GPIO.OUT) # set pin as output
GPIO.setup(AN1, GPIO.OUT) # set pin as output
GPIO.setup(DIG2, GPIO.OUT) # set pin as output
GPIO.setup(DIG1, GPIO.OUT) # set pin as output
GPIO.setup(16,GPIO.OUT)

sleep(1) # delay for 1 seconds


p1 = GPIO.PWM(AN1, 100) # set pwm for M1
p2 = GPIO.PWM(AN2, 100) # set pwm for M2
p3 = GPIO.PWM(16, 50)
p3.start(0)
pos=0


print("*******Hackhub VIT Chennai*******")

try:
    while True:

        #For forward function, insert:
	    
	    a=requests.get("http://54.160.238.67:5000/read")
            s=a.json()
	    print(s['dir'])
           
	    if (s['dir']=='a'):
            	print ("Left")
            	GPIO.output(DIG1, GPIO.HIGH) # set DIG1 as high, dir2 = forward
            	GPIO.output(DIG2, GPIO.HIGH) # set DIG2 as high, dir1 = forward
            	p1.start(70) # set speed for M1, speed=0 - 100
            	p2.start(70) # set speed for M2, speed=0 - 100
            	sleep(2) # delay for 1 seconds

            #For backward function, insert:
	    if (s['dir']=='d'):
           
            	print ("Right")
            	GPIO.output(DIG1, GPIO.LOW) # set DIG1 as low, DIR = backward
            	GPIO.output(DIG2, GPIO.LOW) # set DIG2 as low, DIR = backward
            	p1.start(70) # set speed for M1, speed=0 - 100
            	p2.start(70) # set speed for M2, speed=0 - 100
            	sleep(2) # delay for 1 seconds

            #For left:
	    if (s['dir']=='s'):

            	print ("Backward")
            	GPIO.output(DIG1, GPIO.LOW) # set DIG1 as low, dir2 = backward
            	GPIO.output(DIG2, GPIO.HIGH) # set DIG2 as high, dir1 = forward
            	p1.start(40) # set speed for M1
            	p2.start(40) # set speed for M2
            	sleep(2) # delay for 1 seconds

            #For right:
	
            if (s['dir']=='w'):
            	print ("Forward")
            	GPIO.output(DIG1, GPIO.HIGH) # set DIG1 as high, dir1 = forward
            	GPIO.output(DIG2, GPIO.LOW) # set DIG2 as low, dir2 = backward
            	p1.start(40) # set speed for M1
            	p2.start(40) # set speed for M2,
            	sleep(2) # delay for 1 seconds

	    if (s['dir']=='x'):
		print("**STOP***")
		p1.start(0)
	        p2.start(0)
		sleep(2)
	    if (s['stat']=='p'):
		requests.get("http://54.160.238.67:5000/stat")
		print("Servo running")
		for pos in range(3,11):
			p3.ChangeDutyCycle(pos)  # turn towards 90 degree
        		sleep(0.1)
			print("catching")
		
	    if (s['stat']=='d'):
		requests.post("http://54.160.238.67:5000/stat")
		for pos in range(11,3):
			p3.ChangeDutyCycle(pos)  # turn towards 90 degree
        		sleep(0.1)
			print("opening")
		
		




except KeyboardInterrupt:
    p3.stop()
    GPIO.cleanup()
    p1.start(0)
    p2.start(0)

finally:
    print("YOOO!!!")
