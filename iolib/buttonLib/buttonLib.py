from ioLib2 import WandIO




class Button():
    def __init__(self):
        self.wand = WandIO()

    def set_button_interrupt(self, callback, button):
        if (button == "front_top"):
            # Interrupt handler for button1, callback runs in seperate thread 
            self.wand.configure_interrupt(chip_label="mcp", gpio_list=[2, "button1"], callback=callback)
        elif (button == "front_button"):
             # Interrupt handler for button2, callback runs in seperate thread    
            self.wand.configure_interrupt(chip_label="mcp", gpio_list=[3, "button2"], callback=callback)
        elif (button == "onoff_button"):
            # Interrupt handler for on/off ic (max16150)
            self.wand.configure_interrupt(chip_label="rpi", gpio_list=[27, "on_off_ic"], callback=callback)

    # Interrupt handler for on/off button press
    # Use set_on_off_ic_interrupt() instead unless you know what you are doing
    def set_on_off_button_interrupt(self, callback):
        self.wand.configure_interrupt(chip_label="rpi", gpio_list=[26, "on_off_button"], callback=callback)

if __name__ == "__main__":
    import time
    def int_callback(event):
        print("interrupt")

    button=Button()
    button.set_button_interrupt(callback=int_callback, button="front_top")

    while(1):
        time.sleep(0.1)
        pass