'''Motion Sensor'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
PIR = 0

def PIRSetup(pirPin):
	global PIR
	PIR = pirPin
	GPIO.setup(PIR, GPIO.IN)
	
def PIRReading():
	if GPIO.input(PIR) == 1:
		return True
	return False
	
