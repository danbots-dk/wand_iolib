"wandio client"
from sys import path
from time import sleep
path.append("/usr/local/lib/wand")
from iolib.led import WandLed

SLEEP_TIME = 5

def sleepn(sleep_time):
    "print sleep message and sleep"
    print(f"Sleep {sleep_time}")
    sleep(sleep_time)

led = WandLed(1)

print("Turning LED on")
led.on()
sleepn(SLEEP_TIME)
print("Turnining LED off")
led.off()
sleepn(SLEEP_TIME)
print('Start blinking')
led.blink()
sleepn(SLEEP_TIME)
print('Stop blinking')
led.off()
sleepn(SLEEP_TIME)
print('Start blinking fast')
led.blink_fast()
sleepn(SLEEP_TIME)
print('Stop blinking')
led.off()
sleepn(SLEEP_TIME)
print("led on")
led.on()
sleepn(SLEEP_TIME)
print("Turnining LED off")
led.off()
sleepn(SLEEP_TIME)
print('Start blinking 3 fast')
led.blink_3()
sleepn(SLEEP_TIME)
print('Stop blinking')
led.off()
