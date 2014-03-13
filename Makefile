fcgi_name:=$(shell echo $$RANDOM)
define HTACCESS
<IfModule mod_fcgid.c>
   AddHandler fcgid-script .fcgi
   <Files ~ (\.fcgi)>
       SetHandler fcgid-script
       Options +FollowSymLinks +ExecCGI
   </Files>
</IfModule>

<IfModule mod_rewrite.c>
   Options +FollowSymlinks
   RewriteEngine On
   RewriteBase /
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteRule ^(.*)$$ $(fcgi_name).fcgi/$$1 [QSA,L]
</IfModule>
endef
export HTACCESS

default:
	cp app.fcgi $(fcgi_name).fcgi
	echo "$$HTACCESS" > .htaccess

lib:
	mkdir -p lib
	wget -P lib https://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-0.19.tar.gz
	wget -P lib https://pypi.python.org/packages/source/f/flup/flup-1.0.2.tar.gz
	wget -P lib https://pypi.python.org/packages/source/i/itsdangerous/itsdangerous-0.23.tar.gz
	wget -P lib https://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz
	wget -P lib https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.7.2.tar.gz
	wget -P lib https://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-0.9.4.tar.gz
	tar -xzf MarkupSafe-0.19.tar.gz
	tar -xzf flup-1.0.2.tar.gz
	tar -xzf itsdangerous-0.23.tar.gz
	tar -xzf Flask-0.10.1.tar.gz
	tar -xzf Jinja2-2.7.2.tar.gz
	tar -xzf Werkzeug-0.9.4.tar.gz
	rm MarkupSafe-0.19.tar.gz
	rm flup-1.0.2.tar.gz
	rm itsdangerous-0.23.tar.gz
	rm Flask-0.10.1.tar.gz
	rm Jinja2-2.7.2.tar.gz
	rm Werkzeug-0.9.4.tar.gz

clean:
	rm -f .htaccess
	rm -f `find . -name "*fcgi" | grep -v app.fcgi`
