#!/bin/bash

dtc -@ -I dts -O dtb -o cap12xx_pca9542.dtbo cap12xx_pca9542.dts
sudo cp cap12xx_pca9542.dtbo /boot/overlays/

make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
sudo depmod
