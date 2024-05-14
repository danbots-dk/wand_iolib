from evdev import InputDevice, categorize, ecodes
import threading
import time

class Button:
    """
    Represents a physical button connected to the system as an input device..
    
    This class allows for the detection of button press, long press, and release events through callbacks.
    
    Attributes:
        device (InputDevice): The evdev InputDevice instance representing the physical button.
        key_to_watch (int): The key code to watch for events.s
    """
    
    def __init__(self, button_id):
        """
        Initializes the Button with a device path based on the provided button ID.
        
        Args:
            button_id (str): A string identifier for the button (e.g., "onoff", "front1", "front2").
            
        Raises:
            FileNotFoundError: If the specified input device does not exist.
            PermissionError: If the program does not have permission to access the input device.
        """
        device_path = ''
        try:
            if button_id == "onoff":
                device_path = "/dev/input/event0"
            elif button_id == "front2":
                device_path = "/dev/input/event2"
                self.key_to_watch = ecodes.KEY_DOWN
            elif button_id == "front1":
                device_path = "/dev/input/event1"
                self.key_to_watch = ecodes.KEY_UP
        except FileNotFoundError:
            print(f"Error: Device not found at {device_path}")
        except PermissionError:
            print(f"Error: Insufficient permissions to access {device_path}")

        self.device = InputDevice(device_path)

    def read_input_events(self, press_callback_function, release_callback_function=None, while_pressed_callback_function=None):
        """
        Starts listening for input events from the button, triggering callbacks as appropriate.
        
        This method sets up and starts a separate thread to listen for press, release, and while-pressed events.
        
        Args:
            press_callback_function (callable): A function to call when the button is pressed.
            release_callback_function (callable, optional): A function to call when the button is released.
            while_pressed_callback_function (callable, optional): A function to call repeatedly while the button is pressed.
        """
        if while_pressed_callback_function is not None and release_callback_function is None:
            raise Exception("Release callback function must be provided when while pressed callback function is defined.")
            
        def input_thread():
            nonlocal is_pressed
            for event in self.device.read_loop():
                if event.type == ecodes.EV_KEY:
                    key = categorize(event)
                    if key.scancode == self.key_to_watch:
                        if event.value == 1:
                            press_callback_function(categorize(event))
                            is_pressed = True
                        elif event.value == 2 and while_pressed_callback_function is not None:
                            while_pressed_thread = threading.Thread(target=while_pressed_thread_function)
                            while_pressed_thread.daemon = True
                            while_pressed_thread.start()
                        elif event.value == 0 and release_callback_function is not None:
                            release_callback_function(categorize(event))
                            is_pressed = False

        def while_pressed_thread_function():
            nonlocal is_pressed
            while is_pressed:
                while_pressed_callback_function()

        is_pressed = False
        input_thread = threading.Thread(target=input_thread)
        input_thread.daemon = True
        input_thread.start()

def handle_press_event(event):
    """
    Handles button press events.
    
    Args:
        event: The event object representing the button press.
    """
    print(f"Press: {event}")

def handle_release_event(event):
    """
    Handles button release events.
    
    Args:
        event: The event object representing the button release.
    """
    print(f"Release: {event}")

def while_pressed_event():
    """
    A callback function executed continuously while the button is pressed.
    """
    print("Button is still pressed!")
    time.sleep(0.1)

if __name__ == "__main__":
    button = Button("front2")
    button.read_input_events(press_callback_function=handle_press_event, release_callback_function=handle_release_event)

    input("Press Enter to exit...\n")
