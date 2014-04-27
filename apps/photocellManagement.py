'''Photocell Management'''
'''
	The way this code works is that combines the GPIO pin into a circuit
	that includes the photoressitor and a capacitor. 3.3v to the photoresistor 
	on one end and the positive side of the capacitor on the other with gnd attacthed 
	at the other end of the capacitor. In this ciruit the pin form the board is
	connected btween the two and outputs a LOW generally 0v.
	The pin is then changed to an input pin and we measure through some unit of time 
	how long it takes for the discharge from the capacitor to get above 0.7v to a HIGH state around 1.4 v on the pin 
	as all the voltage left after going through the resistor (VARYING RESISTOR DUE TO THE 
	AMOUNT OF LIGHT) was collected in the capacitor as well as whaever is coming through past 
	the resistor.
	
	In short:
		Lots of light = Low resistance -> more voltage goes to the capacitor faster
							->capacitor discharges into gpio pin faster
							-> our value is small
		Little to no light = High resistance -> less voltage goes to the capacitor
							-> capacitor discharges what it can into pin and reamainder from 3.3 passing through
							->takes a while for pin to reach past a low state
							->our value is large
'''
import RPi.GPIO as GPIO , time, datetime

#must be called prior to any other function to assign the pin value

PR = 0
GPIO.setmode(GPIO.BOARD)

count = 0 

def photoresistorSetup(lightSensor):
	global PR 
	PR = lightSensor
	
def photoresistorReading():
    value = 0
    GPIO.setup(PR, GPIO.OUT)
    GPIO.output(PR, GPIO.LOW)
 
    GPIO.setup(PR, GPIO.IN)
    while (GPIO.input(PR) == GPIO.LOW):
        value += 1

    return value


def runningSum(avg,new):
        global count
        count+=1
        avg-=avg/count
        avg+=new/count

        return avg

def lightLevel():
        global count        
        count = 0
        average = 0
        j = 0

        for j in range(100):
	        new = photoresistorReading()
	        average = runningSum(average,new)
        
        percent = 200.0 /average * 100.0


        print percent
        if percent < 570: #theres little light in the room 
                return 'Low'
        else:           #there is enough light in a room
                return 'High'

