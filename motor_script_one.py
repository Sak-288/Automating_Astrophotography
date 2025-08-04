import RPi.GPIO as GPIO
import time

print('hello world I am working !')

DIR = 20
STEP = 21
MS1 = 23
MS2 = 24
MS3 = 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)
GPIO.output(STEP, GPIO.HIGH) 
GPIO.output(MS1, GPIO.HIGH)
GPIO.output(MS2, GPIO.HIGH) 
GPIO.output(MS3, GPIO.HIGH)

target = 180

# Since MS1-2 && 3 are set to HIGH, we are dealing in 1/16th steps

nMicro = 16
nSteps = round(target / 1.8 * nMicro)
DELAY = 1/nSteps * 5

for i in range(nSteps):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(DELAY)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(DELAY)
