import RPi.GPIO as GPIO
GPIO.setwarnings(False) # Add this line to the top of your script
import time

# Pin Definitions
DIR = 20  # Direction pin
STEP = 21 # Step pin
MS1 = 14  # Microstepping pin 1
MS2 = 15  # Microstepping pin 2
MS3 = 18  # Microstepping pin 3

# Set the GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Setup all pins as outputs
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# Set motor direction (HIGH for one direction, LOW for the other)
GPIO.output(DIR, GPIO.HIGH)

# Set microstepping to full-step mode (all LOW)
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)
GPIO.output(MS3, GPIO.LOW)

# Define motor parameters
# A typical stepper motor has 200 steps per revolution (360 / 1.8 = 200)
DEGREES_PER_STEP = 1.8
TARGET_ANGLE = 90
STEPS_PER_REVOLUTION = 360 / DEGREES_PER_STEP

# Calculate the number of steps needed for the target angle
# The int() conversion is correct here.
nSteps = int(TARGET_ANGLE / DEGREES_PER_STEP)

# A more reasonable delay for a faster step
# This gives a pulse rate of ~250 Hz (1 / (0.002 * 2))
DELAY = 0.002

print(f"Moving {TARGET_ANGLE} degrees, which is {nSteps} steps.")
print(f"Using a delay of {DELAY} seconds.")

# Loop to generate the step pulses
for i in range(nSteps):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(DELAY)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(DELAY)

print("Movement complete. Cleaning up GPIO.")
# Clean up GPIO pins to release them
GPIO.cleanup()