import RPi.GPIO as g
import time
import sys

PIN = int(sys.argv[1])

g.setmode(g.BCM)
g.setup(PIN,g.OUT)

if "delay" in sys.argv:
	delay()
else:
	nodelay()


def nodelay():
	g.output(PIN,1)
	g.output(PIN,0)

def delay():
	import time
	while True:
		time.sleep(1)
		g.output(PIN,1)
		time.sleep(1)
		g.output(PIN,0)
