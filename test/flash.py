"Test of flash led functionality"
from sys import path
from time import sleep
path.append("/usr/local/lib/wand/iolib")
from led import WandLed         # pylint: disable=wrong-import-position, import-error
from scanLedLib import ScanLed  # pylint: disable=wrong-import-position, import-error

NEW = True

if NEW:
    led = ScanLed()
    print("Turning flash on")
    led.set_flash(1)
    print("pause")
    sleep(3)
    print("Turn off")
    led.set_flash(0)
    print("Turning flash on")
    led.set_flash(1)
    print("pause")
    sleep(3)
    print("close")
else:
    print("Turning flash on")
    led = WandLed(2)
    led.on()
    print("pause")
    sleep(3)
    print("Turn off")
    led.off()
