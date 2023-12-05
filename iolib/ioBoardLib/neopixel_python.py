import smbus
import time


NEOPIXEL = 0
VIB_MOTOR = 1
# Define Arduino's I2C address
arduino_address = 0x08
bus = smbus.SMBus(1)  # For Raspberry Pi, use 1. For others, check your platform documentation.

def set_io(index = 0, r = 0, g = 0, b = 0, vib_state = 0):
    # Send LED color data to Arduino over I2C
    bus.write_i2c_block_data(arduino_address, 1, [index, r, g, b, vib_state])


def cycle_leds():
    # Turn on LEDs one by one
    for i in range(0, 6):
        set_io(i, 0, 255, 0)  # Green color
        time.sleep(1)

    # Turn off LEDs in reverse order
    for i in range(7, 0, -1):
        set_io(i, 0, 0, 0)  # Turn off LEDs
        time.sleep(1)


def turn_off_all_leds():
    # Turn off all LEDs
    for i in range(0, 7):
        set_io(i, 0, 0, 0)  # Black color (off)
    time.sleep(1)

def start_routine():

    # Flash all LEDs in green for a second
    for _ in range(2):  # Flash twice
        for i in range(1, 8):
            set_io(index = i, r=0, g=255, b=0, vib_state=1)  # g color
        
        time.sleep(0.25)
        for i in range(1, 8):
            set_io(index = i, r=0, g=0, b=0, vib_state=0)  # g color
        time.sleep(0.25)

def main():
    try:
        while True:
            # Example: Set LED 2 to red
            start_routine()
            time.sleep(1)

            #cycle_leds()
            #turn_off_all_leds()


    except KeyboardInterrupt:
        # Clean up on program exit
        print("Exiting...")
        turn_off_all_leds()
        bus.close()

if __name__ == "__main__":
    main()
