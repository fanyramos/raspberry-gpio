import RPi.GPIO as g

def pushNotification(pin,value):
  print pin, value

g.setmode(g.BCM)
g.setup(2, g.IN, pull_up_down=g.PUD_UP)
try:
  g.add_interrupt_callback(2, pushNotification, edge='rising',  pull_up_down=g.PUD_OFF, threaded_callback=True, debounce_timeout_ms=None)
  g.wait_for_interrupts(threaded=True)
except KeyboardInterrupt:
  g.clean
g.clean
