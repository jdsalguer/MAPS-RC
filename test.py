#!/usr/bin/env python

from __future__ import print_function
import time
import os
import sys
'''sys.stdout = os.fdopen(0, 'w', 0)'''


for num in range(0,8):
	sys.stdout.write("hello\n")

	#print('my []-- ', num)
	time.sleep(1.2)
	sys.stdout.flush()