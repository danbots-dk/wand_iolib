import os
import time

class PWM:
    """A class to control PWM (Pulse Width Modulation) signals on Linux-based systems.

    Args:
        pwm_chip (str): The name of the PWM chip, e.g., "pwmchip0".
        pwm_channel (int): The channel number of the PWM, e.g., 0.

    Attributes:
        pwm_chip (str): The name of the PWM chip.
        pwm_channel (int): The channel number of the PWM.
        base_path (str): The base path of the PWM directory.

    Raises:
        FileNotFoundError: If the specified PWM channel does not exist.

    """

    def __init__(self, pwm_chip, pwm_channel):
        self.pwm_chip = pwm_chip
        self.pwm_channel = pwm_channel
        self.base_path = f"/sys/class/pwm/{pwm_chip}/pwm{pwm_channel}/"

        if not os.path.exists(self.base_path):
            self.export_pwm_channel()

    def export_pwm_channel(self):
        """Export the PWM channel if it does not exist."""

        pwm_export_path = f"/sys/class/pwm/{self.pwm_chip}/export"
        with open(pwm_export_path, "w") as f:
            f.write(str(self.pwm_channel))

    def unexport_pwm_channel(self):
        """Unexport the PWM channel."""

        pwm_export_path = f"/sys/class/pwm/{self.pwm_chip}/unexport"
        with open(pwm_export_path, "w") as f:
            f.write(str(self.pwm_channel))

    def set_duty_cycle(self, duty_cycle_normalized):
        """Set the duty cycle of the PWM signal.

        Args:
            duty_cycle_normalized (float): The duty cycle as a normalized value between 0 and 1.

        Raises:
            ValueError: If the duty cycle percentage is not between 0 and 100.

        """

        duty_cycle_percent = int(duty_cycle_normalized * 100.0)
        if duty_cycle_percent < 0 or duty_cycle_percent > 100:
            raise ValueError("Duty cycle percentage must be between 0 and 100.")

        period_ns = int(1e9 / self.get_frequency())  # Convert Hertz to nanoseconds
        duty_cycle_ns = int((duty_cycle_percent / 100) * period_ns)

        with open(os.path.join(self.base_path, "duty_cycle"), "w") as f:
            f.write(str(duty_cycle_ns))

    def pwm_enable(self, enable):
        """Enable or disable the PWM signal.

        Args:
            enable (int): 1 to enable the PWM signal, 0 to disable it.

        """

        with open(os.path.join(self.base_path, "enable"), "w") as f:
            f.write(str(enable))

    def set_frequency(self, frequency_hz):
        """Set the frequency of the PWM signal.

        Args:
            frequency_hz (float): The frequency of the PWM signal in Hertz.

        """

        period_ns = int(1e9 / frequency_hz)  # Convert Hertz to nanoseconds
        with open(os.path.join(self.base_path, "period"), "w") as f:
            f.write(str(period_ns))

    def get_frequency(self):
        """Get the frequency of the PWM signal.

        Returns:
            float: The frequency of the PWM signal in Hertz.

        """

        period_ns = self.get_period_ns()
        return 1e9 / period_ns  # Convert nanoseconds to Hertz

    def get_period_ns(self):
        """Get the period of the PWM signal.

        Returns:
            int: The period of the PWM signal in nanoseconds.

        """

        with open(os.path.join(self.base_path, "period"), "r") as f:
            period_ns = int(f.read())
        return period_ns
    

if __name__ == "__main__":
    import numpy as np
    try:
        pwm = PWM("pwmchip0", 0)  # Change "pwmchip0" and 0 to your specific PWM chip and channel
        pwm.set_frequency(2000)  # Set the PWM frequency in Hertz (e.g., 2000 Hz)
        pwm.set_duty_cycle(1)
        pwm.pwm_enable(1)
        time.sleep(2)
        for i in np.arange(0.0, 1.0, 0.1):
            pwm.set_duty_cycle(i)  # Set the PWM duty cycle as a percentage (e.g., 50%)
            time.sleep(0.1)
        for i in np.arange(1, 0.0, -0.1):
            pwm.set_duty_cycle(i)  # Set the PWM duty cycle as a percentage (e.g., 50%)
            time.sleep(0.1)
        pwm.pwm_enable(0)
        # Do other operations with the PWM as needed

    except FileNotFoundError as e:
        print(e)
