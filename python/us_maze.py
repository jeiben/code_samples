from gopigo import *
import time

enable_encoders()
enable_servo()

def turn_right():
  enc_tgt(1,0,14)
  time.sleep(.1)
  right()
  time.sleep(2)
  
def turn_left():
  enc_tgt(0,1,14)
  time.sleep(.1)
  left()
  time.sleep(2)

servo(90)
for i in range(20):
  while us_dist(15) > 20:
    fwd()
  stop()
  time.sleep(.5)
  servo(0)
  left_dist = us_dist(15)
  time.sleep(1)
  servo(180)
  right_dist = us_dist(15)
  time.sleep(1)
  servo(90)
  if left_dist < 20 and right_dist < 20:
    turn_left()
    turn_left()
  elif left_dist > right_dist:
    turn_left()
  else:
    turn_right()
  time.sleep(1)
