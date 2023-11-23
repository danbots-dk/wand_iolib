#!/bin/python3
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
import board

# Initialize the I2C and LSM6DS3 sensor


class IMU():
    def __init__(self):
        i2c = board.I2C()
        self.sox = LSM6DS3(i2c)

    def get_acc(self):
        acc_state = {
            "x": f"{self.sox.acceleration[0]:.2f}",
            "y": f"{self.sox.acceleration[1]:.2f}",
            "z": f"{self.sox.acceleration[2]:.2f}"
        }
        return acc_state
    
    def get_gyro(self):
        gyro_state = {
            "x": f"{self.sox.gyro[0]:.2f}",
            "y": f"{self.sox.gyro[1]:.2f}",
            "z": f"{self.sox.gyro[2]:.2f}",
        }
        return gyro_state



imu = IMU()
acc_value = imu.get_acc()
print(acc_value["x"])