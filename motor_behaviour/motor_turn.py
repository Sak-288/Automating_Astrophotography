import RPi.GPIO as GPIO
import time

# PINS FOR MOTOR CONTROLLERS | Obvi, do not touch that, but do replicate it when you have a doubt
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

# It's a game of whackamole. 3 LOWS --> FULL STEP (1.8/360), 3 HIGHS --> 1/16th STEP ? (1.8/16/360)
GPIO.output(MS1, GPIO.HIGH)
GPIO.output(MS2, GPIO.HIGH)
GPIO.output(MS3, GPIO.HIGH)

# Motor parameters
MICRO_STEPPING = 1/16
FULL_STEP_ANGLE = 1.8

# Degrees covered by a single pulse sent to the STEP pin
DEGREES_PER_STEP = FULL_STEP_ANGLE * MICRO_STEPPING  # 0.1125 degrees
# Total pulses needed to turn 360 degrees
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)           # 3200 steps

# Step function
def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

# Movement Function
def move(degrees, dir):
    nSteps = int(degrees / DEGREES_PER_STEP)

    if dir == 1:
        GPIO.output(DIR, GPIO.HIGH)  # Set direction | HIGH == Clockly
    elif dir == 0:
        GPIO.output(DIR, GPIO.LOW)  # Set direction | LOW == ANTI-Clockly

    delay = 0.2 * MICRO_STEPPING  # controlsd speed, so 0.2s for 1.8° and 40s for 360°, a bit slow but good enough ?
    for i in range(nSteps):
        step(delay)

    GPIO.cleanup()
    print("Movement finished.")

