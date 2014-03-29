#stdio chatter test#
####################

import time
import os
import sys
#sys.stdout = os.fdopen(0, 'w', 0)

for num in range(0,3):
	print ("this is my")
	sys.stdout.flush()
	time.sleep(1)
	