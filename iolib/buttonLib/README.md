## Button API Usage Documentation

This script showcases the usage of the button API using `/dev/input/eventX` devices. It sets up an interrupt that triggers on the selected button, registering press, long press, and release events.

### Function: `read_input_events(button_id, press_callback_function, release_callback_function=None, while_pressed_callback_function=None)`

Sets up an interrupt for a specified button.

#### Parameters:
- `button_id` (str): Identifier for the button. Possible values are `"front1"`, `"front2"`, or `"onoff"`.
- `press_callback_function` (function): Callback function to handle press events.
- `release_callback_function` (function, optional): Callback function to handle release events. Default is `None`.
- `while_pressed_callback_function` (function, optional): Callback function to run while the button is pressed. Default is `None`.

### Example Usage:

```python
import evdev
import threading

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
    read_input_events(device, press_callback_function=handle_press_event, release_callback_function=handle_release_event, while_pressed_callback_function=while_pressed_event)

    # Your main program can continue running or do other tasks here

    # Optionally, wait for user input to keep the program alive
    input("Press Enter to exit...")
