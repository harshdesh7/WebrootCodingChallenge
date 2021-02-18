from flask import Flask, redirect, url_for, request, render_template, session
import os
import pickle

app = Flask(__name__)
app.secret_key = os.urandom(12) #needed for signing session token

@app.route('/')
def index():

    if "username" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = request.form['nm']
        passwd = request.form['pwd']

        #check for if db_sim file is empty - if it is then will do except clause
        try:
            pick_off = open("db_sim.pickle", "rb")
            currDB = pickle.load(pick_off)
            pick_off.close()

            if user not in currDB:
                currDB[user] = passwd
                pick = open("db_sim.pickle", "wb")
                pickle.dump(currDB, pick)
                pick.close()
            else:
                return 'User Already in DB<br><a href="/login">Click here to login again</a>'
        except:
            currDB = {user: passwd}
            pick = open("db_sim.pickle", "wb")
            pickle.dump(currDB, pick)
            pick.close()

        return 'Successfully Registered User!<br><a href="/login">Click here to login</a>'
    else:
        return render_template('register.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        passwd = request.form['pwd']

        #check for if db_sim file is empty - if it is then will do except clause
        try:
            pick_off = open("db_sim.pickle", "rb")
            currDB = pickle.load(pick_off)
            pick_off.close()

            if user not in currDB:
                return 'User Not Found<br><a href="/register">Click here to register the user</a>'
            elif currDB[user] != passwd:
                return 'Wrong Password<br><a href="/login">Click here to login again</a>'
            else:
                session['username'] = user
                return redirect(url_for("home"))
        except:
            return 'User Not Found<br><a href="/register">Click here to register the user</a>'
    else:
        return render_template('login.html')


@app.route('/home', methods = ['POST', 'GET'])
def home():
    if "username" not in session:
        return redirect(url_for("index"))

    if request.method == 'POST':
        session.pop("username")
        return redirect(url_for("index"))
    else:
        return 'Logged in as ' + session["username"] + '<br>' + \
        '<b><form action = "http://localhost:5000/home" method = "post"><p><input type = "submit" value = "Logout" /></p></form></b>'

if __name__ == '__main__':
    app.run()
