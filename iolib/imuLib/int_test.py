import RPi.GPIO as GPIO
import time

# GPIO pin number
interrupt_pin = 4

# Setup GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin as input and enable the pull-up resistor
GPIO.setup(interrupt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define a callback function to be executed when the interrupt occurs
def interrupt_callback(channel):
    print("Interrupt detected on GPIO %d" % channel)

# Add event detection to the GPIO pin
GPIO.add_event_detect(interrupt_pin, GPIO.FALLING, callback=interrupt_callback, bouncetime=20)

try:
    print("Waiting for interrupts...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program")
    GPIO.cleanup()
