#/bin/python3
'''
Service that handles requests from the user multiple different clients.
'''

import zmq
import json
from typing import Dict, Optional
from sys import path
path.append("/usr/local/lib/wand")
from neopixelLib import WandLed

class NeopixelService:
    def __init__(self):
        """
        Initializes the NeopixelService class, creating a ZeroMQ PULL socket and registering it with a poller.
        """
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind("tcp://*:5555")
        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)

        self.wandLed = WandLed(2)

    def read_msg(self) -> None:
        """
        Reads messages from the ZeroMQ socket and performs actions based on the message type.
        Available message types:
        - "set_button_led": Set the LED color for a button.
        - "blink": Blink the LED with specified parameters.
        - "blink_fast": Fast blink with specified parameters.
        - "blink_3": Blink three times with specified parameters.
        - "blink_n": Blink 'n' times with specified parameters.
        - "close": Close the NeopixelService.
        """
        socks = dict(self.poller.poll())
        if self.socket in socks:
            message = self.socket.recv_multipart()

            dict_message = json.loads(message[1])
            try:
                param0: Optional[int] = dict_message["param0"]
                param1: Optional[int] = dict_message["param1"]
                param2: Optional[int] = dict_message["param2"]
                param3: Optional[int] = dict_message["param3"]
            except KeyError:
                param0 = param1 = param2 = param3 = None

            if dict_message["type"] == "set_button_led":
                self.wandLed.set_button_led(param0, param1, param2, param3)
            elif dict_message["type"] == "blink":
                self.wandLed.blink(param0, param1, param2, param3)
            elif dict_message["type"] == "blink_fast":
                self.wandLed.blink_fast(param0)
            elif dict_message["type"] == "blink_3":
                self.wandLed.blink_3(param0)
            elif dict_message["type"] == "blink_n":
                self.wandLed.blink_n(param0, param1)
            elif dict_message["type"] == "close":
                self.wandLed.close()
            else:
                raise Exception(f"Invalid type option. Received {dict_message['type']}")

if __name__ == "__main__":
    neopixelService = NeopixelService()
    while True:
        neopixelService.read_msg()
