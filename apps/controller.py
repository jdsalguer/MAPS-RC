'''RES Controller'''
import motionSensor as mS
import motorControl as mC
import photocellManagement as pM
import ledManagement as lM
import ultrasonicSensor as uS
import temperatureSensor as tS
import time
import RPi.GPIO as GPIO
'''SETUP ALL THE PINS'''
#ultrasonic
trig = 10
echo = 8
#photoresistor
pr = 5
#gear motors
left1 = 21
left2 = 11
right1 = 16
right2 = 18
#motion sensor
motion = 3
#LEDs
red = 13 	#maybe
green = 19	#maybe
blue = 15	#maybe
rearl = 23
rearr = 26

uS.uSensorSetup(trig, echo)

pM.photoresistorSetup(pr)
mC.motorPins(left1, left2, right1, right2)
mS.PIRSetup(motion)
lM.ledSetup(red, green, blue, rearl, rearr)
'''get distance'''
def getDistance():
	return uS.distance()
'''turn light on'''
def lightON():
	lM.rgbActivate(lM.WHITE)
'''turn light off'''
def lightOFF():
	lM.rgbDeactivate(lM.WHITE)
'''flash green'''
def flashGreen():
	for i in range(5):
		lM.rgbActivate(lM.GREEN)
		time.sleep(.1)
		lM.rgbDeactivate(lM.GREEN)
		time.sleep(.1)
'''brake lights on'''
def brakeLightsON():
	lM.ledActivate(rearr)
	lM.ledActivate(rearl)
'''brake lights off'''
def brakeLightsOFF():
	lM.ledDeactivate(rearr)
	lM.ledDeactivate(rearl)
###########################################################################
#TESTING PURPOSES#
###########################################################################

'''
print 'testing motors'
mC.reverse()
time.sleep(2)
mC.off()

print 'testing brake lights'
for i in range(5):	
	brakeLightsON()
	time.sleep(.2)
	brakeLightsOFF()
	time.sleep(.2)

print 'testing the color white'
for i in range(5):	
	lightON()
	time.sleep(.2)
	lightOFF()
	time.sleep(.2)

print 'testing the color green'
for i in range(5):	
	flashGreen()

print 'testing the ultrasonic sensor'
for i in range(5):
	print  round(getDistance(), 2), 'cm'
	time.sleep(0.2)
print 'testing light'

for i in range(5):
	if pM.lightLevel() == 'Low':
		print 'low'
		lightON()
	else:
		if pM.lightLevel() =='High':
			print 'high'
			lightOFF()
	time.sleep(2)

'''
print 'testing the temperature'
for i in range(5):
	print 'Fahrenheit: ', tS.tempF(), ' Celcius: ', tS.tempC()



GPIO.cleanup()

######################################################################
#
######################################################################
"""
try:
	while true:
		'''if light is low turn light on'''
		if pM.lightLevel() == 'Low':
			lightON()
		'''if light is high turn light off'''
		if pM.lightLevel() == 'High':
			lightOFF()
		'''if motion detected flash green and get distance'''
		if mS.PIRReading():
			print 'I found somebody ' + getDistance() + 'cm away'
			flashGreen()
			if pM.lightLevel() == 'Low':
				lightON()
		'''if obstruction within 60 cm report obstruction and distance'''
		if getDistance() <= 60:
			print 'Theres something in front of me'
			print 'its kinda close: ' + getDistance() + 'cm' 
		'''if temperature above 100F report danger'''
		if tS.tempF() >= 100:
			print 'Its pretty hot here!!'
			print 'Fahrenhiet: ' + tS.tempF() + 'Celcius: ' + tS.tempC()
		'''when car is stopped turn on rear lights'''
		if (mC.LL == 0 & mC.LH == 0) || (mC.LL == 1 & mC.LH == 1) \
		   (mC.RL == 0 & mC.RH == 0) || (mC.RL == 1 & mC.RH == 1):
			time.sleep(0.1)
			'''so it doesnt blink on when going from forward to turning'''
			if (mC.LL == 0 & mC.LH == 0) || (mC.LL == 1 & mC.LH == 1) \
		   	   (mC.RL == 0 & mC.RH == 0) || (mC.RL == 1 & mC.RH == 1):	
				brakeLightsON()
		else if (mC.LL == 1 & mC.LH == 0) || (mC.LL == 0 & mC.LH == 1) \
		   	(mC.RL == 1 & mC.RH == 0) || (mC.RL == 0 & mC.RH == 1):
				brakeLightsOFF()


except KeyboardInterrupt:
	print 'boy that was a lot of work'
	GPIO.cleanup()
"""
