#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ "$ARCH" = "aarch64" ]; then
    echo "64-bit system detected"
    sudo cp $SCRIPT_DIR/binary/v0.6/cap1293.dtbo /boot/overlays/
    sudo cp $SCRIPT_DIR/binary/v0.6/cap12xx.ko.xz /lib/modules/$(uname -r)/kernel/drivers/input/keyboard
else
    echo "32-bit system detected"
    sudo cp $SCRIPT_DIR/binary/v0.5/cap1293.dtbo /boot/overlays/
    sudo cp $SCRIPT_DIR/binary/v0.5/cap12xx.ko.xz /lib/modules/$(uname -r)/kernel/drivers/input/keyboard
fi


