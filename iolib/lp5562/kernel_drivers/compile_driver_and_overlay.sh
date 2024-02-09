#!/bin/bash

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
