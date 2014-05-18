'''Motor Test'''

import motorControl as MC
import time 
import RPi.GPIO as GPIO

#pin assignments
LL = 21#11
LH = 11#13
RL = 16#16
RH = 18#18

MC.motorPins(LL, LH, RL, RH)
#MC.motorSetup()
#print 'Starting test..'
time.sleep(2)
'''
print 'Testing left wheel forward'
#left wheel forward
MC.leftForward()
time.sleep(2)
MC.off()
'''

print ("Testing right wheel forward")
#right wheel forward
MC.rightForward()
time.sleep(5)
MC.off()
'''
print 'Testing left wheel reverse'
#left wheel reverse
MC.leftReverse
time.sleep(2)
MC.off()
print 'Testing right wheel reverse'
#right wheel reverse
MC.rightReverse
time.sleep(2)
MC.off()

print 'Testing both wheels forward'
#both wheels forward
MC.forward()
time.sleep(2)
MC.off()
''''''
print 'Testing both wheels reverse'
#both wheels reverse
MC.reverse()
time.sleep(2)
MC.off()
''''''
print 'Testing turning right'
#turn right
MC.turnRight()
time.sleep(2)
MC.off()
print 'Testing turning left'
#turn left
MC.turnLeft()
time.sleep(2)
MC.off()
'''
print ('Testing Complete.. exiting in 2 seconds.')
time.sleep(2)
GPIO.cleanup()
