#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

SYMBOL_CRC(devm_led_classdev_multicolor_register_ext, 0x7fffffff, "_gpl");
SYMBOL_CRC(devm_led_classdev_multicolor_unregister, 0x0fcb6f2e, "_gpl");
SYMBOL_CRC(led_classdev_multicolor_register_ext, 0x7fffffff, "_gpl");
SYMBOL_CRC(led_classdev_multicolor_unregister, 0x7fffffff, "_gpl");
SYMBOL_CRC(led_mc_calc_color_components, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_deinit_device, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_init_device, 0x4a42973f, "_gpl");
SYMBOL_CRC(lp55xx_is_extclk_used, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_of_populate_pdata, 0x12f3b4b9, "_gpl");
SYMBOL_CRC(lp55xx_read, 0x55067cc7, "_gpl");
SYMBOL_CRC(lp55xx_register_leds, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_register_sysfs, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_unregister_sysfs, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_update_bits, 0x7fffffff, "_gpl");
SYMBOL_CRC(lp55xx_write, 0x7fffffff, "_gpl");

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xd0e9fb09, "release_firmware" },
	{ 0xdc71bb31, "devm_kmalloc" },
	{ 0x166be30a, "of_node_put" },
	{ 0x2a21fd2e, "gpiod_set_value" },
	{ 0x3ae659fe, "of_property_read_variable_u32_array" },
	{ 0xc358aaf8, "snprintf" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x222e7ce2, "sysfs_streq" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x314b20c8, "scnprintf" },
	{ 0x2cfde9a2, "warn_slowpath_fmt" },
	{ 0x22d16aa2, "led_classdev_unregister" },
	{ 0xc3055d20, "usleep_range_state" },
	{ 0xfdcf4c8e, "devm_gpiod_get_optional" },
	{ 0xbe88eaf6, "of_get_next_available_child" },
	{ 0xfb18204a, "devm_clk_get" },
	{ 0xc38972c, "devres_add" },
	{ 0xe2f55851, "of_get_property" },
	{ 0x668b595, "_kstrtoul" },
	{ 0x7c9a7371, "clk_prepare" },
	{ 0x92997ed8, "_printk" },
	{ 0x3ea1b6e4, "__stack_chk_fail" },
	{ 0x85256c96, "devres_release" },
	{ 0x25aa45a0, "_dev_info" },
	{ 0xf425bc, "i2c_register_driver" },
	{ 0xfb0d6cf2, "_dev_err" },
	{ 0xec7b087b, "request_firmware_nowait" },
	{ 0x828ce6bb, "mutex_lock" },
	{ 0xcd80e6be, "__devres_alloc_node" },
	{ 0xc48deb2b, "of_property_read_string" },
	{ 0xa8012fbd, "sysfs_create_group" },
	{ 0x5cc77c45, "led_colors" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0xeb9fd2fa, "led_classdev_register_ext" },
	{ 0xde4bf88b, "__mutex_init" },
	{ 0x72c19167, "devm_led_classdev_register_ext" },
	{ 0xe707d823, "__aeabi_uidiv" },
	{ 0x1caa81ea, "of_property_read_variable_u8_array" },
	{ 0x141b19f0, "sysfs_remove_group" },
	{ 0x556e4390, "clk_get_rate" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x9618ede0, "mutex_unlock" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
	{ 0xe93e49c3, "devres_free" },
	{ 0xb6e6d99d, "clk_disable" },
	{ 0xc76934bb, "led_set_brightness" },
	{ 0x59367fac, "i2c_smbus_write_byte_data" },
	{ 0xff0cc455, "i2c_del_driver" },
	{ 0xd6e64d2c, "i2c_smbus_read_byte_data" },
	{ 0xe371a760, "gpiod_set_consumer_name" },
	{ 0x1bf11392, "gpiod_direction_output" },
	{ 0x815588a6, "clk_enable" },
	{ 0xb077e70a, "clk_unprepare" },
	{ 0x78a319e7, "module_layout" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("i2c:lp5562");
MODULE_ALIAS("of:N*T*Cti,lp5562");
MODULE_ALIAS("of:N*T*Cti,lp5562C*");

MODULE_INFO(srcversion, "3E50BE0C52B9B8A156D27E8");
