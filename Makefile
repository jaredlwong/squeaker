fcgi_name:=$(shell echo $$RANDOM)

default:
	cp app.fcgi $(fcgi_name).fcgi
	/bin/sh htaccess_gen.sh $(fcgi_name) > .htaccess
