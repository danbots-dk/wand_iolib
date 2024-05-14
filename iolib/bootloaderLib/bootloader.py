import RPi.GPIO as GPIO
import time
import subprocess

class BootloaderConf:
    def __init__(self):
        # Set GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)
        # Set GPIO 4 and 17 as output pins
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
    
    def set_gpio_high(self, pin):
        GPIO.output(pin, GPIO.HIGH)
    
    def set_gpio_low(self, pin):
        GPIO.output(pin, GPIO.LOW)
    
    def assert_bootloader(self):
        try:
            # Pull GPIO 4 high
            self.set_gpio_high(4)
            time.sleep(0.1)
            # Pull GPIO 17 high
            self.set_gpio_high(17)
            time.sleep(0.1)

            # Pull GPIO 4 low
            self.set_gpio_low(17)
            # Pull GPIO 17 low
            self.set_gpio_low(4)
            
        finally:
            # Clean up GPIO
            GPIO.cleanup()

    def deassert_bootloader(self):
        try:
            # Pull GPIO 4 high
            self.set_gpio_high(4)
            
            # Pull GPIO 17 high
            self.set_gpio_high(17)
            time.sleep(0.1)
            
            # Pull GPIO 4 low
            self.set_gpio_low(4)
            time.sleep(0.1)

            # Pull GPIO 17 high
            self.set_gpio_high(17)
            
        finally:
            # Clean up GPIO
            GPIO.cleanup()

    def restart_computer(self):
        subprocess.call(["shutdown", "-r", "-t", "0"])

# Example usage
if __name__ == "__main__":
    gpio_controller = BootloaderConf()
    gpio_controller.assert_bootloader()
