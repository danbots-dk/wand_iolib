#
# makefile for iolib

VERSION=1.0.7-15
PKG_NAME=danbots-wand-iolib-$(VERSION)
USR_LOCAL=/usr/local/lib/wand

help:
	echo "make install\tto install lib in /usr/local"

requirements:
	pip install -r requirements.txt

inst_iolib:
	mkdir -p $(USR_LOCAL)
	cp -r iolib $(USR_LOCAL)

install: inst_iolib

deb-pkg:
	mkdir -p tmp/pkg/usr/local/lib/wand
	cp -r pkg/* tmp/pkg
	cp -r iolib/ tmp/pkg/usr/local/lib/wand/	
	cp -r test/ tmp/pkg/usr/local/lib/wand/
	dpkg-deb --build --root-owner-group -Zxz tmp/pkg tmp/$(PKG_NAME).deb

deb-push:
	rcp tmp/$(PKG_NAME).deb  apt.danbots.com:/var/www/apt/simple/pool/wand/
	rsh apt.danbots.com /var/www/apt/simple/scan

clean:
	rm -rf tmp
