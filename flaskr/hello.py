from flask import Flask, render_template
app = Flask(__name__)


@app.route('/login/')
def log_in():
    return render_template('login.html')


@app.route('/success/')
def login_success():
    return render_template('success.html')

