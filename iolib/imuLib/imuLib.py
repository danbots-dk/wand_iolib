#!/bin/python3
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
import board
from typing import Dict

class IMU:
    def __init__(self):
        """
        Initializes the IMU class with the I2C and LSM6DS3 sensor.
        """
        i2c = board.I2C()
        self.sox = LSM6DS3(i2c)

    def get_acc(self) -> Dict[str, str]:
        """
        Gets the acceleration values from the LSM6DS3 sensor.

        Returns:
            Dict[str, str]: A dictionary containing acceleration values for x, y, and z axes.
        """
        acc_state = {
            "x": f"{self.sox.acceleration[0]:.2f}",
            "y": f"{self.sox.acceleration[1]:.2f}",
            "z": f"{self.sox.acceleration[2]:.2f}"
        }
        return acc_state
    
    def get_gyro(self) -> Dict[str, str]:
        """
        Gets the gyroscope values from the LSM6DS3 sensor.

        Returns:
            Dict[str, str]: A dictionary containing gyroscope values for x, y, and z axes.
        """
        gyro_state = {
            "x": f"{self.sox.gyro[0]:.2f}",
            "y": f"{self.sox.gyro[1]:.2f}",
            "z": f"{self.sox.gyro[2]:.2f}",
        }
        return gyro_state

if __name__ == "__main__":
    imu = IMU()
    acc_value = imu.get_acc()
    print(acc_value["x"])
