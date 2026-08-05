import RPi.GPIO as GPIO
import time

# PINS FOR MOTOR CONTROLLERS | Obvi, do not touch that, but do replicate it when you have a doubt
DIR = 38    # Direction pin
STEP = 40   # Step pin
MS1 = 8     # Microstep pin 1
MS2 = 10    # Microstep pin 2
MS3 = 12    # Microstep pin 3
ENABLE = 36 # Shitter pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENABLE, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

GPIO.output(ENABLE, GPIO.LOW)

# 3 LOWS --> FULL STEP (1.8/360)
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)
GPIO.output(MS3, GPIO.LOW)

# Motor parameters
MICRO_STEPPING = 1/1
FULL_STEP_ANGLE = 1.8

# Degrees covered by a single pulse sent to the STEP pin
DEGREES_PER_STEP = FULL_STEP_ANGLE * MICRO_STEPPING  # 1.8 degrees at Full Step
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)           # 200 steps

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
        GPIO.output(DIR, GPIO.HIGH)  # Set direction | HIGH == Clockwise
    elif dir == 0:
        GPIO.output(DIR, GPIO.LOW)   # Set direction | LOW == Anti-Clockwise

    delay = 0.0005 * MICRO_STEPPING     # Controls speed
    for i in range(nSteps):
        step(delay)

    print("Movement finished.")

# Main execution loop
try:
    move(18000, 1)
    time.sleep(2)
    move(18000, 0)

finally:
    # Cleanup only when ALL movements are finished
    GPIO.cleanup()
    print("GPIO safely cleaned up.")