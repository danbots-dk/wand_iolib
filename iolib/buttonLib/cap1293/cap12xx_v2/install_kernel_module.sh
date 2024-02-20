#!/bin/bash

dtc -@ -I dts -O dtb -o /usr/local/lib/wand/iolib/buttonLib/cap1293/cap12xx_v2/cap1293.dtbo /usr/local/lib/wand/iolib/buttonLib/cap1293/cap12xx_v2/cap1293.dts
sudo cp /usr/local/lib/wand/iolib/buttonLib/cap1293/cap12xx_v2/cap1293.dtbo /boot/overlays/


cd /usr/local/lib/wand/iolib/buttonLib/cap1293/cap12xx_v2/ && make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
cd /usr/local/lib/wand/iolib/buttonLib/cap1293/cap12xx_v2/ && sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
cd /usr/local/lib/wand/iolib/buttonLib/cap1293/cap12xx_v2/ && sudo depmod
