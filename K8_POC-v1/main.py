from flask import render_template , url_for, redirect, session
from flask import Flask, request

app = Flask("__name__")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return "USER HAS BEEN LOGGED OUT OR NEVER LOGGED IN"

@app.route('/favorite')
def favorite():
    if session['Anime'] == "Naruto":
        return render_template('Anime1.html')
    elif session['Anime'] == "DeathNote":
        return render_template('Anime2.html')
    elif session['Anime'] == "TokyoGhoul":
        return render_template('Anime3.html')



@app.route('/select',methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        session['Anime'] = request.form['Anime']
        return redirect(url_for('favorite'))

    return render_template("select.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if (session['username'] != "" and session['password'] != ""):
            return redirect(url_for('select'))
        else:
            return render_template("form.html")
    return render_template("form.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if "__name__" == "main":
    app.run()

