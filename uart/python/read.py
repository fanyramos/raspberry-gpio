import serial
import time
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=None)

while 1:
  tdata = port.read()           # Wait forever for anything
  time.sleep(0.1)              # Sleep (or inWaiting() doesn't give the correct value)
  remaining_bytes = port.inWaiting()  # Get the number of characters ready to be read
  tdata += port.read(remaining_bytes) # Do the read and combine it with the first character
  print tdata
