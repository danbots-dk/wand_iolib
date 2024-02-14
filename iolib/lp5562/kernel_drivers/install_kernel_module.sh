#!/bin/bash

module_file="lp5562.ko.xz"
destination="/lib/modules/$(uname -r)/kernel/drivers/input/keyboard/"

if [ -e "/lib/modules/$(uname -r)/extra/$module_file" ]; then
    echo "Module file already exists in /lib/modules/$(uname -r)/extra/, make sure to only have on copy of the driver available"
else
    sudo cp "$module_file" "$destination"
    sudo depmod
fi
