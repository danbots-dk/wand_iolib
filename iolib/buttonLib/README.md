## Button API Usage Documentation

Library to interface with front touch buttons.

### Function: `read_input_events(button_id, press_callback_function, release_callback_function=None, while_pressed_callback_function=None)`

Sets up an interrupt for a specified button.

#### Parameters:
- `button_id` (str): Identifier for the button. Possible values are `"front1"`, `"front2"`, or `"onoff"`.
- `press_callback_function` (function, required): Callback function to handle press events.
- `release_callback_function` (function, optional): Callback function to handle release events. Default is `None`.
- `while_pressed_callback_function` (function, optional): Callback function to run while the button is pressed. Default is `None`.

### Example Usage:

```python
import evdev
import threading

'''
This script show cases the button API using /dev/input/eventX.
The script sets up an interrupt that is triggered by the selected button, and can register a press, long press and release.
'''

def read_input_events(button_id, press_callback_function, release_callback_function=None, while_pressed_callback_function=None):
    try:
        if button_id == "front1":
            device_path = "/dev/input/event2"
        elif button_id == "front2":
            device_path = "/dev/input/event1"
        elif button_id == "onoff":
            device_path = "/dev/input/event0"
        
        # Open the input device
        device = evdev.InputDevice(device_path)
        print(f"Connected to {device.name}")

        # Variable to track the pressed state
        is_pressed = False

        # Read and print input events in a separate thread
        def input_thread():
            nonlocal is_pressed

            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                    if event.value == 1 and press_callback_function is not None:
                        # Call the press callback function
                        press_callback_function(evdev.categorize(event))
                        is_pressed = True
                        # If while_pressed_callback_function is provided, start the while-pressed loop
                        if while_pressed_callback_function is not None:
                            while_pressed_thread = threading.Thread(target=while_pressed_thread_function)
                            while_pressed_thread.daemon = True
                            while_pressed_thread.start()

                    elif event.value == 0 and release_callback_function is not None:
                        # Call the release callback function
                        release_callback_function(evdev.categorize(event))
                        is_pressed = False

        def while_pressed_thread_function():
            nonlocal is_pressed
            while is_pressed:
                # Call the while-pressed callback function
                while_pressed_callback_function()

        # Start the input thread
        input_thread = threading.Thread(target=input_thread)
        input_thread.daemon = True  # The thread will exit when the main program exits
        input_thread.start()

        # Your main program can continue running or do other tasks here

        # Optionally, wait for the input thread to finish (e.g., using input_thread.join())

    except FileNotFoundError:
        print(f"Error: Device not found at {device_path}")
    except PermissionError:
        print(f"Error: Insufficient permissions to access {device_path}")

def handle_press_event(event):
    # Callback function to handle press events
    print(f"Press: {event}")

def handle_release_event(event):
    # Callback function to handle release events
    print(f"Release: {event}")

def while_pressed_event():
    # Callback function to run while the button is pressed
    print("Button is still pressed!")

if __name__ == "__main__":
    # Specify the path to your input device, e.g., /dev/input/event0
    device = "front1"

    # Pass the press, release, and while-pressed callback functions as arguments
    #read_input_events(device_path, press_callback_function=handle_press_event, release_callback_function=handle_release_event, while_pressed_callback_function=while_pressed_event)
    read_input_events(device, press_callback_function=handle_press_event)

    # Your main program can continue running or do other tasks here

    # Optionally, wait for user input to keep the program alive
    input("Press Enter to exit...")

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
[How to compile LKM](https://github.com/RPi-Distro/rpi-source
[Bindings for writing dtoverlays](https://github.com/raspberrypi/linux/tree/77fc1fbcb5c013329af9583307dd1ff3cd4752aa/Documentation/devicetree/bindings)
[Docs for various drivers](https://github.com/raspberrypi/linux/tree/77fc1fbcb5c013329af9583307dd1ff3cd4752aa/Documentation)


