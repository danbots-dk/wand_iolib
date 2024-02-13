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


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0xf425bc, "i2c_register_driver" },
	{ 0xdef52f47, "regmap_update_bits_base" },
	{ 0xff0cc455, "i2c_del_driver" },
	{ 0x3c672de1, "regmap_read" },
	{ 0x85f7adad, "input_event" },
	{ 0x3ea1b6e4, "__stack_chk_fail" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x92997ed8, "_printk" },
	{ 0xfb0d6cf2, "_dev_err" },
	{ 0xdc71bb31, "devm_kmalloc" },
	{ 0x35deb9b5, "__devm_regmap_init_i2c" },
	{ 0x25aa45a0, "_dev_info" },
	{ 0x3ae659fe, "of_property_read_variable_u32_array" },
	{ 0x24dcae1c, "_dev_warn" },
	{ 0x4ad3aa32, "of_find_property" },
	{ 0xba0ce2e7, "regmap_write" },
	{ 0x8aaf7d46, "of_property_read_u32_index" },
	{ 0xa3ed8c8e, "devm_input_allocate_device" },
	{ 0x96d5e0ab, "of_get_next_child" },
	{ 0xe2f55851, "of_get_property" },
	{ 0x166be30a, "of_node_put" },
	{ 0x72c19167, "devm_led_classdev_register_ext" },
	{ 0x952dfa11, "input_register_device" },
	{ 0x863e6863, "devm_request_threaded_irq" },
	{ 0x78a319e7, "module_layout" },
};

MODULE_INFO(depends, "regmap-i2c");

MODULE_ALIAS("i2c:cap1106");
MODULE_ALIAS("i2c:cap1126");
MODULE_ALIAS("i2c:cap1188");
MODULE_ALIAS("i2c:cap1203");
MODULE_ALIAS("i2c:cap1206");
MODULE_ALIAS("i2c:cap1293");
MODULE_ALIAS("i2c:cap1298");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1106");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1106C*");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1126");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1126C*");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1188");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1188C*");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1203");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1203C*");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1206");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1206C*");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1293");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1293C*");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1298");
MODULE_ALIAS("of:N*T*Cmicrochip,cap1298C*");

MODULE_INFO(srcversion, "C137A94490CD7F5FB512E79");
