#! /usr/bin/python3
# non-blocking chatter demo #
#############################
# so occasionally the other thread will linger on std in
# and get that and then put the changed data back in the
# main process
import sys
import select
import time
import threading
import queue

instream = [sys.stdin]
# the timeout for maybe set to 0
# its a precausion for race conditions against the hardware
# example: data doesn't come in at the right time on the UART
timeout  = 0.01
baud_rate = 0.04
cmdQueue        = queue.Queue()
last_interrupt  = time.time()

'''print override for streamIO'''
def print(*args, **kwargs):
    __builtins__.print(*args, **kwargs)
    sys.stdout.flush()
    time.sleep(timeout)

def jprint(s1,s2):
  print('{"',s1,'":"',s2,'"}')

def jread():
  return sys.stdin.read().rstrip('\n')

# this is where input should be taken and inturperated into the 
# global commands that tell the robot what to do
# DO NOT PUT ANYTHING BLOCKING IN HERE
def handler(s):
  global last_interrupt
  jprint('handling',s)
  last_interrupt = time.time()

def MAIN_LOOP():
  global last_interrupt
  now = time.time()
  if now - last_interrupt > baud_rate:
    ### all the main stuff
    jprint('msg','running smooth')
    last_interrupt = now


# used to test if something got blocked and didn't run
# is called on a Ctrl-C
def cleanup():
  print()
  while not cmdQueue.empty():
    s = cmdQueue.get()
    jprint("could not execute", s)

#########################################################
# non-blocking stdin read using semaphore locked thread #
#########################################################
interrupted = threading.Lock()
interrupted.acquire()

def get_stdin():
  while (instream and not interrupted.acquire(blocking=False)):
    ready = select.select(instream, [], [], timeout)[0]
    for file in ready:
      s = file.readline().rstrip('\n')
      handler(s)
      if not s:
        instream.remove(file)
  jprint('msg','stdin was closed')

input_thread = threading.Thread(target=get_stdin)
input_thread.start()
#########################################################

try:
  while True:
    if cmdQueue.empty() and not input_thread.is_alive():
      break
    else:
      try:
        handler(cmdQueue.get(timeout=timeout))
      except queue.Empty:
        MAIN_LOOP()
except KeyboardInterrupt:
  cleanup()

interrupted.release() # kill child zombies! :D
jprint('status','not_running')
