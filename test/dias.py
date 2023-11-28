"Test of projector led functionality"
from sys import path
from time import sleep
path.append("/usr/local/lib/wand/iolib")
from led import WandLed         # pylint: disable=wrong-import-position, import-error
from scanLedLib import ScanLed  # pylint: disable=wrong-import-position, import-error


led = ScanLed()
print("Turning dias on")
led.set_dias(1)
print("pause")
sleep(3)
print("Turn off")
led.set_dias(0)
sleep(3)
print("Turning flash on")
led.set_dias(1)
print("pause")
sleep(3)
print("Turn off")
led.set_dias(0)
print("close")
