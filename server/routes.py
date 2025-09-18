from flask import render_template,request
from model import Vendor, Customer

def register_routes(app,db):

    @app.route('/',methods = ['GET','POST'])
    def index():
        return render_template('index.html')