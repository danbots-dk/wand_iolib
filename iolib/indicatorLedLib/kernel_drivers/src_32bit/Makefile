obj-m += lp5562.o
# List of additional object files that leds-lp5562.o depends on
lp5562-objs := led-class-multicolor.o leds-lp55xx-common.o leds-lp5562.o

KDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean

install:
	$(MAKE) -C $(KDIR) M=$(PWD) modules modules_install

