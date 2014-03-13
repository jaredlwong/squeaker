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
