'''Ultrasonic sensor'''

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
trig = 0
echo = 0

def uSensorSetup(tr, ec):
	global trig
	global echo
	trig = tr
	echo = ec
	GPIO.setup(trig, GPIO.OUT)
	GPIO.output(trig, GPIO.LOW)
	GPIO.setup(echo, GPIO.IN)
	time.sleep(0.5)

def distance():
	
	#print 'Starting Measurment..'
	#send a 10 microsecond pulse
	GPIO.output(trig, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(trig, GPIO.LOW)

	while GPIO.input(echo) == 0:
		pass	
	start = time.time()

	while GPIO.input(echo) == 1:
		pass
	stop  = time.time()
	#take the difference in time and multiply it by the speed of sound (340m/s)
	#divided by 2 as the distance will be from here to there and there to here
	#times 100 to convert to centimeters. 
	distance = (stop - start) * 17000

	return distance


