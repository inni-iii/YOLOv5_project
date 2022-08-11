import socket
import RPi.GPIO as GPIO
import time
import signal
import sys
from signal import signal, SIGPIPE, SIG_DFL

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

signal(SIGPIPE, SIG_DFL)
#connect server
HOST = '192.168.137.160'
PORT = 12345
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

# Turn off all lights when user ends demo
'''def allLightsOff(signal, frame):
    GPIO.output(9, False)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)'''

# Loop forever
while True:
    # Red
    RED = GPIO.output(9, True)
    print('red')
    time.sleep(20)
# Green
    GREEN = GPIO.output(9, False)
    print('red out')
    s.send('red out'.encode())
    print(f'>{(s.recv(1024)).decode()}')
    time.sleep(1)

    GPIO.output(11, True)
    print('green')
    time.sleep(40)

    GPIO.output(11, False)
    print('green out')
    s.send('green out'.encode())
    print(f'>{(s.recv(1024)).decode()}')
    time.sleep(1)
    #socket.setblocking(False)
GPIO.cleanup()    