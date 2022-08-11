import RPi.GPIO as GPIO
import time
import signal
import sys

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
    GPIO.output(9, False)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True:
    # Red
    GPIO.output(9, True)
    print('red')
    time.sleep(3)
# Green
    GPIO.output(9, False)
    print('red out')
    time.sleep(1)

    GPIO.output(11, True)
    print('green')
    time.sleep(5)

    GPIO.output(11, False)
    print('green out')
    time.sleep(1)
GPIO.cleanup()