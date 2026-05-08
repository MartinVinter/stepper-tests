import RPi.GPIO as GPIO
import time

# GPIO pin setup
STEP_PIN = 12
DIR_PIN = 11
ENABLE_PIN = 16

# Step delay
DELAY = 0.001  # smaller = faster

# Number of steps
STEPS = 200  # typical full rotation for NEMA17

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Enable driver (LOW = enabled on A4988)
GPIO.output(ENABLE_PIN, GPIO.LOW)

def move_steps(steps, direction):
    GPIO.output(DIR_PIN, direction)

    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)

        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)

try:
    while True:
        print("Moving clockwise")
        move_steps(STEPS, GPIO.HIGH)

        time.sleep(1)

        print("Moving counter-clockwise")
        move_steps(STEPS, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping")

finally:
    # Disable driver
    GPIO.output(ENABLE_PIN, GPIO.HIGH)

    GPIO.cleanup()