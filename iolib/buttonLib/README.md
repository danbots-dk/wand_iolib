The button library is implemented using kernel drivers. The setting are configured using the .dts overlay file found in iolib/buttonLib/cap1293/cap12xx_v2/cap12xx_pca9542.dts. The following settings can be configured for now:

 - Pin interrupt (configured via /boot/config.txt)
 - sensor-gain (set to 2)
 - keycodes (semi random values for now..)
 - Signal guard
 - 

Once loaded (verified using dmesg), the button input is available via /dev/input/eventX. Consult the button_api_example.py for how to interface with this.

## Button API Usage Documentation

This script showcases the usage of the button API using `/dev/input/eventX` devices. It sets up an interrupt that triggers on the selected button, registering press, long press, and release events.

### Class: `Button`

Represents a button object that can read input events from a specified input device.

#### Constructor: `__init__(button_id: str)`

Initializes a Button object with a specified button ID.

- `button_id` (str): Identifier for the button. Possible values are `"front1"`, `"front2"`, or `"onoff"`.

#### Method: `read_input_events(press_callback_function=None, release_callback_function=None, while_pressed_callback_function=None)`

Sets up an interrupt for the button, registering press, long press, and release events.

- `press_callback_function` (function, optional): Callback function to handle press events.
- `release_callback_function` (function, optional): Callback function to handle release events.
- `while_pressed_callback_function` (function, optional): Callback function to run while the button is pressed.

### Example Usage:

```python
from buttonLib import Button
import evdev
import threading
import time

def handle_press_event(event):
    # Callback function to handle press events
    print(f"Press: {event}")

def handle_release_event(event):
    # Callback function to handle release events
    print(f"Release: {event}")

def while_pressed_event():
    # Callback function to run while the button is pressed
    print("Button is still pressed!")
    time.sleep(0.1)

if __name__ == "__main__":
    # Specify the path to your input device, e.g., /dev/input/event0
    device = "front2"
    button = Button(device)
    # Pass the press, release, and while-pressed callback functions as arguments
    button.read_input_events(press_callback_function=handle_press_event, release_callback_function=handle_release_event)

    # Your main program can continue running or do other tasks here

    # Optionally, wait for user input to keep the program alive
    input("Press Enter to exit...\n")
```

# On the subject of compiling..
The module is compiled as a Loadable-Kernel-Module (LKM) meaning the whole kernel does not need to be compile upon new changes. Running the make_kernel_module.sh script compile both the dtoverlay and copies it to the correct path and the cap1293 driver using the provided Makefile.
In order to be able to compile for the current kernel version the following must be installed (note that when all devices run the same OS, it should not be necessary as once the driver is compiled it should be compatible everywhere).

Dependencies
```text
sudo apt install git bc bison flex libssl-dev
```

Install
```text
sudo wget https://raw.githubusercontent.com/RPi-Distro/rpi-source/master/rpi-source -O /usr/local/bin/rpi-source && sudo chmod +x /usr/local/bin/rpi-source && /usr/local/bin/rpi-source -q --tag-update

```
Run
```text
rpi-source
```


## Resources
[How to compile LKM](https://github.com/RPi-Distro/rpi-source)  
[Bindings for writing dtoverlays](https://github.com/raspberrypi/linux/tree/77fc1fbcb5c013329af9583307dd1ff3cd4752aa/Documentation/devicetree/bindings)  
[Docs for various drivers](https://github.com/raspberrypi/linux/tree/77fc1fbcb5c013329af9583307dd1ff3cd4752aa/Documentation)  


