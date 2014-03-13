fcgi_name:=$(shell echo $RANDOM)

deploy:
	/bin/sh htaccess_gen.sh $(fcgi_name) > $(fcgi_name).htaccess
	cp app.fcgi $(fcgi_name).fcgi
	rsync $(fcgi_name).htaccess mit:~/web_scripts/.htaccess
	rsync $(fcgi_name).fcgi     mit:~/web_scripts
	
	rsync squeaker.py mit:~/web_scripts
	rsync index.html  mit:~/web_scripts
	rsync -r lib      mit:~/web_scripts
	
	rm $(fcgi_name).htaccess
	rm $(fcgi_name).fcgi
