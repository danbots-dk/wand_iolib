#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ARCH=$(uname -m)





if [ "$ARCH" = "aarch64" ]; then
    echo "64-bit system detected"
    cd "$SCRIPT_DIR/src_64bit" && make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
    cd "$SCRIPT_DIR/src_64bit" && sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
    dtc -@ -I dts -O dtb -o "$SCRIPT_DIR/binary/v0.6/leds-lp5562.dtbo" "$SCRIPT_DIR/overlay/leds-lp5562.dts"
    cp $SCRIPT_DIR/binary/v0.6/leds-lp5562.dtbo /boot/overlays/
    cp /lib/modules/$(uname -r)/updates/lp5562.ko.xz "$SCRIPT_DIR/binary/v0.6"
else
    echo "32-bit system detected"
    cd "$SCRIPT_DIR/src_32bit" && make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
    cd "$SCRIPT_DIR/src_32bit" && sudo make -C /lib/modules/$(uname -r)/build M=$(pwd) modules_install
    dtc -@ -I dts -O dtb -o "$SCRIPT_DIR/binary/v0.5/leds-lp5562.dtbo" "$SCRIPT_DIR/overlay/leds-lp5562.dts"
    cp $SCRIPT_DIR/binary/v0.6/leds-lp5562.dtbo /boot/overlays/
    cp /lib/modules/$(uname -r)/extra/lp5562.ko.xz "$SCRIPT_DIR/binary/v0.5"
fi
