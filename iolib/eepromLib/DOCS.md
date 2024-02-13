## AT24_EEPROM Class Documentation

This class provides an interface for interacting with an EEPROM (Electrically Erasable Programmable Read-Only Memory) chip of the AT24 series over I2C communication protocol.

### Class: `AT24_EEPROM`

#### Constructor: `__init__(i2c_bus: int, i2c_addr: int)`

Initializes the AT24_EEPROM class.

- `i2c_bus` (int): The I2C bus number.
- `i2c_addr` (int): The I2C address of the EEPROM.

#### Method: `write_parameter(parameter_name: str, value: str, offset: int) -> Optional[int]`

Writes a parameter to the EEPROM.

- `parameter_name` (str): The name of the parameter.
- `value` (str): The value to write.
- `offset` (int): The offset in the EEPROM memory.

Returns:
- `Optional[int]`: The number of bytes written or None if the write operation fails.

#### Method: `read_parameter(parameter_name: str, size: int, offset: int) -> str`

Reads a parameter from the EEPROM.

- `parameter_name` (str): The name of the parameter.
- `size` (int): The size of the parameter.
- `offset` (int): The offset in the EEPROM memory.

Returns:
- `str`: The read parameter value.

#### Method: `write_flash_date(flash_date: str) -> Optional[int]`

Writes the flash date to the EEPROM.

- `flash_date` (str): The flash date to write.

Returns:
- `Optional[int]`: The number of bytes written or None if the write operation fails.

#### Method: `read_flash_date(size: int = 15) -> str`

Reads the flash date from the EEPROM.

- `size` (int): The size of the flash date.

Returns:
- `str`: The read flash date.

#### Method: `write_software_version(software_version: str) -> Optional[int]`

Writes the software version to the EEPROM.

- `software_version` (str): The software version to write.

Returns:
- `Optional[int]`: The number of bytes written or None if the write operation fails.

#### Method: `read_software_version(size: int = 15) -> str`

Reads the software version from the EEPROM.

- `size` (int): The size of the software version.

Returns:
- `str`: The read software version.

#### Method: `write_hardware_version(hardware_version: str) -> Optional[int]`

Writes the hardware version to the EEPROM.

- `hardware_version` (str): The hardware version to write.

Returns:
- `Optional[int]`: The number of bytes written or None if the write operation fails.

#### Method: `read_hardware_version(size: int = 15) -> str`

Reads the hardware version from the EEPROM.

- `size` (int): The size of the hardware version.

Returns:
- `str`: The read hardware version.

#### Method: `write_assembly_date(assembly_date: str) -> Optional[int]`

Writes the assembly date to the EEPROM.

- `assembly_date` (str): The assembly date to write.

Returns:
- `Optional[int]`: The number of bytes written or None if the write operation fails.

#### Method: `read_assembly_date(size: int = 15) -> str`

Reads the assembly date from the EEPROM.

- `size` (int): The size of the assembly date.

Returns:
- `str`: The read assembly date.

#### Method: `write_unique_id(unique_id: str) -> Optional[int]`

Writes the unique ID to the EEPROM.

- `unique_id` (str): The unique ID to write.

Returns:
- `Optional[int]`: The number of bytes written or None if the write operation fails.

#### Method: `read_unique_id(size: int = 15) -> str`

Reads the unique ID from the EEPROM.

- `size` (int): The size of the unique ID.

Returns:
- `str`: The read unique ID.

#### Method: `read_all_parameters(size: int = 15) -> Dict[str, str]`

Reads all parameters from the EEPROM.

- `size` (int): The size of the parameters.

Returns:
- `Dict[str, str]`: A dictionary containing parameter names and their respective values.

### Example Usage:

```python
from eeprom import AT24_EEPROM

try:
    # Initialize EEPROM
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
