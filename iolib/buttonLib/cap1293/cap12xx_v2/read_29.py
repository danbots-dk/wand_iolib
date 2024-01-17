import smbus

# Define the I2C device address
device_address = 0x28

# Define the register address to read
register_address = 29

# Create an I2C bus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi 2 or 3, use 0 for Raspberry Pi 1

# Read a byte from the specified register
data = bus.read_byte_data(device_address, register_address)

# Print the result
print(f"Value read from register {register_address} on I2C device {hex(device_address)}: {hex(data)}")

# Close the I2C bus
bus.close()
