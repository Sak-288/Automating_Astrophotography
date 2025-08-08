# Importing the related libraries
from MPU6050.mpu6050 import mpu6050
import time

mpu = mpu6050(0x68, 1)

while True:
    print("Temp : "+str(mpu.get_temp()))
    print()

    # Basically just reading the data of the 3 axis : pitch, yaw, roll
    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x'])) # yaw
    print("Gyro Y : "+str(gyro_data['y'])) # pitch
    print("Gyro Z : "+str(gyro_data['z'])) # roll
    print()
    print("-------------------------------")