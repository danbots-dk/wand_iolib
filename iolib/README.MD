# Driver documentation

All drivers are implemented using a .deb package. The following will provide detail on installation and on the individual drivers.

## Installation
First compile the package
   
    cd wand_iolib
    make dep-pkg

Then install

    sudo dpkg -i tmp/danbots-wand-iolib-x.deb

This should install all necessary packages with no further configuration.

## Deb package
### preinst
preinstall configures all of the various dtoverlays by scanning /boot/config.txt and injecting the overlay configuration if not already present. It does this at the end under [All].

### postinst
Copies libraries to /usr/local/lib/wand/iolib/ and overlay files from /usr/local/lib/wand/iolib/ to /boot/overlay in order for them to be available in $PATH and /boot/config.txt respectively.

## Libraries
The .deb package is comprised of multiple individual packages and drives.

###	buttonLib
The button library is implemented using kernel drivers. The setting are configured using the .dts overlay file found in iolib/buttonLib/cap1293/cap12xx_v2/cap12xx_pca9542.dts. The following settings can be configured for now:

 - Pin interrupt (configured via /boot/config.txt)
 - sensor-gain (set to 2)
 - keycodes (semi random values for now..)

A to do is to implement a calibration on power-on in the cap1293.c driver.

Once loaded (verified using dmesg), the button input is available via /dev/input/eventX. Consult the button_api_example.py for how to interface with this.

### EepromLib
[Eeprom docs](eepromLib/README.md)
