from gpiozero import PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
#from gpiozero.pins.rpio import RPIOPin
import time

class ScanLed:
    """
    Class for controlling hardware PWM on Raspberry Pi for scanning LED lights.

    Attributes:
        dias (int): GPIO pin number for the 'dias' LED.
        flash (int): GPIO pin number for the 'flash' LED.
        frequency (int): PWM frequency in Hertz.

    Methods:
        set_dias(duty_cycle): Set the duty cycle for the 'dias' LED.
        set_flash(duty_cycle): Set the duty cycle for the 'flash' LED.
        stop_pwm(): Stop PWM and close GPIO connections.
    """

    def __init__(self, dias: int = 12, flash: int = 13, frequency: int = 3000):
        """
        Initializes the ScanLed object.

        Args:
            dias (int): GPIO pin number for the 'dias' LED.
            flash (int): GPIO pin number for the 'flash' LED.
            frequency (int): PWM frequency in Hertz.
        """
        self.dias = dias
        self.flash = flash
        self.frequency = frequency

        # Initialize PWM devices
        factory = PiGPIOFactory()
        self.pwm1 = PWMOutputDevice(self.dias, frequency=self.frequency, pin_factory=factory)
        self.pwm2 = PWMOutputDevice(self.flash, frequency=self.frequency, pin_factory=factory)

    def set_dias(self, duty_cycle: float):
        """
        Set the duty cycle for the 'dias' LED.

        Args:
            duty_cycle (float): Duty cycle value between 0.0 and 1.0.
        """
        self.pwm1.value = duty_cycle

    def set_flash(self, duty_cycle: float):
        """
        Set the duty cycle for the 'flash' LED.

        Args:
            duty_cycle (float): Duty cycle value between 0.0 and 1.0.
        """
        self.pwm2.value = duty_cycle

    def stop_pwm(self):
        """Stop PWM and close GPIO connections."""
        self.pwm1.close()
        self.pwm2.close()

if __name__ == "__main__":
    try:
        pwm_controller = ScanLed(dias=12, flash=13, frequency=5000)
        pwm_controller.set_dias(duty_cycle=0.5)
        pwm_controller.set_flash(duty_cycle=0.5)

        # Run your PWM-controlled code here
        time.sleep(10)  # Run for 10 seconds

        pwm_controller.set_dias(duty_cycle=0.75)
        pwm_controller.set_flash(duty_cycle=0.25)
        time.sleep(5)  # Run for an additional 5 seconds

    except KeyboardInterrupt:
        pass
    finally:
        pwm_controller.stop_pwm()
