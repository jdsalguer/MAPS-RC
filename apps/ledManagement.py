import time
import RPi.GPIO as gpio

ledEnable = 1
ledDisable = 0
rgbEnable = 1
rgbDisable = 0

rgbred=0
rgbgreen=0
rgbblue=0
ledredl=0
ledredr=0
LED = []
RGB = []
RED = []
GREEN = []
BLUE = []
CYAN = []
MAGENTA = []
YELLOW = []
WHITE = []


gpio.setmode(gpio.BOARD)


def ledSetup(r, g, b, rl, rr):
	global rgbred
	global rgbgreen
	global rgbblue
	global ledredl
	global ledredr
	global LED
	global RGB
	global RED
	global GREEN
	global BLUE
	global CYAN
	global MAGENTA
	global YELLOW
	global WHITE
	

	rgbred = r
	rgbgreen = b 
	rgbblue = g
    	ledredl = rl
	ledredr = rr

	#GROUP THE LED PINS
	LED = [ledredl, ledredr]
	RGB = [rgbred, rgbgreen, rgbblue]

	#RGB COLORS
	RED = [rgbred]
	GREEN = [rgbgreen]
	BLUE = [rgbblue]
	CYAN = [rgbblue, rgbgreen]
	MAGENTA = [rgbblue, rgbred]
	YELLOW = [rgbgreen, rgbred]
	WHITE = [rgbred, rgbblue, rgbgreen]

	#print rgbred, rgbgreen, rgbblue, ledredl, ledredr
	#print LED
	#SETS UP EACH LED PIN FOR OUTPUT
	for i in LED:
		gpio.setup(i, gpio.OUT)
	for i in RGB:
		gpio.setup(i, gpio.OUT)


def ledActivate(led):
    	#TURNS ON THE LED COLOR OF CHOICE
   	gpio.output(led, ledEnable)

def rgbActivate(color):
    	#ACTIVATES THE COLOR  FOR THE RGB
	for i in color:
		gpio.output(i, rgbEnable)

def ledDeactivate(led):
	gpio.output(led, ledDisable)

def rgbDeactivate(color):
   	for i in color:
   		gpio.output(i, rgbDisable)

def ledClear():
  	# print 'clearing..'
	for j in LED:
		gpio.output(j, ledDisable)
	for j in RGB:
		gpio.output(j, rgbDisable)


