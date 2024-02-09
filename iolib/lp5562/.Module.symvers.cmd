cmd_/home/peter/lp5562/Module.symvers :=  sed 's/ko$$/o/'  /home/peter/lp5562/modules.order | scripts/mod/modpost -m -a    -o /home/peter/lp5562/Module.symvers -e -i Module.symvers -T - 
