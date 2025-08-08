from mpu6050 import mpu6050
from time import sleep

# CONSTANTS :
sensor = mpu6050(0x68, 1) # Object
reference_delay = 5 # Delay in seconds to let gyro stabilize

# Mainline
sleep(reference_delay)
reference_coords = mpu.get_gyro_data()

 