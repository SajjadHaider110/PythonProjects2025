from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///mydb.db' 
db =SQLAlchemy(app)


class User(db.Model): 
    id= db.Column (db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    fname = db.Column(db.String(120), unique=True, nullable=False)
    lname = db.Column(db.String(120), unique=True, nullable=False)
    pswd = db.Column(db.String(120), unique=True, nullable=False)
    
    def _repr_(self): 
        return '<User %r>' % self.username

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
   return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)