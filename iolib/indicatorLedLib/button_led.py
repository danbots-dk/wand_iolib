from evdev import InputDevice, categorize, ecodes
from iolib.lp5562.indicatorLib import SysLED
import time

# Replace '/dev/input/event0' with the appropriate event device
dev = InputDevice('/dev/input/event0')

# Define the key you want to watch for (replace KEY_A with the desired keycode)
key_to_watch = ecodes.KEY_1

print("Listening for key press...")
led_0 = SysLED(0)
toggle = True
value_before = None
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.scancode == key_to_watch:
            if event.value == 1:
                if toggle == True:
                    led_0.on(100, 100, 100)
                    toggle = False
                else:
                    led_0.off()
                    toggle = True
                print("Key with keycode {} pressed".format(key_to_watch))
            elif event.value == 2:
                led_0.on(0, 100, 0)
                
                print("Event value is 2, setting LED to green")
            elif event.value == 0 and value_before == 2:
                led_0.off()
                toggle = True
                print("Event value changed from 2 to 0, turning off LED")
            value_before = event.value
