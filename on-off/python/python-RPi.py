def nodelay():
	while True:
		g.output(PIN,1)
		g.output(PIN,0)

def delay():
	import time
	while True:
		time.sleep(DELAY)
		g.output(PIN,1)
		time.sleep(DELAY)
		g.output(PIN,0)

import RPi.GPIO as g
import sys

PIN = int(sys.argv[1])
DELAY = int(sys.argv[len(sys.argv)-1])
g.setmode(g.BCM)
g.setup(PIN,g.OUT)

if "delay" in sys.argv:
	delay()
else:
	nodelay()
