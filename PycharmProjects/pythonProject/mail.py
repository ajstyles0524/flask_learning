from flask import *
from flask_mail import Mail, Message

app = Flask(__name__)
#  Configure the Flask Mail.

app.config['MAIL_SERVER'] = 'ajstyles0524.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ajstyles0524@gmail.com'
app.config['MAIL_PASSWORD'] = 'Knoldus@678'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Instantiate the Mail class.

mail = Mail(app)


# Instantiate the Message class with the desired attributes in the function mapped by some URL rule.


@app.route('/')
def index():
    msg = Message('subject', sender='ajstyles0524@gmail.com', recipients=['ajstyles0524@gmail.com'])
    msg.body = 'hi, this is the mail sent by using the flask web application'
    return "Mail Sent, Please check the mail id"


if __name__ == '__main__':
    app.run(debug=True)
