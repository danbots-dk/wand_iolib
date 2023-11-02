"wandio client"
from sys import path
from time import sleep
path.append("/usr/local/lib/wand")
from iolib.led import WandLed       # pylint: disable=wrong-import-position

SLEEP_TIME = 5

def sleepn(sleep_time):
    "print sleep message and sleep"
    print(f"Sleep {sleep_time}")
    sleep(sleep_time)

#led1 = WandLed(1)
led2 = WandLed(2)
#led3 = WandLed(3)
# print("Turning LED1 on")
# led1.on()
# sleepn(SLEEP_TIME)
# print("Turnining LED1 off")
# led1.off()
# sleepn(SLEEP_TIME)
print("Turning LED2 on")
led2.on()
sleepn(SLEEP_TIME)
print("Turnining LED2 off")
led2.off()
sleepn(SLEEP_TIME)


print('Start blinking')
led2.blink()
sleepn(SLEEP_TIME)
print('Stop blinking')
led2.off()
sleepn(SLEEP_TIME)
print('Start blinking fast')
led2.blink_fast()
sleepn(SLEEP_TIME)
print('Stop blinking')
led2.off()
sleepn(SLEEP_TIME)
print("led on")
led2.on()
sleepn(SLEEP_TIME)
print("Turnining LED off")
led2.off()
sleepn(SLEEP_TIME)
print('Start blinking 3 fast')
led2.blink_3()
sleepn(SLEEP_TIME)
print('Stop blinking')
led2.off()

# print("Turning LED3 on")
# led3.on()
# sleepn(SLEEP_TIME)
# print("Turnining LED3 off")
# led3.off()
# sleepn(SLEEP_TIME)
