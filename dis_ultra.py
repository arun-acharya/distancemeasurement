#Libraries
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 #set GPIO Pins
GPIO_TRIGGER = 18
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
def distance():
	    # set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, HIGH)
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, LOW)
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

allLedOff():
	GPIO.output(redLed, LOW)
	GPIO.output(greenLed, LOW)
	GPIO.output(yellowLed1, LOW)
	GPIO.output(yellowLed2, LOW)
	GPIO.output(buzzer, LOW)
oneLedOn():
	GPIO.output(redLed, HIGH)
	GPIO.output(greenLed, LOW)
	GPIO.output(yellowLed1, LOW)
	GPIO.output(yellowLed2, LOW)
	GPIO.output(buzzer, HIGH)
	time.seep(0.5)
	GPIO.output(buzzer, LOW)
twoLedOn():
	GPIO.output(redLed, HIGH)
	GPIO.output(yellowLed1, HIGH)
	GPIO.output(yellowLed2, LOW)
	GPIO.output(greenLed, LOW)

threeLedOn():
	GPIO.output(redLed, HIGH)
	GPIO.output(yellowLed1, HIGH)
	GPIO.output(yellowLed2, HIGH)
	GPIO.output(greenLed, LOW)

allLedOn():
	GPIO.output(redLed, HIGH)
	GPIO.output(yellowLed1, HIGH)
	GPIO.output(yellowLed2, HIGH)
	GPIO.output(greenLed, HIGH)

if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print ("Measured Distance = %.1f cm" % dist)
			if (distance<1):
				print("Distance too low")
				allLedOff()
			elif (distance>20):
				print("Distance too high")
				allLedOff()
			else:
				if (distance>=5):
					oneLedOn()
				elif(distance>=10):
					twoLedOn()
				elif(distance>=15):
					threeLedOn()
				else:
					allLedOn()
			time.sleep(1)
# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()
