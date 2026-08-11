import RPi.GPIO as GPIO
import time

# PINS FOR MOTOR CONTROLLERS
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

# FULL STEP MODE: Maximum holding and running torque
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)
GPIO.output(MS3, GPIO.LOW)

# Motor parameters
MICRO_STEPPING = 1/1
FULL_STEP_ANGLE = 1.8

DEGREES_PER_STEP = FULL_STEP_ANGLE * MICRO_STEPPING  
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)           

# Step function (Optimized for driver logic)
def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    # A short, fixed high-pulse guarantees the driver registers the step perfectly
    time.sleep(0.0005) 
    GPIO.output(STEP, GPIO.LOW)
    # The variable delay dictates the speed and torque curve
    time.sleep(delay)

# Movement Function with Acceleration/Deceleration Ramping
def move(degrees, dir):
    nSteps = int(degrees / DEGREES_PER_STEP)

    if dir == 1:
        GPIO.output(DIR, GPIO.HIGH)  # Clockwise
    elif dir == 0:
        GPIO.output(DIR, GPIO.LOW)   # Anti-Clockwise

    # --- TORQUE OPTIMIZATION: TRAPEZOIDAL RAMPING ---
    start_delay = 0.02  # SLOW starting speed = MASSIVE starting torque
    target_delay = 0.005 # Cruising speed
    
    # Ramp over 20% of the movement, or up to 40 steps, whichever is smaller
    ramp_steps = min(int(nSteps * 0.20), 40) 

    for i in range(nSteps):
        if i < ramp_steps:
            # Acceleration phase: slowly decrease the delay
            current_delay = start_delay - ((start_delay - target_delay) * (i / ramp_steps))
        elif i >= nSteps - ramp_steps:
            # Deceleration phase: slowly increase the delay to prevent inertial skip at the end
            steps_into_decel = i - (nSteps - ramp_steps)
            current_delay = target_delay + ((start_delay - target_delay) * (steps_into_decel / ramp_steps))
        else:
            # Cruising phase
            current_delay = target_delay
            
        step(current_delay)

    print("Movement finished.")

# Main execution loop
try:
    move(90 * 38, 1)
    time.sleep(2)
    move(90 * 38, 0)

finally:
    GPIO.cleanup()
    print("GPIO safely cleaned up.")