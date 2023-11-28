from gpiozero import PWMOutputDevice
import time

class ScanLed:
    def __init__(self, dias=12, flash=13, frequency=1000):
        self.dias = dias
        self.flash = flash
        self.frequency = frequency

        # Initialize PWM devices
        self.pwm1 = PWMOutputDevice(self.dias, frequency=self.frequency)
        self.pwm2 = PWMOutputDevice(self.flash, frequency=self.frequency)

    def set_dias(self, duty_cycle):
        self.pwm1.value = duty_cycle

    def set_flash(self, duty_cycle):
        self.pwm2.value = duty_cycle

    def stop_pwm(self):
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
