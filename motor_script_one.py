import RPi.GPIO as GPIO
import time

DIR = 11
STEP = 13
MS1 = 15
MS2 = 16
MS3 = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

GPIO.output(DIR, HIGH)
GPIO.output(STEP, GPIO.LOW) 
GPIO.output(MS1, GPIO.HIGH) 
GPIO.output(MS2, GPIO.HIGH) 
GPIO.output(MS3, GPIO.HIGH) 

target = 90

# Since MS1-2 && 3 are set to HIGH, we are dealing in 1/16th steps

nMicro = 16
nSteps = round(target / 1.8 * nMicro)
print(nSteps)
DELAY = 0.1

for i in range(nSteps):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(DELAY)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(DELAY)