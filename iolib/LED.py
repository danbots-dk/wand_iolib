import os


# Set onboard activity led state
def set_activity_led(on_or_off):
    # 0: Turn activity led off
    # 1: Turn activity led on
    try:
        os.system(f'sudo sh -c "echo {on_or_off} > /sys/class/leds/ACT/brightness"')
    except:
        print("Activity LED failed. You are probably not root.")
        return 0
    
# Set onboard power led state
def set_power_led(on_or_off):
    # 0: Turn power led off
    # 1: Turn power led on
    try:
        os.system(f'sudo sh -c "echo {on_or_off} > /sys/class/leds/PWR/brightness"')
    except:
        print("Activity LED failed. You are probably not root.")
        return 0