#!/bin/bash

dtc -@ -I dts -O dtb -o cap1293_0.dtbo cap1293_0.dts
sudo cp cap1293_0.dtbo /boot/overlays/

dtc -@ -I dts -O dtb -o cap1293_1.dtbo cap1293_1.dts
sudo cp cap1293_1.dtbo /boot/overlays/

make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
sudo depmod
