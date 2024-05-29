import os
import time
import threading

class SysLED:
    """
    A class to control the LED brightness and blinking functionality of the system LED.

    Attributes:
        red (str): The path to the red LED brightness control file.
        green (str): The path to the green LED brightness control file.
        blue (str): The path to the blue LED brightness control file.
        color (str): The current color of the LED.
        blink_thread (threading.Thread): The thread responsible for blinking the LED.
        stop_event (threading.Event): An event to signal stopping the blinking thread.

    Methods:
        __init__(self, channel=0):
            Initializes the SysLED object with the specified LED channel.
        set_brightness(self, r=None, g=None, b=None):
            Sets the brightness of the LED for each color component (red, green, blue).
        __blink_worker(self, r, g, b, on_time, off_time, n):
            Worker function for the blinking functionality of the LED.
        blink(self, r, g, b, on_time=1, off_time=1, n=float("inf")):
            Starts blinking the LED with the specified color and timing parameters.
        stop_blink(self):
            Stops the blinking of the LED.
        on(self, r=0, g=0, b=0):
            Turns on the LED with the specified color.
        off(self):
            Turns off the LED.
    """

    def __init__(self, channel=0):
        """
        Initializes the SysLED object with the specified LED channel.

        Args:
            channel (int): The channel number of the LED (default is 0).
        """
        self.red = f"/sys/class/leds/red_{channel}/"
        self.green = f"/sys/class/leds/green_{channel}/"
        self.blue = f"/sys/class/leds/blue_{channel}/"

        self.color = "red"
        self.blink_thread = None
        self.stop_event = threading.Event()

    def set_brightness(self, r=None, g=None, b=None):
        """
        Sets the brightness of the LED for each color component (red, green, blue).

        Args:
            r (int): Brightness value for the red color (0 to 255).
            g (int): Brightness value for the green color (0 to 255).
            b (int): Brightness value for the blue color (0 to 255).
        """
        if r is not None:
            r = max(0, min(r, 255))  # Ensure brightness is between 0 and 255
            with open(os.path.join(self.red, "brightness"), "w") as f:
                f.write(str(r))
        if g is not None:
            g = max(0, min(g, 255))  # Ensure brightness is between 0 and 255
            with open(os.path.join(self.green, "brightness"), "w") as f:
                f.write(str(g))
        if b is not None:
            b = max(0, min(b, 255))  # Ensure brightness is between 0 and 255
            with open(os.path.join(self.blue, "brightness"), "w") as f:
                f.write(str(b))

    def __blink_worker(self, r, g, b, on_time, off_time, n):
        """
        Worker function for the blinking functionality of the LED.

        Args:
            r (int): Brightness value for the red color (0 to 255).
            g (int): Brightness value for the green color (0 to 255).
            b (int): Brightness value for the blue color (0 to 255).
            on_time (float): Time duration in seconds for the LED to be ON during each blink cycle.
            off_time (float): Time duration in seconds for the LED to be OFF during each blink cycle.
            n (float): Number of blink cycles (default is infinite for indefinite blinking).
        """
        while n > 0 and not self.stop_event.is_set():
            self.set_brightness(r, g, b)
            time.sleep(on_time)
            if not self.stop_event.is_set():
                self.set_brightness(0, 0, 0)
                time.sleep(off_time)
            n -= 1

    def blink(self, r, g, b, on_time=1, off_time=1, n=float("inf")):
        """
        Starts blinking the LED with the specified color and timing parameters.

        Args:
            r (int): Brightness value for the red color (0 to 255).
            g (int): Brightness value for the green color (0 to 255).
            b (int): Brightness value for the blue color (0 to 255).
            on_time (float): Time duration in seconds for the LED to be ON during each blink cycle (default is 1).
            off_time (float): Time duration in seconds for the LED to be OFF during each blink cycle (default is 1).
            n (float): Number of blink cycles (default is infinite for indefinite blinking).
        """
        self.stop_event.clear()
        self.blink_thread = threading.Thread(target=self.__blink_worker, args=(r, g, b, on_time, off_time, n))
        self.blink_thread.start()

    def stop_blink(self):
        """
        Stops the blinking of the LED.
        """
        self.stop_event.set()
        if self.blink_thread:
            self.blink_thread.join()

    def on(self, r=0, g=0, b=0):
        """
        Turns on the LED with the specified color.

        Args:
            r (int): Brightness value for the red color (default is 0).
            g (int): Brightness value for the green color (default is 0).
            b (int): Brightness value for the blue color (default is 0).
        """
        self.set_brightness(r, g, b)

    def off(self):
        """
        Turns off the LED.
        """
        self.set_brightness(0, 0, 0)

    def get_state(self):
        """ 
        Gets state of LED.
        
        Returns:
            int: Brightness value of the red LED.
            int: Brightness value of the green LED.
            int: Brightness value of the blue LED.
        """
        with open(os.path.join(self.red, "brightness"), "r") as f_red:
            red_brightness = int(f_red.read())
        with open(os.path.join(self.green, "brightness"), "r") as f_green:
            green_brightness = int(f_green.read())
        with open(os.path.join(self.blue, "brightness"), "r") as f_blue:
            blue_brightness = int(f_blue.read())
        return red_brightness, green_brightness, blue_brightness


# Example usage:
if __name__ == "__main__":
    led = SysLED(channel=0)
    led.blink(r=255, g=200, b=0, on_time=0.5, off_time=0.5, n=5)
    print("keep blinking in separate thread")
    time.sleep(8)
    led.stop_blink()
