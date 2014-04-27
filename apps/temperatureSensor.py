''' Temperature Sensor'''

import time
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

filedir = '/sys/bus/w1/devices/28-000005b5b540/w1_slave'

def tempReading():

	file = open(filedir, 'r')
	filelines = file.readlines()
	file.close()

	
	while filelines[0].strip()[-3:] != 'YES': 
		time.sleep(0.5)	
		print 'in the loop'		
		tempReading()			
	
	equalsign = filelines[1].find('t=')
	if equalsign == -1:
		time.sleep(0.5)
		print 'in the if'
		tempReading()
	tempstring = filelines[1][equalsign+2:]
	return tempstring
	
def tempF():
	return tempC() * (9.0/5.0) +32

def tempC():
	tempstring = tempReading()
	return float(tempstring) / 1000



