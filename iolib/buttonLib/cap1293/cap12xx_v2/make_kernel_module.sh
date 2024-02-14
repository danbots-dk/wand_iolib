#!/bin/bash

dtc -@ -I dts -O dtb -o cap12xx_pca9542.dtbo cap12xx_pca9542.dts
sudo cp cap12xx_pca9542.dtbo /boot/overlays/

module_file="cap12xx.ko.xz"
destination="/lib/modules/$(uname -r)/kernel/drivers/input/keyboard/"

if [ -e "$destination/$module_file" ]; then
    echo "Module file already exists in $destination, delete before compiling to avoid multiple copies"
else
    make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
    sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
    sudo depmod
fi