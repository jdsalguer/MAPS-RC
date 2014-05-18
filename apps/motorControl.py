''' Motor Control'''
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
LL = 0
LH = 0
RL = 0
RH = 0

#must be called prior to any other fucntion to assign the pin values
def motorPins(leftLo, leftHi, rightLo, rightHi):
	global LL 
	global LH 
	global RL
	global RH
	LL = leftLo
	LH = leftHi
	RL = rightLo
	RH = rightHi
	motorSetup()
#must be called prior to anything further
def motorSetup():
	#Sets the pins to output
	GPIO.setup(LL, GPIO.OUT)
	GPIO.setup(LH, GPIO.OUT)
	GPIO.setup(RL, GPIO.OUT)
	GPIO.setup(RH, GPIO.OUT)

def turnRight():
	#Stops the right wheel and forwards the left to turn right
	leftoff()
	rightForward()
def turnLeft():
	#Stops the left wheel and forwards the right to turn left 
	leftForward()
	rightoff()

def rotateRight():
	#Reverses the right wheel and forwards the left to turn right
	leftForward()
	rightReverse()
def rotateLeft():
	#Reverses the left wheel and forwards the right to turn left 
	leftReverse()
	rightForward()
def reverseLeft():
	#Stops the left wheel and reverse the right to reverse left
	rightReverse()
	leftoff()
def reverseRight():
	#Stops the right wheel and reverse the left to reverse left
	leftReverse()
	rightoff()
def forward():
	#Turns both left and right wheel forward
	leftForward()
	rightForward()
def reverse():
	#Turns both left and right wheel reverse
	leftReverse()
	rightReverse()

def leftForward():
	GPIO.output(LL, 0)
	GPIO.output(LH, 1)
def leftReverse():
	GPIO.output(LL, 1)
	GPIO.output(LH, 0)
def rightForward():
	GPIO.output(RL, 0)
	GPIO.output(RH, 1)
def rightReverse():
	GPIO.output(RL, 1)
	GPIO.output(RH, 0)
	
def off():
	GPIO.output(LL, 0)
	GPIO.output(LH, 0)
	GPIO.output(RL, 0)
	GPIO.output(RH, 0)
def leftoff():
	GPIO.output(LL, 0)
	GPIO.output(LH, 0)
def rightoff():
	GPIO.output(RL, 0)
	GPIO.output(RH, 0)
