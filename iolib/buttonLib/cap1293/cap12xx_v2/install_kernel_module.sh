#!/bin/bash

dtc -@ -I dts -O dtb -o cap12xx_pca9542.dtbo cap12xx_pca9542.dts
sudo cp cap12xx_pca9542.dtbo /boot/overlays/

#!/bin/bash

module_file="cap12xx.ko.xz"
destination="/lib/modules/$(uname -r)/kernel/drivers/input/keyboard/"

if [ -e "/lib/modules/$(uname -r)/extra/$module_file" ]; then
    echo "Module file already exists in /lib/modules/$(uname -r)/extra/, make sure to only have on copy of the driver available"
else
    sudo cp "$module_file" "$destination"
    sudo depmod
fi
