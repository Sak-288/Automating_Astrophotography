import RPi.GPIO as GPIO
import time

# --- Broches GPIO (BOARD numbering)
DIR = 38    # Direction pin
STEP = 40   # Step pin
MS1 = 8     # Microstep pin 1
MS2 = 10    # Microstep pin 2
MS3 = 12    # Microstep pin 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# --- Config microstepping : FULL STEP (max torque)
GPIO.output(MS1, GPIO.HIGH)
GPIO.output(MS2, GPIO.HIGH)
GPIO.output(MS3, GPIO.HIGH)

# --- Motor parameters
DEGREES_PER_STEP = 1.8/16
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)

# --- Movement
TARGET_ANGLE = 180
nSteps = int(TARGET_ANGLE / DEGREES_PER_STEP)
print(f"Moving {TARGET_ANGLE}°, which is {nSteps} full steps.")

# --- Step function
def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

try:
    GPIO.output(DIR, GPIO.HIGH)  # Set direction

    delay = 0.2  # initial speed (~50 Hz)

    for i in range(nSteps):
        step(delay)

finally:
    GPIO.cleanup()
    print("Movement finished.")
