import RPi.GPIO as GPIO
import time

# --- Broches GPIO (BCM numbering)
DIR = 20   # Direction pin
STEP = 21  # Step pin
MS1 = 14
MS2 = 15
MS3 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# --- Config microstepping : 1/4 pas
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.HIGH)
GPIO.output(MS3, GPIO.LOW)

# --- Paramètres moteur
DEGREES_PER_STEP = 1.8 / 4  # 1/4 pas
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)

# --- Mouvement
TARGET_ANGLE = 90
nSteps = int(TARGET_ANGLE / DEGREES_PER_STEP)

print(f"Moving {TARGET_ANGLE}°, soit {nSteps} micro-pas.")

# --- Rampes d'accélération
def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

try:
    GPIO.output(DIR, GPIO.HIGH)  # sens 1

    delay = 0.01   # départ lent (~50 Hz)
    for i in range(nSteps):
        step(delay)
        # accélère progressivement
        if delay > 0.002 and i < nSteps/3:
            delay -= 0.00005
        # ralentit à la fin
        if i > (2*nSteps)/3:
            delay += 0.00005

finally:
    GPIO.cleanup()
    print("Fin du mouvement.")
