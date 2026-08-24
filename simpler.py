import RPi.GPIO as GPIO
import time

STEP = 3
DIR = 5

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(DIR, GPIO.HIGH)

try:
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
