import RPi.GPIO as GPIO
import time
import picamera
import sys
import os

# Script Path
scriptPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scriptPath)


# Set up the GPIO pin for the button
button_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set up 

# Create a function to capture an image when the button is pressed
def capture_image():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        #camera.start_preview(fullscreen=False,window=(100,200,300,400))
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        image_path = 'new_image.jpg'
        camera.capture(image_path)
        # Print the image
        os.system(f"sudo python3  phomemo-filter.py {image_path} > /dev/rfcomm0")
        #printer.print_bitmap(image_path)

# Set up event detection for the button press
try:
    while True:
        if GPIO.input(24) == GPIO.HIGH:
            print("button pressed")
            capture_image()
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
