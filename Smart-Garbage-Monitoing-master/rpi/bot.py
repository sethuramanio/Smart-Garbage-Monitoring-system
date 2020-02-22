import RPi.GPIO as GPIO
from time import sleep

#initialise motor gpio pins
motor1f=21
motor1b=20
motor2f=26
motor2b=16
a='z'

def setup():
	#setup gpio pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(motor1f,GPIO.OUT) 
	GPIO.setup(motor1b,GPIO.OUT)
	GPIO.setup(motor2f,GPIO.OUT)
	GPIO.setup(motor2b,GPIO.OUT)
	motor1f = GPTO.PWM(motor1f,100)
	motor2f = GPTO.PWM(motor2f,100)
	motor1b = GPTO.PWM(motor1b,100)
	motor2b = GPTO.PWM(motor2b,100)	

def readdb():
	dynamodbTable=dynamodb.Table('makeathon_control')
    	response = dynamodbTable.scan()
    	item=response
    	print(item)
    	a=item['Items'][0]['a']
   
 
def loop():
	#reads the database
	readdb()

	#moving front
	if (a=='w'):
		GPIO.output(motor1f,GPIO.HIGH)
		GPIO.output(motor1b,GPIO.LOW)
		GPIO.output(motor2f,GPIO.HIGH)
		GPIO.output(Motor2b,GPIO.LOW)

	#moving back
	if (a=='s'):
		GPIO.output(motor1b,GPIO.HIGH)
		GPIO.output(motor1f,GPIO.LOW)
		GPIO.output(motor2b,GPIO.HIGH)
		GPIO.output(Motor2f,GPIO.LOW)

	#moving right
	if (a=='d'):
		GPIO.output(motor1f,GPIO.HIGH)
		GPIO.output(motor1b,GPIO.LOW)
		GPIO.output(motor2f,GPIO.LOW)
		GPIO.output(Motor2b,GPIO.HIGH)
 
	#moving left
	if (a=='a'):
		GPIO.output(motor1b,GPIO.HIGH)
		GPIO.output(motor1f,GPIO.LOW)
		GPIO.output(motor2b,GPIO.LOW)
		GPIO.output(Motor2f,GPIO.HIGH)

	#stop
	if (a=='z'):
		GPIO.output(motor1b,GPIO.HIGH)
		GPIO.output(motor1f,GPIO.HIGH)
		GPIO.output(motor2b,GPIO.HIGH)
		GPIO.output(Motor2f,GPIO.HIGH)

loop()
