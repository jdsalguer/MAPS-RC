import time
import RPi.GPIO as GPIO

rgbred=0
rgbgreen=0
rgbblue=0
ledredl=0
ledredr=0
GPIO.setmode(GPIO.BOARD)
def ledSetup(r, g, b, rl, rr):
	global rgbred
	global rgbgreen
	global rgbblue
	global ledredl
	global ledredr
	rgbred = r
	rgbgreen = b 
	rgbblue = g
	ledredl = rl
	ledredr = rr

	GPIO.setup(rgbred, GPIO.OUT)
	GPIO.setup(rgbblue, GPIO.OUT)
	GPIO.setup(rgbgreen, GPIO.OUT)
	GPIO.setup(ledredl, GPIO.OUT)
	GPIO.setup(ledredr, GPIO.OUT)

def blueON():
	GPIO.output(rgbblue, 1)
def greenON():
	GPIO.output(rgbgreen, 1)
def redON():
	GPIO.output(rgbred, 1)
def brakesON():
	GPIO.output(ledredr, 1)
	GPIO.output(ledredl, 1)
def whiteON():
	blueON()
	greenON()
	redON()

def blueOFF():
	GPIO.output(rgbblue, 0)
def greenOFF():
	GPIO.output(rgbgreen, 0)
def redOFF():
	GPIO.output(rgbred, 0)
def brakesOFF():
	GPIO.output(ledredr, 0)
	GPIO.output(ledredl, 0)
def whiteOFF():
	blueOFF()
	greenOFF()
	redOFF()