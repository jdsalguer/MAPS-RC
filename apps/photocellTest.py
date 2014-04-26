'''Photocell Test'''

import photocellManagement as pM, time
import RPi.GPIO as GPIO

pinnum = 11
pM.photoresistorSetup(pinnum)
average = 0



for i in range(10):
	average = 0
	pM.count = 0
	j=0
	for j in range(100):
		new = pM.photoresistorReading()
		average = pM.runningSum(average,new)
	
	print 200.0 / average * 100.0
 	


GPIO.cleanup()
