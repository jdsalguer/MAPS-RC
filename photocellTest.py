'''Photocell Test'''

import photocellManagement as pM
import RPi.GPIO as GPIO

pinnum = 7
pM.photoresistorSetup(pinnum)
try:
	
	#while True:
	for num in range(0,8):
		print pM.photoresistorReading()
	
	
except KeyboardInterrupt:
	print 'There are you happy now??'
	GPIO.cleanup()
