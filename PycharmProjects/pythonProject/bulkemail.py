from flask import *
from flask_mail import *

app = Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'ajstyles0524@gmail.com'
app.config['MAIL_PASSWORD'] = 'Knoldus@678'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

users = [{'name': 'john', 'email': 'john@gmail.com'}, {'name': 'Ayush', 'email': 'ayush@javatpoint.com'},
         {'name': 'david', 'email': 'david@gmail.com'}]

mail = Mail(app)


@app.route("/")
def index():
    with mail.connect() as con:
        for user in users:
            message = "hello %s" % user['name']
            msgs = Message(recipients=[user['email']], body=message, subject='hello', sender='david@gmail.com')
            con.send(msgs)
    return "Sent"


if __name__ == "__main__":
    app.run(debug=True)
