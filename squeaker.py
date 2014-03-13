import random
import hashlib
import collections
import functools
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
from flask import g

###############################################################################
UserInfo = collections.namedtuple('UserInfo', ['usr', 'pwd', 'tok', 'posts'])
users = {}

###############################################################################
def gen_token(pwd):
    hashinput = "%s%.10f" % (pwd, random.random())
    return hashlib.md5(hashinput).hexdigest()

def gen_cookie(ui):
    """Generate a cookie from the UserInfo object."""
    return "%s#%s" % (ui.usr, ui.tok)

def register_usr(usr, pwd):
    """Register user in users. Return Cookie. Return None if error."""
    # fail if usr or pwd is empty
    if not usr or not pwd:
        return None
    # fail if usr exists
    if usr in users:
        return None
    users[usr] = UserInfo(usr, pwd, gen_token(pwd), [])
    return gen_cookie(users[usr])

def login_usr(usr, pwd):
    """Login user in users. Return Cookie. Return None if error."""
    if not usr or not pwd:
        return None
    if usr not in users:
        return None
    # if pwds don't match, fail
    if users[usr].pwd != pwd:
        return None
    users[usr] = UserInfo(usr, pwd, gen_token(pwd), users[usr].posts)
    return gen_cookie(users[usr])

def check_cookie(cookie):
    """Return UserInfo if cookie is valid, None otherwise"""
    # fail if empty cookie
    if not cookie:
        return None
    (usr, tok) = cookie.rsplit("#", 1)
    if usr not in users:
        return None
    if users[usr].tok == tok:
        return users[usr]

###############################################################################
def login():
    """Attempt to log user in by setting cookie."""
    response = redirect(url_for('index'))
    cookie = None
    username = request.form.get('login_username')
    password = request.form.get('login_password')

    if username and password:
        if 'submit_registration' in request.form:
            cookie = register_usr(username, password)
        elif 'submit_login' in request.form:
            cookie = login_usr(username, password)
        if cookie:
            # Be careful not to include semicolons in cookie value; see
            # https://github.com/mitsuhiko/werkzeug/issues/226 for more details.
            response.set_cookie('cookie', cookie)

    return response

def logout():
    """Log user out by setting cookie to nothing."""
    response = redirect(url_for('index'))
    response.set_cookie('cookie', '')
    return response

def index():
    ui = check_cookie(request.cookies.get("cookie"))
    if not ui:
        return render_template('squeaker.html', login=True)
    posts = []
    for usr, ui in users.iteritems():
        for post in ui.posts:
            posts.append((usr, post))
    return render_template('squeaker.html', login=False, posts=posts)

def post():
    """Make a post by adding post to user info"""
    ui = check_cookie(request.cookies.get("cookie"))
    if ui is not None:
        ui.posts.append(request.form.get('squeak'))
    return redirect(url_for('index'))

###############################################################################
app = Flask(__name__, template_folder='.')
app.debug = True
app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/login', 'login', login, methods=['POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['GET'])
app.add_url_rule('/post', 'post', post, methods=['POST'])

@app.after_request
def disable_xss_protection(response):
    response.headers.add('X-XSS-PROTECTION', '0')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')

