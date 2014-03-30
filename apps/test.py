from __future__ import print_function
import time
#import os
import sys
#import json
import select

'''print override for streamIO'''
def print(*args, **kwargs):
    __builtins__.print(*args, **kwargs)
    sys.stdout.flush()
    time.sleep(0.05)

def jprint(s1,s2):
	print('{"',s1,'":"',s2,'"}')

def jread():
	return sys.stdin.read().rstrip('\n')

for num in range(0,8):
    jprint("test", num)

jprint('msg','enter something')
s = jread()

if s == "will you be my friend":
	jprint('msg',"yes! i'd love to be your friend because you're so cool... NOT!")
	time.sleep(3)
else:
	jprint('msg', s)

jprint('action','well im going to start my main loop and read from stdin without blocking')

#while True:
while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
	line = jread()#sys.stdin.readline()
	if line:
		jprint('input',line)
	#else:
	#	jprint('stdin','the stream has been broken')
	#	exit(0)
else:
	time.sleep(0.01)


jprint("msg","goodbye")
