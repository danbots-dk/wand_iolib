import sensors
import time

def read_lm75_temperature(sensor_name='temp1'):
    sensors.init()

    try:
        for chip in sensors.iter_detected_chips():
            
                
            for feature in chip:
                if feature.label == sensor_name:
                    while True:
                        # Read temperature data
                        lm75_temp = feature.get_value()

                        # Print the temperature
                        print(f"Temperature: {lm75_temp} °C")

                        # Adjust the delay based on your desired reading frequency
                        time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        sensors.cleanup()

if __name__ == "__main__":
    read_lm75_temperature()
