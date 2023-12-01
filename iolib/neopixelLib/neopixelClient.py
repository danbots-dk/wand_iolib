#!/bin/python

import zmq
import json
from typing import Optional

class RGBLED:
    def __init__(self, client_name: str = "client1"):
        """
        Initializes the RGBLED class with a ZeroMQ PUSH socket.

        Args:
            client_name (str): The name of the client (default is "client1").
        """
        self.client_name = client_name

    def _send_message(self, message: dict) -> None:
        """
        Sends a JSON-encoded message via ZeroMQ PUSH socket.

        Args:
            message (dict): The message to be sent.
        """
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        message = json.dumps(message)
        message = message.encode()
        self.socket.connect("tcp://localhost:5555")
        self.socket.send_multipart([(self.client_name).encode('ASCII'), message])
        self.socket.close()
        self.context.term()

    def set_button_led(self, location: int, r: int, g: int, b: int) -> None:
        """
        Sets the LED color for a button.

        Args:
            location (int): The location of the LED.
            r (int): Red component (0-255).
            g (int): Green component (0-255).
            b (int): Blue component (0-255).
        """
        msg = {
            "type": "set_button_led",
            "param0": location,
            "param1": r,
            "param2": g,
            "param3": b
        }
        self._send_message(msg)

    def blink_n(self, location: int, on_time: int, off_time: int, n: int) -> None:
        """
        Blinks the LED 'n' times with specified on and off times.

        Args:
            location (int): The location of the LED.
            on_time (int): Time the LED is ON in seconds.
            off_time (int): Time the LED is OFF in seconds.
            n (int): Number of times to blink.
        """
        msg = {
            "type": "blink_n",
            "param0": location,
            "param1": on_time,
            "param2": off_time,
            "param3": n
        }
        self._send_message(msg)

    def blink_fast(self, location: int) -> None:
        """
        Fast blinks the LED with default parameters.

        Args:
            location (int): The location of the LED.
        """
        msg = {
            "type": "blink_fast",
            "param0": location,
            "param1": 999,
            "param2": 999,
            "param3": 999
        }
        self._send_message(msg)

    def blink_3(self, location: int) -> None:
        """
        Blinks the LED three times with default parameters.

        Args:
            location (int): The location of the LED.
        """
        msg = {
            "type": "blink_3",
            "param0": location,
            "param1": 999,
            "param2": 999,
            "param3": 999
        }
        self._send_message(msg)

    def close_led(self) -> None:
        """
        Closes the RGBLED by sending a close message.
        """
        msg = {
            "type": "close",
            "param0": 999,
            "param1": 999,
            "param2": 999,
            "param3": 999
        }
        self._send_message(msg)


if __name__ == "__main__":
    import time
    led = RGBLED()
    led.blink_3(0)

    time.sleep(3)
    led.blink_3(0)
    time.sleep(0.1)
    led.set_button_led(1,0,0,0)
    time.sleep(0.1)
    #led.close()