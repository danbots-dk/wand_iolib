# Import necessary libraries
"neopixel led library"
import time
import threading
import neopixel
import board
from sys import path
import os

current_path = os.getcwd()
if current_path.startswith("/usr/local/lib/wand"):
    path.append("/usr/local/lib/wand")
else:
    path.append("/home/peter/iolib")

# Define a class called WandLed to represent a wand LED with typical on/off and blink behavior.
class WandLed:
    """
    Represents a neopixel LED with typical on/off and blink behavior.

    :param num_leds: The number of LEDs in the neopixel strip.
    """

    def __init__(self, num_leds: int):
        """
        Initializes the WandLed class with the specified number of LEDs.

        Args:
            num_leds (int): The number of LEDs in the neopixel strip.
        """
        self.r = [0] * num_leds
        self.g = [0] * num_leds
        self.b = [0] * num_leds
        self.locations = [None] * num_leds
        for i in range(num_leds):
            self.locations[i] = i
        # Initialize NeoPixel object with the specified parameters.
        self.pixels = neopixel.NeoPixel(board.D10, num_leds, brightness=0.5, pixel_order=neopixel.RGBW, auto_write=False)

        # Create a list to hold two thread references for LED control.
        self.led_threads = [None, None]
        self.enable = 1

    def blink(self, location: int, on_time: float, off_time: float, n: int):
        """
        Blink the LED at the specified location.

        Args:
            location (int): The location of the LED (0 for top front, 1 for bottom front).
            on_time (float): Duration in seconds for the LED to be ON.
            off_time (float): Duration in seconds for the LED to be OFF.
            n (int): Number of times to repeat the blink pattern.
        """
        self.set_button_led(location, 0, 0, 0)  # Turn off the LED initially
        thread = threading.Thread(target=self._blink_button_led, args=(location, on_time, off_time, n))
        thread.start()

        # Store the new thread reference
        self.led_threads[location] = thread

    def _blink_button_led(self, location: int, on_time: float, off_time: float, n: int):
        """
        Internal method for controlling LED blinking in a separate thread.

        Args:
            location (int): The location of the LED (0 for top front, 1 for bottom front).
            on_time (float): Duration in seconds for the LED to be ON.
            off_time (float): Duration in seconds for the LED to be OFF.
            n (int): Number of times to repeat the blink pattern.
        """
        for i in range(n):
            self.set_button_led(location, 255, 255, 0)  # Turn the LED ON
            time.sleep(on_time)
            self.set_button_led(location, 0, 0, 0)  # Turn the LED OFF
            time.sleep(off_time)

    def set_button_led(self, location: int, r: int, g: int, b: int):
        """
        Set the color of the LED at the specified location.

        Args:
            location (int): The location of the LED (0 for top front, 1 for bottom front).
            r (int): Red component (0-255).
            g (int): Green component (0-255).
            b (int): Blue component (0-255).
        """
        self.r[location] = r
        self.g[location] = g
        self.b[location] = b

        if self.led_threads[location] is not None:
            # If a thread already exists for this location, you can stop it or take other actions here.
            pass

        # Create a new thread to set the LED color
        thread = threading.Thread(target=self._set_button_led, args=(location, self.r[location], self.g[location], self.b[location]))
        thread.start()

        # Store the new thread reference
        self.led_threads[location] = thread

    def _set_button_led(self, location: int, r: int, g: int, b: int):
        """
        Internal method for setting the LED color in a separate thread.

        Args:
            location (int): The location of the LED (0 for top front, 1 for bottom front).
            r (int): Red component (0-255).
            g (int): Green component (0-255).
            b (int): Blue component (0-255).
        """
        while(1):
            for i, led in enumerate(self.locations):
                # self.pixels[led] = (self.r[i], self.g[i], self.b[i], 0)
                self.pixels[led] = (self.r[i], self.g[i], 0, 0)
            time.sleep(0.1)
            self.pixels.show()
            if(self.enable != 1):
                for i in range(2):
                    self.pixels[location] = (0, 0, 0, 0)
                    time.sleep(0.1)
                break

    def close(self):
        """Close all LED threads"""
        for led in self.locations:
            self.set_button_led(led, 0, 0, 0)
        self.enable = 0

    def blink_fast(self, location: int):
        """Blink the LED quickly."""
        self.blink(location=location, on_time=0.2, off_time=0.2, n=1)

    def blink_3(self, location: int):
        """Blink the LED three times."""
        self.blink(location=location, on_time=0.2, off_time=0.2, n=3)

    def blink_n(self, location: int, n: int):
        """Blink the LED 'n' times.

        Args:
            location (int): The location of the LED.
            n (int): Number of times to blink the LED.
        """
        self.blink(location=location, on_time=0.2, off_time=0.2, n=n)

if __name__ == "__main__":
    # Create an instance of the WandLed class for LED number 1.
    led = WandLed(2)
    # led.set_button_led(1, 255, 0, 0)
    # Perform various LED operations with delays in between.
    # led.close()
    time.sleep(1)
    led.blink_n(1, 3)
    time.sleep(0.2)
    led.blink_n(0, 3)

    time.sleep(2)
    led.close()
    # led.blink_3(1)

    # time.sleep(2)
    led.close()
    #
    time.sleep(1)

    time.sleep(1)
    led.set_button_led(0, 255, 255, 0)
    led.set_button_led(1, 0, 0, 0)

    time.sleep(1)
    led.close()
    # led.close(1)
    # Continuously cycle through an RGB color gradient with a delay.
