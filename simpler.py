import RPi.GPIO as GPIO
import time

STEP = 11
DIR = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

GPIO.output(DIR, 1)

while True:
    GPIO.output(STEP, 1)
    print("HIGH")
    time.sleep(1)

    GPIO.output(STEP, 0)
    print("LOW")
    time.sleep(1)