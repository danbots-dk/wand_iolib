#!/bin/bash

module_file="lp5562.ko.xz"
destination="/lib/modules/$(uname -r)/kernel/drivers/input/keyboard/"

if [ -e "$destination/$module_file" ]; then
    echo "Module file already exists in $destination, delete before compiling to avoid multiple copies"
else
    # Compile lp5562 driver
    echo ""
    echo "Running make clean"
    make clean

    echo ""
    echo "Running make"
    make

    echo ""
    echo "Running sudo make install"
    sudo make install

    echo ""
    echo "Running sudo depmod"
    sudo depmod


    # Compile and place lp5562 overlay
    echo ""
    echo "Running Compile dts file"
    dtc -@ -I dts -O dtb -o leds-lp5562.dtbo leds-lp5562.dts

    echo ""
    echo "Running cp dtbo file"
    sudo cp leds-lp5562.dtbo /boot/overlays
fi