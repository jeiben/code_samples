from gopigo import *
import time

while True:
  val = int(raw_input())
  if val < or val > 180:
    print "Invalid angle - please enter an integer between 0 and 180"
  else:
    print "Turning servo to %s degrees..." %(val)
    servo(val)
    time.sleep(1)
  
  
