import RPi.GPIO as GPIO
import time
import subprocess

class BootloaderConf:
    """
    A class to control GPIO pins on a Raspberry Pi for bootloader configuration.

    Attributes:
        None

    Methods:
        __init__(): Initializes the GPIO pins.
        set_gpio_high(pin): Sets the specified GPIO pin to high.
        set_gpio_low(pin): Sets the specified GPIO pin to low.
        assert_bootloader(): Asserts bootloader mode by manipulating GPIO pins.
        deassert_bootloader(): Deasserts bootloader mode by manipulating GPIO pins.
        restart_computer(): Restarts the Raspberry Pi.
    """

    def __init__(self):
        """
        Initializes the GPIO pins.

        Args:
            None

        Returns:
            None
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
    
    def set_gpio_high(self, pin):
        """
        Sets the specified GPIO pin to high.

        Args:
            pin (int): The GPIO pin number to set high.

        Returns:
            None
        """
        GPIO.output(pin, GPIO.HIGH)
    
    def set_gpio_low(self, pin):
        """
        Sets the specified GPIO pin to low.

        Args:
            pin (int): The GPIO pin number to set low.

        Returns:
            None
        """
        GPIO.output(pin, GPIO.LOW)
    
    def assert_bootloader(self):
        """
        Asserts bootloader mode by manipulating GPIO pins.

        Args:
            None

        Returns:
            None
        """
        try:
            self.set_gpio_high(4)
            time.sleep(0.1)
            self.set_gpio_high(17)
            time.sleep(0.1)
            self.set_gpio_low(17)
            self.set_gpio_low(4)
            
        finally:
            GPIO.cleanup()

    def deassert_bootloader(self):
        """
        Deasserts bootloader mode by manipulating GPIO pins.

        Args:
            None

        Returns:
            None
        """
        try:
            self.set_gpio_high(4)
            self.set_gpio_high(17)
            time.sleep(0.1)
            self.set_gpio_low(4)
            time.sleep(0.1)
            self.set_gpio_high(17)
            
        finally:
            GPIO.cleanup()

    def restart_computer(self):
        """
        Restarts the Raspberry Pi.

        Args:
            None

        Returns:
            None
        """
        subprocess.call(["shutdown", "-r", "-t", "0"])

# Example usage
if __name__ == "__main__":
    gpio_controller = BootloaderConf()
    gpio_controller.assert_bootloader()
