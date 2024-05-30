import keyboard
import RPi.GPIO as GPIO
from sys import path
path.append("/usr/local/lib/wand/iolib")
from indicatorLedLib import SysLED
from buttonLib import Button
from scanLedLib import ScanLed
import time

button1 = Button("front1")
button2 = Button("front2")
indicatorLED = SysLED()

scanLED = ScanLed()
indicator_cycle = 0

def handle_press_event(event):
    """
    Handles button press events.
    
    Args:
        event: The event object representing the button press.
    """
    
    print(f"Press: {event}")
    global indicator_cycle
    r, g, b = indicatorLED.get_state()
    if indicator_cycle == 0:
        r = 50
        g = 0
        b = 0
        indicator_cycle = indicator_cycle + 1
    elif indicator_cycle == 1:
        r = 0
        g = 50
        b = 0
        indicator_cycle = indicator_cycle + 1
    elif indicator_cycle == 2:
        r = 0
        g = 0
        b = 50
        indicator_cycle = 0
    
    indicatorLED.set_brightness(r, g, b)

def handle_release_event(event):
    """
    Handles button release events.
    
    Args:
        event: The event object representing the button release.
    """
    scanLED.set_dias(0)
    scanLED.set_flash(0)
    print(f"Press: {event}")

def while_pressed_event():
    """
    Handles button press events.
    
    Args:
        event: The event object representing the button press.
    """

    dias_val = scanLED.get_dias()
    if dias_val != 1:
        scanLED.set_dias(1)
        scanLED.set_flash(0)


    print(f"pressed")
    time.sleep(0.15)

button1.read_input_events(press_callback_function=handle_press_event, release_callback_function=handle_release_event, while_pressed_callback_function=while_pressed_event)
button2.read_input_events(press_callback_function=handle_press_event, release_callback_function=handle_release_event, while_pressed_callback_function=while_pressed_event)

input("Press Enter to exit...\n")
GPIO.cleanup()