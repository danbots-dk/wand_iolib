import gpiod
import time
import threading
import os
from sys import path
from typing import List, Optional, Callable, Union

current_path = os.getcwd()

if current_path.startswith("/usr/local/lib/wand"):
    path.append("/usr/local/lib/wand")
else:
    path.append("/home/peter/iolib")

class WandIO:
    def __init__(self):
        """
        Initializes WandIO class, creating instances for GPIO chips and setting up initial configurations.
        """
        chip_label0 = 'gpiochip0'
        chip_label2 = 'gpiochip2'

        self.chip0 = gpiod.Chip(chip_label0)
        self.chip2 = gpiod.Chip(chip_label2)

        self.mcp_input_lines = [[0, 6, 7], ["power_stat", "power", "power"]]
        self.rpi_input_lines = [[], []]
        
        self.mcp_output_lines = [[1, 4, 5], ["cap_rst", "mirror_heat", "sound"]] 
        self.rpi_output_lines = [[4, 12, 13, 22], ["bootloader","DIAS", "flash" "kill"]]

        self.mcp_interrupt_lines = [[2, 3], ["button1", "button2"]]
        self.rpi_interrupt_lines = [[27, 6, 17], ["on_off_interrupt", "carrier_pcb_temp", "battery_fuel_interrupt"]]

        self.mcp_gpio_lines = {} 
        self.rpi_gpio_lines = {}


    def configure_input(self, chip_label: str, gpio_list: List[Union[int, str]]) -> Optional[int]:
        """
        Configures an input pin on the specified GPIO chip.

        Args:
            chip_label (str): Label of the GPIO chip ("rpi" or "mcp").
            gpio_list (List[Union[int, str]]): List containing pin number and consumer name.

        Returns:
            Optional[int]: None if the configuration fails, otherwise 0.
        """
        if chip_label == "rpi":
            if gpio_list[0] not in self.rpi_gpio_lines:
                gpio_line = self.chip0.get_line(gpio_list[0])
                gpio_line.request(consumer=gpio_list[1], type=gpiod.LINE_REQ_DIR_IN)
                self.rpi_gpio_lines[gpio_list[0]] = gpio_line
            else:
                print(f"Cannot configure input on {chip_label} pin {gpio_list[0]}. Is there an existing configuration on the same pins elsewhere?")
                return None
        elif chip_label == "mcp":
            if gpio_list[0] not in self.mcp_gpio_lines:
                gpio_line = self.chip2.get_line(gpio_list[0])
                gpio_line.request(consumer=gpio_list[1], type=gpiod.LINE_REQ_DIR_IN)
                self.mcp_gpio_lines[gpio_list[0]] = gpio_line
            else:
                print(f"Cannot configure input on {chip_label} pin {gpio_list[0]}. Is there an existing configuration on the same pins elsewhere?")
                return None
        return 0

    def read_input(self, chip_label: str, pin_number: int) -> Optional[bool]:
        """
        Reads the state of the specified input pin.

        Args:
            chip_label (str): Label of the GPIO chip ("rpi" or "mcp").
            pin_number (int): Pin number to read.

        Returns:
            Optional[bool]: None if the pin is not found, otherwise the state of the pin.
        """
        if chip_label == "rpi":
            if pin_number in self.rpi_gpio_lines:
                gpio_line = self.rpi_gpio_lines[pin_number]
                if gpio_line.is_requested():
                    return gpio_line.get_value()
        elif chip_label == "mcp":
            if pin_number in self.mcp_gpio_lines:
                gpio_line = self.mcp_gpio_lines[pin_number]
                if gpio_line.is_requested():
                    return gpio_line.get_value()
        return None

    def configure_output(self, chip_label: str, gpio_list: List[Union[int, str]]) -> Optional[int]:
        """
        Configures an output pin on the specified GPIO chip.

        Args:
            chip_label (str): Label of the GPIO chip ("rpi" or "mcp").
            gpio_list (List[Union[int, str]]): List containing pin number and consumer name.

        Returns:
            Optional[int]: None if the configuration fails, otherwise 0.
        """
        if chip_label == "rpi":
            if gpio_list[0] not in self.rpi_gpio_lines:
                gpio_line = self.chip0.get_line(gpio_list[0])
                gpio_line.request(consumer=gpio_list[1], type=gpiod.LINE_REQ_DIR_OUT)
                self.rpi_gpio_lines[gpio_list[0]] = gpio_line
            else:
                print(f"Cannot configure output on {chip_label} pin {gpio_list[0]}. Is there an existing configuration on the same pins elsewhere?")
                return None
        elif chip_label == "mcp":
            if gpio_list[0] not in self.mcp_gpio_lines:
                gpio_line = self.chip2.get_line(gpio_list[0])
                gpio_line.request(consumer=gpio_list[1], type=gpiod.LINE_REQ_DIR_OUT)
                self.mcp_gpio_lines[gpio_list[0]] = gpio_line
            else:
                print(f"Cannot configure output on {chip_label} pin {gpio_list[0]}. Is there an existing configuration on the same pins elsewhere?")
                return None
        return 0

    def set_output(self, chip_label: str, pin_number: int, value: int) -> None:
        """
        Sets the state of the specified output pin.

        Args:
            chip_label (str): Label of the GPIO chip ("rpi" or "mcp").
            pin_number (int): Pin number to set.
            value (int): Value to set (0 or 1).
        """
        if chip_label == "rpi":
            if pin_number in self.rpi_gpio_lines:
                gpio_line = self.rpi_gpio_lines[pin_number]
                if gpio_line.is_requested():
                    gpio_line.set_value(value)
        elif chip_label == "mcp":
            if pin_number in self.mcp_gpio_lines:
                gpio_line = self.mcp_gpio_lines[pin_number]
                if gpio_line.is_requested():
                    gpio_line.set_value(value)

    def release_pin(self, chip_label: str, pin_number: int) -> None:
        """
        Releases the specified pin.

        Args:
            chip_label (str): Label of the GPIO chip ("rpi" or "mcp").
            pin_number (int): Pin number to release.
        """
        if chip_label == "rpi":
            if pin_number in self.rpi_gpio_lines:
                gpio_line = self.rpi_gpio_lines.pop(pin_number)
                gpio_line.release()
        elif chip_label == "mcp":
            if pin_number in self.mcp_gpio_lines:
                gpio_line = self.mcp_gpio_lines.pop(pin_number)
                gpio_line.release()

    def release_all_pins(self) -> None:
        """
        Releases all pins on both MCP and RPi.
        """
        rpi_keys = list(self.rpi_gpio_lines.keys())
        for pin_number in rpi_keys:
            gpio_line = self.rpi_gpio_lines.pop(pin_number)
            gpio_line.release()

        mcp_keys = list(self.mcp_gpio_lines.keys())
        for pin_number in mcp_keys:
            gpio_line = self.mcp_gpio_lines.pop(pin_number)
            gpio_line.release()

    def configure_interrupt(
        self,
        chip_label: str,
        gpio_list: List[Union[int, str]],
        debounce: float = 0.1,
        rising_or_falling: int = 0,
        hold: Callable = None,
        hold_time: float = 3,
        callback: Optional[Callable[[gpiod.LineEvent], None]] = None
    ) -> Optional[int]:
        """
        Configures an interrupt on the specified pin.

        Args:
            chip_label (str): Label of the GPIO chip ("rpi" or "mcp").
            gpio_list (List[Union[int, str]]): List containing pin number and consumer name.
            debounce (float): Debounce time in seconds.
            rising_or_falling: 1 for rising trigger, 0 for falling
            hold: If func is provided, func will be called after 3s hold time
            hold_time: time until hold func is envoked
            callback (Optional[Callable[[gpiod.LineEvent], None]]): Callback function to handle the interrupt.

        Returns:
            Optional[int]: None if the configuration fails, otherwise 0.
        """

        if rising_or_falling == 1:
            interrupt_type = gpiod.LINE_REQ_EV_RISING_EDGE
        elif rising_or_falling == 0:
            interrupt_type = gpiod.LINE_REQ_EV_FALLING_EDGE

        if callback is None:
            return None
        if chip_label == "mcp" and gpio_list[0] not in self.mcp_gpio_lines:
            gpio_line = self.chip2.get_line(gpio_list[0])
            gpio_line.request(consumer=gpio_list[1], type=interrupt_type)
            self.mcp_gpio_lines[gpio_list[0]] = gpio_line
        elif chip_label == "rpi" and gpio_list[0] not in self.rpi_gpio_lines:
            gpio_line = self.chip0.get_line(gpio_list[0])
            gpio_line.request(consumer=gpio_list[1], type=interrupt_type)
            self.rpi_gpio_lines[gpio_list[0]] = gpio_line
        else:
            print(f"Cannot create interrupt on {chip_label} pin {gpio_list[0]}. Is there an existing interrupt on the same pins elsewhere?")
            return None
            
        def interrupt_thread():
            while True:
                event = gpio_line.event_wait(10000)
                if event:
                    gpio_line.event_read()
                    callback(event)

                    # long press detection
                    # Works only for shutdown right now
                    if hold != None and (self.read_input("rpi", 26) == 0 or self.read_input("mcp", gpio_list[0]) == 1):
                        hold_time_tresh = 0
                        while self.read_input("rpi", 26) == 0 or self.read_input("mcp", gpio_list[0]) == 1:
                            hold_time_tresh = hold_time_tresh+0.1
                            time.sleep(0.1)
                            if hold_time_tresh > hold_time:
                                hold()

                    if chip_label == "mcp" and gpio_list[0] in self.mcp_gpio_lines:
                        self.mcp_gpio_lines.pop(gpio_list[0])
                    elif chip_label == "rpi" and gpio_list[0] in self.rpi_gpio_lines:
                        self.rpi_gpio_lines.pop(gpio_list[0])

                    gpio_line.release()
                    time.sleep(debounce)
                    self.configure_interrupt(chip_label=chip_label, gpio_list=gpio_list, debounce=debounce, rising_or_falling=rising_or_falling, hold=hold, hold_time=hold_time, callback=callback)
                    break

        thread = threading.Thread(target=interrupt_thread)
        thread.daemon = True
        thread.start()

    def get_primary_power_source(self) -> Optional[bool]:
        """
        Returns the state of the primary power source.

        Returns:
            Optional[bool]: None if the pin is not found, otherwise the state of the pin.
        """
        return self.read_input("mcp", 0)

# Function to test interrupt handling
def test_interrupt(event: gpiod.LineEvent) -> None:
    print("test interrupt123")

# Function to test interrupt handling
def test_interrupt2(event: gpiod.LineEvent) -> None:
    print("test2 interrupt1234")

if __name__ == "__main__":
    wand = WandIO()
    int1 = wand.configure_interrupt(chip_label="mcp", gpio_list=[3, "button2"], callback=test_interrupt)
    int2 = wand.configure_interrupt(chip_label="mcp", gpio_list=[2, "button1"], callback=test_interrupt2)
    wand.release_pin("mcp", 7)
    #wand.set_output("mcp",5,0)
    while(1):
        try:
            #print(wand.get_primary_power_source())
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("Releasing all pins")
            wand.release_all_pins()
            break
