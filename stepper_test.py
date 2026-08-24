import RPi.GPIO as GPIO
import time

# GPIO pin setup
STEP_PIN = 3
DIR_PIN = 5
ENABLE_PIN = 16

# Step delay
DELAY = 0.001  # smaller = faster

# Delay after changing direction
DIR_DELAY = 0.005  # 5 ms

# Number of steps
STEPS = 200  # typical full rotation for NEMA17

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Enable driver (LOW = enabled on TMC2209/A4988)
GPIO.output(ENABLE_PIN, GPIO.LOW)


def move_steps(steps, direction):
    # Set direction
    GPIO.output(DIR_PIN, direction)

    # IMPORTANT:
    # Give driver time to register direction change
    time.sleep(DIR_DELAY)

    # Generate step pulses
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
