# Driver documentation
A change
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
[Example use of buttons](./iolib/buttonLib/README.md)

### EepromLib
[Eeprom docs](./iolib/eepromLib/README.md)



