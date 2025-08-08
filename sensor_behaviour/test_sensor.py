from mpu6050 import mpu6050
from time import sleep, time

# Create sensor object
sensor = mpu6050(0x68, 1)

# Let the sensor stabilize
sleep(2)

# Get Reference Values --> (0; 0)
r_yaw = sensor.get_gyro_data()['z']
r_pitch = sensor.get_gyro_data()['x']

def getTelOrientation():
    c_yaw = sensor.get_gyro_data()['z'] - r_yaw
    c_pitch = sensor.get_gyro_data()['x'] - r_pitch
    telCoords = [c_yaw, c_pitch]
    return telCoords

while True:
    print(getTelOrientation())