#Libraries
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("Starting the program")
 #set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24

totalDistance = 20
redLed = 6 
greenLed = 26 
yellowLed1 = 19
yellowLed2 = 13
buzzer = 5
 #set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#set GPIO direction OUT to LED
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(yellowLed1, GPIO.OUT)
GPIO.setup(yellowLed2, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
def getdistance():
	    # set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, GPIO.LOW)
 	StartTime = time.time()
	StopTime = time.time()
	# save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
    # save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
    # time difference between start and arrival
		TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2
	return distance

def allLedOff():
	GPIO.output(redLed, GPIO.LOW)
	GPIO.output(greenLed, GPIO.LOW)
	GPIO.output(yellowLed1, GPIO.LOW)
	GPIO.output(yellowLed2, GPIO.LOW)
	GPIO.output(buzzer, GPIO.LOW)
def oneLedOn():
	GPIO.output(redLed, GPIO.HIGH)
	GPIO.output(greenLed, GPIO.LOW)
	GPIO.output(yellowLed1, GPIO.LOW)
	GPIO.output(yellowLed2, GPIO.LOW)
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(buzzer, GPIO.LOW)
def twoLedOn():
	GPIO.output(redLed, GPIO.HIGH)
	GPIO.output(yellowLed1, GPIO.HIGH)
	GPIO.output(yellowLed2, GPIO.LOW)
	GPIO.output(greenLed, GPIO.LOW)

def threeLedOn():
	GPIO.output(redLed, GPIO.HIGH)
	GPIO.output(yellowLed1, GPIO.HIGH)
	GPIO.output(yellowLed2, GPIO.HIGH)
	GPIO.output(greenLed, GPIO.LOW)

def allLedOn():
	GPIO.output(redLed, GPIO.HIGH)
	GPIO.output(yellowLed1, GPIO.HIGH)
	GPIO.output(yellowLed2, GPIO.HIGH)
	GPIO.output(greenLed, GPIO.HIGH)

try:
	while True:
		dist = getdistance()
		print ("Measured Distance = %.1f cm" % dist)
		if (dist<1):
			print("Distance too low")
			allLedOff()
		elif (dist>20):
			print("Distance too high")
			allLedOff()
		else:
			if (dist>=5):
				oneLedOn()
			elif(dist>=10):
				twoLedOn()
			elif(dist>=15):
				threeLedOn()
			else:
				allLedOn()
		time.sleep(1)
# Reset by pressing CTRL + C
except KeyboardInterrupt:
	print("Measurement stopped by User")
	GPIO.cleanup()
