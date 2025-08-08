# Needed ibraries for the function --don't forget to import them later on in the main file--
from picamera2 import Picamera2
import os
from datetime import datetime
from picamera2 import Picamera2
from pathlib import Path
from time import sleep
from sys import exit

# Asking the user for specs

# Asking folder name
folder_name = input("Enter the name of the new folder: ").strip()

# Create the new (or not) folder
base_path = Path.home() / folder_name
os.makedirs(base_path, exist_ok=True)

# Asking the amount of photos
try:
    n_photos = int(input("Enter the amount of photos you'd like, between 1 and 20: "))
except Exception as e:
    n_photos = int(input('Please enter a valid number between 1 and 20: '))
while n_photos < 1 or n_photos > 20:
    n_photos = int(input('Please input a valid number between 1 and 20: '))

# Asking for the exposure time
try:
    exp_time = int(input("Enter the amount of photos you'd like, between 500 and 10000 (in Milliseconds): "))
except Exception as e:
    exp_time = int(input('Please enter a valid number between 500 and 10000: '))
while exp_time < 500 or exp_time > 10000:
    exp_time = int(input('Please input a valid number between 500 and 10000: '))

# Main Running Loop
def take_pictures(basepath, exposure, amount_photos):
    # Starting the photo_taking
    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration({"size": (1920, 1080)}))
    picam2.start()      

    # To control the exposure time of the photo (important in astrophotography)
    picam2.set_controls({
    "ExposureTime": exposure * 1000,  # 1 second
    "AnalogueGain": 1.0       # ISO gain (lower = less noise)
    })
    for i in range(amount_photos):
        filename = base_path / f"photo_{i + 1}_{datetime.now().strftime('%H%M%S')}.jpg"
        picam2.capture_file(str(filename))
        print(f"Captured {filename.name}")
    picam2.stop()
    exit()

take_pictures(base_path, exp_time, n_photos)