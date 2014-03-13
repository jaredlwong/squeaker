Squeaker
========
A very minimal, and very poor website meant to experiment hacking.

Originally conceived for a presentation on cross-site scripting.

The name is a knock-off of Twitter.

The presentation was for 6.UAT at MIT. The fcgi script is meant to host this
website on scripts on athena at MIT.


Dependencies:
-------------
- MarkupSafe-0.19
- flup-1.0.2
- itsdangerous-0.23
- Flask-0.10.1
- Jinja2-2.7.2
- Werkzeug-0.9.4

To install dependencies locally into lib folder run:

    make lib

Running:
-------
To run standalone version (meaning without any other webserver), run:

    ./app.fcgi standalone

To run it as a normal fcgi script under apache, run:

    make

Note, no need to do anything extra beyond pointing apache to this directory.

For MIT Students Looking To Run Python App on Using Scripts
-----------------------------------------------------------
These instructions are meant for MIT affiliates with an athena account who want
to host a python application using scripts.

1. make sure to signup for web scripts at http://scripts.mit.edu/web/
2. self host your dependencies, look at Makefile:lib command to see how I
   populate a standalone lib folder
3. create an fcgi script to run your application, see app.fcgi for an example
   using Flask
4. your fcgi script should use flup, for wsgi server things
4. create a .htaccess file to rewrite all requests to your fcgi script. I put
   my .htaccess file in my Makefile. This is because we have to write the
   variable name of our fcgi script into the .htaccess file. We use a
   variable/random fcgi script name in order to "reboot" the server. Whenever you
   change the fcgi name, a new application starts and the old one is killed.
   This is one of the only systematic ways to reboot fcgi based applications,
   otherwise the webserver may always use the old one and will not update.

I would just copy the Makefile and app.fcgi I have here, and modify them for
your needs.

