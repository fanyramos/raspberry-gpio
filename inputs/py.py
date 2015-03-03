import RPi.GPIO as g
import sys
import time

g.setmode(g.BCM)

## lsb pins
g.setup(21,g.IN, pull_up_down=g.PUD_DOWN)
g.setup(20,g.IN, pull_up_down=g.PUD_DOWN)
g.setup(16,g.IN, pull_up_down=g.PUD_DOWN)
g.setup(26,g.IN, pull_up_down=g.PUD_DOWN)


## msb pins
g.setup(19,g.IN, pull_up_down=g.PUD_DOWN)
g.setup(13,g.IN, pull_up_down=g.PUD_DOWN)
g.setup(6,g.IN, pull_up_down=g.PUD_DOWN)
g.setup(5,g.IN, pull_up_down=g.PUD_DOWN)


while True:
  print "[", g.input(21), g.input(20), g.input(16), g.input(26), g.input(19), g.input(13), g.input(6), g.input(5), "]"
  time.sleep(0.5)

g.cleanup()

