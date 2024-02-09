import os
import time
import threading

class SysLED:
    def __init__(self, channel=0):
        self.red = f"/sys/class/leds/red_{channel}/"
        self.green = f"/sys/class/leds/green_{channel}/"
        self.blue = f"/sys/class/leds/blue_{channel}/"

        self.color = "red"
        self.blink_thread = None
        self.stop_event = threading.Event()

    def set_brightness(self, r=None, g=None, b=None):
        if r != None:
            r = max(0, min(r, 255))  # Ensure brightness is between 0 and 255
            with open(os.path.join(self.red, "brightness"), "w") as f:
                f.write(str(r))
        if g != None:
            g = max(0, min(g, 255))  # Ensure brightness is between 0 and 255
            with open(os.path.join(self.green, "brightness"), "w") as f:
                f.write(str(g))
        if b != None:
            b = max(0, min(b, 255))  # Ensure brightness is between 0 and 255
            with open(os.path.join(self.blue, "brightness"), "w") as f:
                f.write(str(b))

    def blink_worker(self, r, g, b, on_time, off_time, n):
        while n > 0 and not self.stop_event.is_set():
            self.set_brightness(r, g, b)
            time.sleep(on_time)
            if not self.stop_event.is_set():
                self.set_brightness(0,0,0)
                time.sleep(off_time)
            n -= 1

    def blink(self, r,g,b, on_time=1, off_time=1, n=None):
        self.stop_event.clear()
        self.blink_thread = threading.Thread(target=self.blink_worker, args=(r,g,b, on_time, off_time, n))
        self.blink_thread.start()

    def stop_blink(self):
        self.stop_event.set()
        if self.blink_thread:
            self.blink_thread.join()

    def on(self, r=0, g=0, b=0):
        self.set_brightness(r, g, b)

    def off(self):
        self.set_brightness(0,0,0)

# Example usage:
if __name__ == "__main__":
    led = SysLED(channel=0)
    led.blink(r=255, g=200, b=0, on_time=0.5, off_time=0.5, n=5)
    print("keep blinking in separate thread")
    time.sleep(8)
    led.stop_blink()
