from flask import Flask, redirect, url_for, request, render_template
import hashlib
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for("register"))

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
                return "User Already in DB"
        except:
            currDB = {user: passwd}
            pick = open("db_sim.pickle", "wb")
            pickle.dump(currDB, pick)
            pick.close()

        return "Successfully Registered User!"
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run()
