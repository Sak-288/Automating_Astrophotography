import os
import subprocess
from pathlib import Path

folder_name = input("Enter the name of the new folder: ").strip()

# Create the new (or not) folder && create the path for the image
base_path = Path.home() / folder_name
os.makedirs(base_path, exist_ok=True)
output_path = base_path / "photo.jpg"

# Making the command to use the pi bash
cmd = [
    "libcamera-still",
    "-o", str(output_path),
    "--width", "1920",
    "--height", "1080"
]


# COMMAND IS RUNNING
subprocess.run(cmd)
