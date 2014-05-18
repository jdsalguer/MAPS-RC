import time
import motorControl as mC

####################################3
#testing
#################################
#left1 = 21
#left2 = 11
#right1 = 16
#right2 = 18

#mC.motorPins(left1, left2, right1, right2)
#Map()
#######################################

def Map():
	time.sleep(1)
	mC.turnRight()

	#how long to turn right 
	time.sleep(.4)

	mC.off()

	#how long to wait at 45 degrees
	time.sleep(3)

	mC.reverseLeft()

	#back to 90(neutral)
	time.sleep(.4)

	mC.off()

	#stay at 90 for a bit
	time.sleep(3)

	mC.turnLeft()

	#how long to turn left
	time.sleep(.4)

	mC.off()

	#how long to wait at -45 degrees
	time.sleep(3)

	mC.reverseRight()

	#back to neutral 
	time.sleep(.4)

	mC.off()

