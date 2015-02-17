import RPi.GPIO as g
import sys
from time import sleep
pin1 = int(sys.argv[1])
pin2 = int(sys.argv[2])

def pushNotification(channel):
  print channel

g.setmode(g.BCM)
g.setup(pin1,g.OUT)
g.setup(pin2, g.IN, pull_up_down=g.PUD_DOWN)

try:
  g.add_event_detect(pin2, g.BOTH, callback=pushNotification)

  while True:
    sleep(0.5)
    g.output(pin1,g.HIGH)
    sleep(0.5)
    g.output(pin1,g.LOW)

except KeyboardInterrupt:
  g.cleanup()

g.cleanup()
