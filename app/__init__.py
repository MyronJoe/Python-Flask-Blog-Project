import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '3c33b8874083c78b15cf465c32973cad'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '*******@gmail.com' #add yours, already configured
app.config['MAIL_PASSWORD'] = '000000' #add yours, already configured
mail = Mail(app)
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER1')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')


from app import routes
