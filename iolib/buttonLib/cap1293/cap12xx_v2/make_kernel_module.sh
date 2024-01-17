#!/bin/bash

dtc -@ -I dts -O dtb -o cap12xx.dtbo cap12xx.dts
sudo cp cap12xx.dtbo /boot/overlays/

make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
sudo cp cap12xx.ko  /lib/modules/6.1.21-v7l+/kernel/drivers/input/keyboard/
sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
sudo depmod
