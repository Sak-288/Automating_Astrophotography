import RPi.GPIO as GPIO
import time

# PINS FOR MOTOR CONTROLLERS
DIR = 38    # Direction pin
STEP = 40   # Step pin
MS1 = 8     # Microstep pin 1
MS2 = 10    # Microstep pin 2
MS3 = 12    # Microstep pin 3
EN = 36     # Enable pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# 1/16TH STEP MODE: All MS pins HIGH
GPIO.output(MS1, GPIO.HIGH)
GPIO.output(MS2, GPIO.HIGH)
GPIO.output(MS3, GPIO.HIGH)

# Enable the driver (Active LOW)
GPIO.output(EN, GPIO.LOW)

# Motor parameters
MICRO_STEPPING = 16  # 16 microsteps per full step
FULL_STEP_ANGLE = 1.8

DEGREES_PER_STEP = FULL_STEP_ANGLE / MICRO_STEPPING  # 0.1125°
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)           # 3200 steps

# Step function
def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(0.0001)  # 100us pulse is plenty for driver trigger
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

# Movement Function with Acceleration/Deceleration Ramping
def move(degrees, dir):
    nSteps = int(degrees / DEGREES_PER_STEP)

    if dir == 1:
        GPIO.output(DIR, GPIO.HIGH)  # Clockwise
    elif dir == 0:
        GPIO.output(DIR, GPIO.LOW)   # Anti-Clockwise

    time.sleep(0.001)  # Settling delay for DIR line

    # --- SPEED & RAMP SCALING FOR MICROSTEPPING ---
    start_delay = 0.01 / MICRO_STEPPING    # ~0.000625s
    target_delay = 0.002 / MICRO_STEPPING  # ~0.000125s
    
    # Ramp over up to 36 degrees (320 steps in 1/16th mode)
    ramp_steps = min(int(nSteps * 0.20), 20 * MICRO_STEPPING) 

    for i in range(nSteps):
        if i < ramp_steps:
            # Acceleration phase
            current_delay = start_delay - ((start_delay - target_delay) * (i / ramp_steps))
        elif i >= nSteps - ramp_steps:
            # Deceleration phase
            steps_into_decel = i - (nSteps - ramp_steps)
            current_delay = target_delay + ((start_delay - target_delay) * (steps_into_decel / ramp_steps))
        else:
            # Cruising phase
            current_delay = target_delay
            
        step(current_delay)

    print("Movement finished.")

# Main execution loop
try:
    print("Moving 1800 degrees (5 full turns)...")
    move(1800, 1)
    time.sleep(2)
    move(1800, 0)

finally:
    # Disable driver outputs to keep motor cool while idle
    GPIO.output(EN, GPIO.HIGH)
    GPIO.cleanup()
    print("GPIO safely cleaned up.")