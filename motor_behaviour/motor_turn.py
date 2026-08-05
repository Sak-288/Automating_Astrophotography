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

def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(0.001)  # Slightly longer HIGH pulse ensures total driver saturation
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

def move(degrees, dir):
    nSteps = int(degrees / DEGREES_PER_STEP)

    if dir == 1:
        GPIO.output(DIR, GPIO.HIGH)  
    elif dir == 0:
        GPIO.output(DIR, GPIO.LOW)   
        
    # TORQUE TWEAK 1: Pre-charge the coils. 
    # Giving the driver 50ms after changing direction allows the magnetic 
    # field to reach 100% holding strength before we attempt to move the load.
    time.sleep(0.05) 

    # --- EXTREME TORQUE RAMPING ---
    start_delay = 0.04   # 40ms delay (EXTREMELY slow start to break static friction)
    target_delay = 0.01  # 10ms delay (Slower top speed = massively higher running torque)
    
    # TORQUE TWEAK 2: Stretch the ramp. 
    # Use up to 40% of the total movement just for accelerating.
    ramp_steps = min(int(nSteps * 0.40), 100) 

    for i in range(nSteps):
        if i < ramp_steps:
            current_delay = start_delay - ((start_delay - target_delay) * (i / ramp_steps))
        elif i >= nSteps - ramp_steps:
            steps_into_decel = i - (nSteps - ramp_steps)
            current_delay = target_delay + ((start_delay - target_delay) * (steps_into_decel / ramp_steps))
        else:
            current_delay = target_delay
            
        step(current_delay)

    print("Movement finished.")

try:
    move(180, 1)
    time.sleep(2)
    move(180, 0)

finally:
    GPIO.cleanup()
    print("GPIO safely cleaned up.")