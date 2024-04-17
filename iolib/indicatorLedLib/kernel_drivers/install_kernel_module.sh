#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ "$ARCH" = "aarch64" ]; then
    echo "64-bit system detected"
    sudo cp $SCRIPT_DIR/binary/v0.6/leds-lp5562.dtbo /boot/overlays/
    sudo cp $SCRIPT_DIR/binary/v0.6/leds-lp5562_local.dtbo /boot/overlays/
    sudo cp $SCRIPT_DIR/binary/v0.6/lp5562.ko.xz /lib/modules/$(uname -r)/kernel/drivers/leds
else
    echo "32-bit system detected"
    sudo cp $SCRIPT_DIR/binary/v0.5/leds-lp5562.dtbo /boot/overlays/
    sudo cp $SCRIPT_DIR/binary/v0.5/leds-lp5562_local.dtbo /boot/overlays/
    sudo cp $SCRIPT_DIR/binary/v0.5/lp5562.ko.xz /lib/modules/$(uname -r)/kernel/drivers/leds
fi


