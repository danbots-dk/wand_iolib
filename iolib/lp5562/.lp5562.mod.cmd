cmd_/home/peter/lp5562/lp5562.mod := printf '%s\n'   led-class-multicolor.o leds-lp55xx-common.o leds-lp5562.o | awk '!x[$$0]++ { print("/home/peter/lp5562/"$$0) }' > /home/peter/lp5562/lp5562.mod
