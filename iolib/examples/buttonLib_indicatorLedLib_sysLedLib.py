import keyboard
import RPi.GPIO as GPIO
from sys import path
path.append("/usr/local/lib/wand/iolib")
from indicatorLedLib import SysLED
from buttonLib import Button
from scanLedLib import ScanLed
import time

button1 = Button("front1")
indicatorLED = SysLED()

scanLED = ScanLed()

sysLed_value = 0
def handle_press_event(event):
    """
    Handles button press events.
    
    Args:
        event: The event object representing the button press.
    """
    
    global sysLed_value
    print(f"Press: {event}")
    if sysLed_value == 0:
        sysLed_value = 255
    else:
        sysLed_value = 0
    
    indicatorLED.set_brightness(sysLed_value)

def handle_release_event(event):
    """
    Handles button release events.
    
    Args:
        event: The event object representing the button release.
    """
    scanLED.set_dias(0)
    print(f"Press: {event}")

def while_pressed_event():
    """
    Handles button press events.
    
    Args:
        event: The event object representing the button press.
    """
    scanLED.set_dias(1)
    print(f"pressed")
    time.sleep(0.1)

button1.read_input_events(press_callback_function=handle_press_event, release_callback_function=handle_release_event, while_pressed_callback_function=while_pressed_event)
input("Press Enter to exit...\n")
GPIO.cleanup()