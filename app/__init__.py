from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:English12_@localhost/CompuStore"
app.config['SQLALCHMEY_BINDS'] = {'compustore1': "mysql://root:English12_@localhost/CompuStore1",
                                'compustore2': "mysql://root:English12_@localhost/CompuStore2"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)

#Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views