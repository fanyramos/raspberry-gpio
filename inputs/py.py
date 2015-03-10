import RPi.GPIO as g
import sys
import time

digitalInputs[]

def pipePins():
  for i in xrange(10):
    lsb0 = g.input(21)
    lsb1 = g.input(20)
    lsb2 = g.input(16)
    lsb3 = g.input(26)
    msb4 = g.input(19)
    msb5 = g.input(13)
    msb6 = g.input(6)
    msb7 = g.input(5)
    input = [msb7,msb6,msb5,msb4,lsb3,lsb2,lsb1,lsb0]
    digitalInputs.append(input)
  for input in digitalInputs:
    g.output(7,input[0])
    g.output(8,input[1])
    g.output(25,input[2])
    g.output(24,input[3])
    g.output(23,input[4])
    g.output(18,input[5])
    g.output(15,input[6])
    g.output(14,input[7])
  print digitalInputs


import RPi.GPIO as g
import sys
import time

g.setmode(g.BCM)

#################
####  Inputs  ###
#################
## lsb pins
g.setup(21,g.IN)
g.setup(20,g.IN)
g.setup(16,g.IN)
g.setup(26,g.IN)
## msb pins
g.setup(19,g.IN)
g.setup(13,g.IN)
g.setup(6,g.IN)
g.setup(5,g.IN)


g.setup(4,g.IN, pull_up_down=g.PUD_UP)

#################
####  Outputs ###
#################

g.setup(7,g.OUT)
g.setup(8,g.OUT)
g.setup(25,g.OUT)
g.setup(24,g.OUT)
## msb pins
g.setup(23,g.OUT)
g.setup(18,g.OUT)
g.setup(15,g.OUT)
g.setup(14,g.OUT)

while True:
  try:
     if g.input(4) == False:
     pipePins()
#    time.sleep(0.1)
  except KeyboardInterrupt:
  g.cleanup()

