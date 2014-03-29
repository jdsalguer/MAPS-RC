from __future__ import print_function
import time
import os
import sys
import json

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

jprint('msg', s)
jprint("msg","goodbye")
