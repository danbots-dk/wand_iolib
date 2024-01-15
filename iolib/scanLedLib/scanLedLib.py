from sysfsPWM import PWM

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

    def __init__(self, dias: int = 0, flash: int = 1, frequency: int = 3000):
        """
        Initializes the ScanLed object.

        Args:
            dias (int): GPIO pin number for the 'dias' LED.
            flash (int): GPIO pin number for the 'flash' LED.
            frequency (int): PWM frequency in Hertz.
        """
        self.dias = PWM("pwmchip0", dias)
        self.dias.set_frequency(frequency)

        self.flash = PWM("pwmchip0", flash)        
        self.flash.set_frequency(frequency)


    def set_dias(self, duty_cycle: float):
        """
        Set the duty cycle for the 'dias' LED.

        Args:
            duty_cycle (float): Duty cycle value between 0.0 and 1.0.
        """
        self.dias.set_duty_cycle(duty_cycle)
        if(duty_cycle==0):
            self.dias.pwm_enable(0)
        else:
            self.dias.pwm_enable(1)

    def set_flash(self, duty_cycle: float):
        """
        Set the duty cycle for the 'flash' LED.

        Args:
            duty_cycle (float): Duty cycle value between 0.0 and 1.0.
        """
        self.flash.set_duty_cycle(duty_cycle)
        if(duty_cycle==0):
            self.flash.pwm_enable(0)
        else:
            self.flash.pwm_enable(1)

    def stop_pwm(self):
        """Stop PWM and close GPIO connections."""
        self.set_dias(0)
        self.set_flash(0)
        self.dias.unexport_pwm_channel()
        self.flash.unexport_pwm_channel()
        

if __name__ == "__main__":
    try:
        import numpy as np
        pwm = ScanLed()
        for i in np.arange(0.0, 1.0, 0.1):
            pwm.set_dias(i)  # Set the PWM duty cycle as a percentage (e.g., 50%)
            time.sleep(0.1)
        for i in np.arange(1, 0.0, -0.1):
            pwm.set_dias(i)  # Set the PWM duty cycle as a percentage (e.g., 50%)
            time.sleep(0.1)
        pwm.set_dias(0)
        time.sleep(1)
        pwm.stop_pwm()

    except KeyboardInterrupt:
        pass
    finally:
        try:
            pwm.stop_pwm()
        except:
            print("PWM probably already destroyed")
