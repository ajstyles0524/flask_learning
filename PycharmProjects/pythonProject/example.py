from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello World"


@app.route('/home')
def welcome():
    return "Hello Harry"


@app.route('/home/<name>')
def home(name):
    return "hello," + name


@app.route('/home/<int:age>')
def number(age):
    return "Age = %d" % age


""" def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  """


# url_for function


@app.route('/admin')
def admin():
    return 'Hello Admin'


@app.route('/guest/<name_of_guest>')
def guest(name_of_guest):
    return 'Hello %s as Guest' % name_of_guest


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name_of_guest=name))


# POST Method

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


# POST METHOD


@app.route('/login/post', methods=['POST'])
def login_post():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "ayush" and passwrd == "google":
        return "Welcome %s" % uname


# GET METHOD

@app.route('/login/get', methods=['GET'])
def login_get():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    if uname == "ayush" and passwrd == "google":
        return "Welcome %s" % uname


# templates


@app.route('/html')
def message():
    return "<html><body><h1>Hi, welcome to the website</h1></body></html>"


@app.route('/render')
def message_render():
    return render_template('index.html')


# Delimiters


@app.route('/name/<uname>')
def message_name(uname):
    return render_template('jinga1.html', name=uname)


@app.route('/table/<int:num>')
def table(num):
    return render_template('jinga2.html', n=num)


@app.route('/css')
def message_css():
    return render_template('jinga3.html')


# sending form data to template

@app.route('/')
def customer():
    return render_template('customer.html')


@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("result_data.html", result=result)


# flask Cookies (example -1)

@app.route('/cookie')
def cookie():
    res = make_response("<h1>cookie is set</h1>")
    res.set_cookie('foo', 'bar')
    return res


# flask Cookies (example -2)


@app.route('/cookies')
def index():
    return render_template('index1.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['user']

    resp = make_response(render_template('readCookie.html'))
    resp.set_cookie('user', user)
    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('user')
    resp = make_response(render_template('getcookie.html', name=name))
    return resp


# flask Cookies (Example -3)

@app.route('/error')
def error():
    return "<p><strong>Enter correct password</strong></p>"


@app.route('/login_fb')
def login_fb():
    return render_template("login.html")


@app.route('/success_login', methods=['POST'])
def success_fb():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']

    if password == "jtp":
        resp = make_response(render_template('success.html'))
        resp.set_cookie('email', email)
        return resp
    else:
        return redirect(url_for('error'))


@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    resp = make_response(render_template('profile.html', name=email))
    return resp


# flask session (example -1)


app.secret_key = "abc"


@app.route('/session')
def home_session():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['response'] = 'session#1'
    return res


@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response']
        return render_template('getsession.html', name=s)


# flask session (example - 2)

app.secret_key = "ayush"


@app.route('/home/wiki')
def home_wiki():
    return render_template("home.html")


@app.route('/login/wiki')
def login_wiki():
    return render_template("login_home.html")


@app.route('/success/wiki', methods=["POST"])
def success_wiki():
    if request.method == "POST":
        session['email'] = request.form['email']
    return render_template('success.html')


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return render_template('logout.html')
    else:
        return '<p>user already logged out</p>'


@app.route('/profile/wiki')
def profile_wiki():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        return '<p>Please login first</p>'


# file uploading in flask


@app.route('/upload')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success/upload', methods=['POST'])
def success_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("success_upload.html", name=f.filename)


# flask redirect and error (example -1 )


@app.route('/redirect/home')
def home_redirect():
    return render_template("redirect_home.html")


@app.route('/redirect/login')
def login_redirect():
    return render_template("redirect_login.html")


@app.route('/redirect/validate', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'anand':
        return redirect(url_for("success_redirect"))
    # return redirect(url_for("login_redirect"))
    abort(401)


@app.route('/redirect/success')
def success_redirect():
    return "logged in successfully"


# flask flashing

app.secret_key = "abc"


@app.route('/flash/index')
def home_flash():
    return render_template("flash_index.html")


@app.route('/flash/login', methods=["GET", "POST"])
def login_flash():
    error = None
    if request.method == "POST":
        if request.form['pass'] != 'anand':
            error = "invalid password"
        else:
            message = "you are successfuly logged in"
            return render_template('flash_index.html', message = message)
    return render_template('flash_login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
