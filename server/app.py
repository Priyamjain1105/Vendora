from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()
#database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder = 'templates')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://avnadmin:{os.getenv("DB_PASSWORD")}@mysql-3b0838a6-priyamjainsocial-b642.i.aivencloud.com:27509/defaultdb'
    #basedir = os.path.abspath(os.path.dirname(__file__))
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'vendor.db') # This will create a file named mylife.db in your project directory
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning
    db.init_app(app)

    #import later open
    from routes import register_routes
    register_routes(app,db)

    migrate = Migrate(app,db)
    return app