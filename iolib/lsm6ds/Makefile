obj-m += st_lsm6dsx.o
obj-m += st_lsm6dsx_i2c.o
# List of additional object files that leds-lp5562.o depends on
# SPDX-License-Identifier: GPL-2.0-only
st_lsm6dsx-y := st_lsm6dsx_core.o st_lsm6dsx_buffer.o \
		st_lsm6dsx_shub.o




KDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean

install:
	$(MAKE) -C $(KDIR) M=$(PWD) modules modules_install

