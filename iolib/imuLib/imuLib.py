
from adafruit_extended_bus import ExtendedI2C as I2C
import time
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_GAME_ROTATION_VECTOR,
    BNO_REPORT_STABILITY_CLASSIFIER,
    BNO_REPORT_ACTIVITY_CLASSIFIER,
    BNO_REPORT_ROTATION_VECTOR
)
from adafruit_bno08x.i2c import BNO08X_I2C
import math


class IMUlib:
    '''
    IMUlib class provides methods to interact with the BNO08X IMU sensor.
    
    Methods:
    - get_accel(): Returns the raw accelerometer readings.
    - get_accel_norm(): Returns the normalized accelerometer readings.
    - get_game_quaternion(): Returns the quaternion values for the game rotation vector.
    - get_relative_rotation_vector(radians=False): Returns the relative roll, pitch, and yaw values based on the game rotation vector quaternion. 
      If radians is True, the values are returned in radians; otherwise, they are returned in degrees.
    '''
    def __init__(self):
        '''
        Initializes the IMUlib object with the BNO08X IMU sensor.
        '''
        self.bno = BNO08X_I2C(I2C(8))
        self.bno.enable_feature(BNO_REPORT_ACCELEROMETER)
        self.bno.enable_feature(BNO_REPORT_GYROSCOPE)
        self.bno.enable_feature(BNO_REPORT_GAME_ROTATION_VECTOR)
        self.bno.enable_feature(BNO_REPORT_STABILITY_CLASSIFIER)
        self.bno.enable_feature(BNO_REPORT_ACTIVITY_CLASSIFIER)
        self.bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)
    
    def get_accel(self):
        '''
        Returns:
        dict: Dictionary containing the raw accelerometer readings for x, y, and z axes.
        '''
        accel_x, accel_y, accel_z = self.bno.acceleration
        accel = {
            'x': accel_x,
            'y': accel_y,
            'z': accel_z
        }
        return accel
    
    def get_accel_norm(self):
        '''
        Returns:
        dict: Dictionary containing the normalized accelerometer readings for x, y, and z axes.
        '''
        accel_x, accel_y, accel_z = self.bno.acceleration
        magnitude = (accel_x**2 + accel_y**2 + accel_z**2)**0.5
        normalized_x = accel_x / magnitude
        normalized_y = accel_y / magnitude
        normalized_z = accel_z / magnitude
        normalized_accel = {
            'x': normalized_x,
            'y': normalized_y,
            'z': normalized_z
        }
        return normalized_accel

    def _quaternion_to_euler_angle(self, quat_i, quat_j, quat_k, quat_real):
        '''
        Converts quaternion to euler angles.

        Args:
        quat_i (float): Quaternion i component.
        quat_j (float): Quaternion j component.
        quat_k (float): Quaternion k component.
        quat_real (float): Quaternion real component.

        Returns:
        tuple: Tuple containing roll, pitch, and yaw angles in radians.
        '''
        try:
            sinr_cosp = 2.0 * (quat_real * quat_i + quat_j * quat_k)
            cosr_cosp = 1.0 - 2.0 * (quat_i * quat_i + quat_j * quat_j)
            roll = math.atan2(sinr_cosp, cosr_cosp)

            sinp = 2.0 * (quat_real * quat_j - quat_k * quat_i)
            pitch = math.asin(sinp)

            siny_cosp = 2.0 * (quat_real * quat_k + quat_i * quat_j)
            cosy_cosp = 1.0 - 2.0 * (quat_j * quat_j + quat_k * quat_k)
            yaw = math.atan2(siny_cosp, cosy_cosp)
        except:
            print("gimball lock - moving on")

        return roll, pitch, yaw
    
    def get_game_quaternion(self):
        '''
        Returns:
        dict: Dictionary containing the quaternion values for the game rotation vector (i, j, k, and real parts).
        '''
        quat_i, quat_j, quat_k, quat_real = self.bno.game_quaternion
        game_quaternion = {
            'i': quat_i,
            'j': quat_j,
            'k': quat_k,
            'real': quat_real
        }
        return game_quaternion
    

    def get_relative_rotation_vector(self, radians=False):
        '''
        Returns the relative roll, pitch, and yaw values based on the game rotation vector quaternion.

        Args:
        radians (bool, optional): If True, returns the values in radians. If False (default), returns the values in degrees.

        Returns:
        dict: Dictionary containing the relative roll, pitch, and yaw values.
        '''
        game_quaternion = self.get_game_quaternion()
        roll, pitch, yaw = self._quaternion_to_euler_angle(game_quaternion['i'], game_quaternion['j'], game_quaternion['k'], game_quaternion['real'])
        if radians:
            relative_rot_vector = {
                'roll': roll,
                'pitch': pitch,
                'yaw': yaw
            }
        else:
            relative_rot_vector = {
                'roll': math.degrees(roll),
                'pitch': math.degrees(pitch),
                'yaw': math.degrees(yaw)
            }
        return relative_rot_vector


    def get_quaternion(self):
        '''
        Returns:
        dict: Dictionary containing the quaternion values for the game rotation vector (i, j, k, and real parts).
        '''
        quat_i, quat_j, quat_k, quat_real = self.bno.quaternion
        game_quaternion = {
            'i': quat_i,
            'j': quat_j,
            'k': quat_k,
            'real': quat_real
        }
        return game_quaternion
    

    def get_absolute_rotation_vector(self, radians=False):
        '''
        Returns the relative roll, pitch, and yaw values based on the game rotation vector quaternion.

        Args:
        radians (bool, optional): If True, returns the values in radians. If False (default), returns the values in degrees.

        Returns:
        dict: Dictionary containing the relative roll, pitch, and yaw values.
        '''
        quaternion = self.get_quaternion()
        roll, pitch, yaw = self._quaternion_to_euler_angle(quaternion['i'], quaternion['j'], quaternion['k'], quaternion['real'])
        if radians:
            relative_rot_vector = {
                'roll': roll,
                'pitch': pitch,
                'yaw': yaw
            }
        else:
            relative_rot_vector = {
                'roll': math.degrees(roll),
                'pitch': math.degrees(pitch),
                'yaw': math.degrees(yaw)
            }
        return relative_rot_vector

    def device_in_motion(self):
        '''
        Returns:
        bool: True if device is in motion, False otherwise
        '''
        activity_classification = self.bno.stability_classification
        if activity_classification == "In motion":
            return True
        else:
            return False

def main():
    '''
    Main function to demonstrate the usage of IMUlib.
    '''
    imu = IMUlib()
    while(1):
        #x = imu.get_relative_rotation_vector()
        x = imu.get_absolute_rotation_vector()
        print(x)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
