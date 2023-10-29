"Wand led library"

#   231027  PLH     First version for Pizero test with gpiozero
#
# the following LEDs are implemented:
#
# Led 1: status led
#   signals the general status of the device, eg ConfigMode, NormalOperation, NoNetworkConnection
#
# Led 2: Camera flash light
# Led 3: Scanner Projecktor
#


NO_LED = 3      # number of suported leds

LED_STATUS = 1
LED_CAMERA_FLASH = 2
LED_PROJECTOR = 3

# HW models
HW_PIZERO = "PIZERO"
HW_CM4 = "CM4"
HW_CM4_1 = "CM4_1"

# DETECT HW
HW="PIZERO"

if HW=="PIZERO":
    from gpiozero import LED
    LED_PINS = [17, 17, 17]


PIZERO_LED = 17

class WandLed():
    """
    Represents a wand led with typical on/off and blink behaviour.

    :type led_number: int
    :param led_number:
    """

    def __init__(self, led_number):
        if led_number<=0 or led_number>NO_LED:
            raise Exception("Illegal led_number")
        
        self._pin = LED_PINS[led_number-1]
        self._led = LED(self._pin)

    @property
    def value(self):
        "get current value of led"
        return self._led.value

    def close(self):
        "close driver"
        self._led.close()

    def on(self):
        "Turn LED on"
        self._led.on()

    def off(self):
        "Turn LED off"
        self._led.off()

    def blink(self, on_time=1, off_time=1):
        """
        Make the device turn on and off repeatedly.

        :param float on_time:
            Number of seconds on. Defaults to 1 second.

        :param float off_time:
            Number of seconds off. Defaults to 1 second.
       """
        self._led.blink(on_time=on_time, off_time=off_time, n=None, background=True)

    def blink_fast(self):
        "Blink fast"
        self._led.blink(on_time=0.2, off_time=0.2, n=None, background=True)
    
    def blink_3(self):
        "Blink 3 very fast"
        self._led.blink(on_time=0.1, off_time=0.1, n=3, background=True)
