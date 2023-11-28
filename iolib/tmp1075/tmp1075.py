import sensors
import time

class CarrierbrdTemp():
    def __init__(self):
        pass

    def read_PCB_temp(sensor_name='temp1'):
        """
        Reads the temperature of the carrier board PCB.

        Args:
            sensor_name (str): sensor label

        Returns:
            lm75_temp (float): temperature in celcius
        """
        sensors.init()
        try:
            for chip in sensors.iter_detected_chips():
                for feature in chip:
                    if feature.label == sensor_name:
                        lm75_temp = feature.get_value()
                        return lm75_temp

        except Exception as e:
            print(f"Error: {e}")

        finally:
            sensors.cleanup()

if __name__ == "__main__":
    pcbTemp = CarrierbrdTemp()
    print(CarrierbrdTemp.read_PCB_temp())
