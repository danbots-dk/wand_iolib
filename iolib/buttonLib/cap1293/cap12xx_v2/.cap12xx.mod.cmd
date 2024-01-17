cmd_/home/peter/cap1293/cap12xx_v2/cap12xx.mod := printf '%s\n'   cap12xx.o | awk '!x[$$0]++ { print("/home/peter/cap1293/cap12xx_v2/"$$0) }' > /home/peter/cap1293/cap12xx_v2/cap12xx.mod
