from sys import path
path.append("/usr/local/lib/wand/iolib")
from ioLib2 import WandIO
import time
from typing import Callable, Optional
import gpiod

class Button:
    def __init__(self):
        """
        Initializes the Button class with a WandIO instance.
        """
        self.wand = WandIO()
        self.reset_button()

    def set_button_interrupt(self, callback: Callable[[gpiod.LineEvent], None], longPress_callback: Callable, button: str) -> None:
        """
        Sets up an interrupt for the specified button.

        Args:
            callback (Callable[[gpiod.LineEvent], None]): The callback function to handle the interrupt.
            longPress_callback (Callable): Callback function to handle long press.
            button (str): The button identifier ("front_top", "front_button", or "onoff_button").
        """

        if button == "front_button1":
            # Interrupt handler for button1, callback runs in a separate thread 
            self.wand.configure_interrupt(chip_label="mcp", gpio_list=[2, "button1"], rising_or_falling=0, hold=longPress_callback, callback=callback)
        elif button == "front_button2":
            # Interrupt handler for button2, callback runs in a separate thread    
            self.wand.configure_interrupt(chip_label="mcp", gpio_list=[3, "button2"], rising_or_falling=0, hold=longPress_callback, callback=callback)
        elif button == "onoff_button":
            # Interrupt handler for on/off ic (max16150)
            self.wand.configure_interrupt(chip_label="rpi", gpio_list=[27, "on_off_ic"], debounce=0.1, rising_or_falling=0, hold=longPress_callback, callback=callback)
        else:
            raise Exception(f"Button name input incorrect, received {button}")

    

    def reset_button(self) -> None:
        """
        Resets the button by toggling its output state.
        """
        self.wand.set_output("mcp", 1, 0)
        time.sleep(0.01)
        self.wand.set_output("mcp", 1, 1)

    def set_on_off_button_interrupt(self, callback: Callable[[gpiod.LineEvent], None]) -> None:
        """
        Sets up an interrupt for the on/off button press.

        Args:
            callback (Callable[[gpiod.LineEvent], None]): The callback function to handle the interrupt.
        """
        self.wand.configure_interrupt(chip_label="rpi", gpio_list=[26, "on_off_button"], callback=callback)

if __name__ == "__main__":
    import time

    def int_callback(event: gpiod.LineEvent) -> None:
        print("interrupt")

    def onoff_callback(event: gpiod.LineEvent) -> None:
        print("interrupt_onoff")

    def hold():
        print("holding123")

    button = Button()
    #button.set_button_interrupt(callback=int_callback, button="front_button1")
    button.set_button_interrupt(callback=int_callback, longPress_callback=None, button="front_button2")
    button.set_button_interrupt(callback=onoff_callback,longPress_callback=hold, button="onoff_button")
    # button.wand.set_output("mcp", 1, 1)

    while True:
        reset = input("press enter to reset")
        button.reset_button()
        time.sleep(0.1)
