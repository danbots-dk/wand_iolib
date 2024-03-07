#!/bin/bash

dtc -@ -I dts -O dtb -o /usr/local/lib/wand/iolib/lp5562/kernel_drivers/leds-lp5562.dtbo /usr/local/lib/wand/iolib/lp5562/kernel_drivers/leds-lp5562.dts
sudo cp /usr/local/lib/wand/iolib/lp5562/kernel_drivers/leds-lp5562.dtbo /boot/overlays/

cd /usr/local/lib/wand/iolib/lp5562/kernel_drivers/ && make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
cd /usr/local/lib/wand/iolib/lp5562/kernel_drivers/ && sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install

