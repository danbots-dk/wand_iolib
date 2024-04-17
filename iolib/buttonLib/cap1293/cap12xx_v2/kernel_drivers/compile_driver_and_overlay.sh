#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ARCH=$(uname -m)



cd "$SCRIPT_DIR/src" && make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
cd "$SCRIPT_DIR/src" && sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install

if [ "$ARCH" = "aarch64" ]; then
    echo "64-bit system detected"
    dtc -@ -I dts -O dtb -o "$SCRIPT_DIR/binary/v0.6/cap1293.dtbo" "$SCRIPT_DIR/overlay/cap1293.dts"
    cp /lib/modules/$(uname -r)/updates/cap12xx.ko.xz "$SCRIPT_DIR/binary/v0.6"
else
    echo "32-bit system detected"
    dtc -@ -I dts -O dtb -o "$SCRIPT_DIR/binary/v0.5/cap1293.dtbo" "$SCRIPT_DIR/overlay/cap1293.dts"
    cp /lib/modules/$(uname -r)/extra/cap12xx.ko.xz "$SCRIPT_DIR/binary/v0.5"
fi
 