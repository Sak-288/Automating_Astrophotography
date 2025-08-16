import RPi.GPIO as GPIO
import time

# Pin Definitions
DIR = 20   # Direction pin
STEP = 21  # Step pin
MS1 = 14   # Microstepping pin 1
MS2 = 15   # Microstepping pin 2
MS3 = 18   # Microstepping pin 3

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# Set motor direction
GPIO.output(DIR, GPIO.HIGH)

# Full step (max torque)
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)
GPIO.output(MS3, GPIO.LOW)

# Motor parameters
DEGREES_PER_STEP = 1.8
TARGET_ANGLE = 90
nSteps = int(TARGET_ANGLE / DEGREES_PER_STEP)

# Ramp parameters
start_delay = 0.01   # slow at start (100 Hz)
min_delay   = 0.001  # max speed (~500 Hz)
accel_steps = 20     # number of steps to accelerate/decelerate

def step_motor(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

print(f"Moving {TARGET_ANGLE} degrees, {nSteps} steps.")

# --- Ramp up ---
for i in range(accel_steps):
    # interpolate between start_delay and min_delay
    d = start_delay - (i / accel_steps) * (start_delay - min_delay)
    step_motor(d)

# --- Constant speed ---
for i in range(nSteps - 2*accel_steps):
    step_motor(min_delay)

# --- Ramp down ---
for i in range(accel_steps):
    d = min_delay + (i / accel_steps) * (start_delay - min_delay)
    step_motor(d)

print("Movement complete. Cleaning up GPIO.")
GPIO.cleanup()
