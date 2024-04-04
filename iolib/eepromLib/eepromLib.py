from eeprom import EEPROM
from typing import Optional, Dict

class AT24_EEPROM:
    def __init__(self, i2c_bus: int, i2c_addr: int):
        """
        Initializes the AT24_EEPROM class.

        Args:
            i2c_bus (int): The I2C bus number.
            i2c_addr (int): The I2C address of the EEPROM.
        """
        self.eeprom = EEPROM("24c512", i2c_bus, i2c_addr)

    def write_parameter(self, parameter_name: str, value: str, offset: int) -> Optional[int]:
        """
        Writes a parameter to the EEPROM.

        Args:
            parameter_name (str): The name of the parameter.
            value (str): The value to write.
            offset (int): The offset in the EEPROM memory.

        Returns:
            Optional[int]: The number of bytes written or None if the write operation fails.
        """
        padded_value = value.ljust(15)
        return self.eeprom.write(padded_value.encode(), offset)

    def read_parameter(self, parameter_name: str, size: int, offset: int) -> str:
        """
        Reads a parameter from the EEPROM.

        Args:
            parameter_name (str): The name of the parameter.
            size (int): The size of the parameter.
            offset (int): The offset in the EEPROM memory.

        Returns:
            str: The read parameter value.
        """
        return self.eeprom.read(size, offset).decode('utf-8', errors='ignore')

    def write_flash_date(self, flash_date: str) -> Optional[int]:
        """
        Writes the flash date to the EEPROM.

        Args:
            flash_date (str): The flash date to write.

        Returns:
            Optional[int]: The number of bytes written or None if the write operation fails.
        """
        return self.write_parameter('flash_date', flash_date, 0)

    def read_flash_date(self, size: int = 15) -> str:
        """
        Reads the flash date from the EEPROM.

        Args:
            size (int): The size of the flash date.

        Returns:
            str: The read flash date.
        """
        return self.read_parameter('flash_date', size, 0)

    def write_software_version(self, software_version: str) -> Optional[int]:
        """
        Writes the software version to the EEPROM.

        Args:
            software_version (str): The software version to write.

        Returns:
            Optional[int]: The number of bytes written or None if the write operation fails.
        """
        return self.write_parameter('software_version', software_version, 20)

    def read_software_version(self, size: int = 15) -> str:
        """
        Reads the software version from the EEPROM.

        Args:
            size (int): The size of the software version.

        Returns:
            str: The read software version.
        """
        return self.read_parameter('software_version', size, 20)

    def write_hardware_version(self, hardware_version: str) -> Optional[int]:
        """
        Writes the hardware version to the EEPROM.

        Args:
            hardware_version (str): The hardware version to write.

        Returns:
            Optional[int]: The number of bytes written or None if the write operation fails.
        """
        return self.write_parameter('hardware_version', hardware_version, 40)

    def read_hardware_version(self, size: int = 15) -> str:
        """
        Reads the hardware version from the EEPROM.

        Args:
            size (int): The size of the hardware version.

        Returns:
            str: The read hardware version.
        """
        return self.read_parameter('hardware_version', size, 40)

    def write_assembly_date(self, assembly_date: str) -> Optional[int]:
        """
        Writes the assembly date to the EEPROM.

        Args:
            assembly_date (str): The assembly date to write.

        Returns:
            Optional[int]: The number of bytes written or None if the write operation fails.
        """
        return self.write_parameter('assembly_date', assembly_date, 60)

    def read_assembly_date(self, size: int = 15) -> str:
        """
        Reads the assembly date from the EEPROM.

        Args:
            size (int): The size of the assembly date.

        Returns:
            str: The read assembly date.
        """
        return self.read_parameter('assembly_date', size, 60)

    def write_unique_id(self, unique_id: str) -> Optional[int]:
        """
        Writes the unique ID to the EEPROM.

        Args:
            unique_id (str): The unique ID to write.

        Returns:
            Optional[int]: The number of bytes written or None if the write operation fails.
        """
        return self.write_parameter('unique_id', unique_id, 80)

    def read_unique_id(self, size: int = 15) -> str:
        """
        Reads the unique ID from the EEPROM.

        Args:
            size (int): The size of the unique ID.

        Returns:
            str: The read unique ID.
        """
        return self.read_parameter('unique_id', size, 80)

    def read_all_parameters(self, size: int = 15) -> Dict[str, str]:
        """
        Reads all parameters from the EEPROM.

        Args:
            size (int): The size of the parameters.

        Returns:
            Dict[str, str]: A dictionary containing parameter names and their respective values.
        """
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
