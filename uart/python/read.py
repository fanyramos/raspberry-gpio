import serial
import time
import re
import RPi.GPIO as gpio

on_regex = re.compile("^\s*\b\d{1,2}\b(?:\s*\,?\s*\b\d{1,2}\b)*\s*$")
avaliable_pins = [18,23,24,25,8,7,12,16,21,26]

def gpio_setup():
  gpio.setmode(gpio.BCM)
  for pin in avaliable_pins:
    gpio.setup(pin,gpio.OUT)

# def turn_on_all(gpio_pins):

# def turn_on_all_but(gpio_pins):

# def flash_error():


def evaluate_arguments(argv):
  if (on_regex.match(argv)):
    to_turn_on_pins = list(set([x for x in str.replace(",", " ").split(" ") if x != ""]))
    print to_turn_on_pins


try:
  port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=None)
  gpio_setup()
  while 1:
    data_chunk = port.read()           # Wait forever for anything
    time.sleep(0.1)              # Sleep (or inWaiting() doesn't give the correct value)
    remaining_bytes = port.inWaiting()  # Get the number of characters ready to be read
    data_chunk += port.read(remaining_bytes) # Do the read and combine it with the first character
    evaluate_arguments(data_chunk)
except Exception:
  gpio.cleanup()

gpio.cleanup()
