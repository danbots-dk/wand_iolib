from eeprom import EEPROM

class AT24_EEPROM():
    def __init__(self, i2c_bus, i2c_addr):
        self.eeprom = EEPROM("24c512", i2c_bus, i2c_addr)

    def write_parameter(self, parameter_name, value, offset):
        # Pad with blank spaces if the length is less than 15
        padded_value = value.ljust(15)
        return self.eeprom.write(padded_value.encode(), offset)

    def read_parameter(self, parameter_name, size, offset):
        return self.eeprom.read(size, offset).decode('utf-8', errors='ignore')

    def write_flash_date(self, flash_date):
        return self.write_parameter('flash_date', flash_date, 0)

    def read_flash_date(self, size=15):
        return self.read_parameter('flash_date', size, 0)

    def write_software_version(self, software_version):
        return self.write_parameter('software_version', software_version, 20)

    def read_software_version(self, size=15):
        return self.read_parameter('software_version', size, 20)

    def write_hardware_version(self, hardware_version):
        return self.write_parameter('hardware_version', hardware_version, 40)

    def read_hardware_version(self, size=15):
        return self.read_parameter('hardware_version', size, 40)

    def write_assembly_date(self, assembly_date):
        return self.write_parameter('assembly_date', assembly_date, 60)

    def read_assembly_date(self, size=15):
        return self.read_parameter('assembly_date', size, 60)

    def write_unique_id(self, unique_id):
        return self.write_parameter('unique_id', unique_id, 80)

    def read_unique_id(self, size=15):
        return self.read_parameter('unique_id', size, 80)

    def read_all_parameters(self, size=15):
        return {
            'flash_date': self.read_flash_date(size),
            'software_version': self.read_software_version(size),
            'hardware_version': self.read_hardware_version(size),
            'assembly_date': self.read_assembly_date(size),
            'unique_id': self.read_unique_id(size)
        }

# Example Usage:
try:
    eeprom = AT24_EEPROM(1, 0x50)

    # Write parameters
    eeprom.write_flash_date("2023-11-21")
    eeprom.write_software_version("v1.0.0")
    eeprom.write_hardware_version("HW-123")
    eeprom.write_assembly_date("2023-11-20")
    eeprom.write_unique_id("ABC123")

    # Read all parameters
    parameters = eeprom.read_all_parameters()
    print("Parameters:", parameters)

finally:
    pass
