from flask import Flask, render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.worksheet import Worksheet
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Root
@app.route("/")
def index():
    return render_template("index.html")


#Create a new user
@app.route('/register', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    
    data = {
        "f_name": request.form["f_name"],
        "l_name": request.form["l_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

#Login
@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

#Dashboard
@app.route("/dashboard")
def homepage():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    print(data)
    return render_template('dashboard.html', user=User.get_by_id(data), worksheets_from_db=Worksheet.get_all())

#Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')