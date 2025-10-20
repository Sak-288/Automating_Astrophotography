import RPi.GPIO as GPIO
import time

# --- Broches GPIO (BCM numbering)
DIR = 38   # Direction pin
STEP = 40  # Step pin
MS1 = 10
MS2 = 12
MS3 = 14

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

# --- Config microstepping : FULL STEP (max couple)
GPIO.output(MS1, GPIO.LOW)
GPIO.output(MS2, GPIO.LOW)
GPIO.output(MS3, GPIO.LOW)

# --- Paramètres moteur
DEGREES_PER_STEP = 1.8       # Full step
STEPS_PER_REV = int(360 / DEGREES_PER_STEP)

# --- Mouvement
TARGET_ANGLE = 2160
nSteps = int(TARGET_ANGLE / DEGREES_PER_STEP)

print(f"Moving {TARGET_ANGLE}°, soit {nSteps} pas entiers.")

# --- Fonction pour faire un pas
def step(delay):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

try:
    GPIO.output(DIR, GPIO.HIGH)  # sens 1

    delay = 0.01   # départ très lent (~50 Hz)
    min_delay = 0.002  # vitesse max (~250 Hz)
    accel_rate = 0.00002  # plus petit = accélération plus lente

    for i in range(nSteps):
        step(delay)

        # accélère progressivement jusqu'au tiers du parcours
        if delay > min_delay and i < nSteps/3:
            delay -= accel_rate

        # ralentit sur le dernier tiers
        if i > (2*nSteps)/3:
            delay += accel_rate

finally:
    GPIO.cleanup()
    print("Fin du mouvement.")
