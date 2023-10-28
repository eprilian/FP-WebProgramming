from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login_app():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'user_admin' or request.form['password'] != 'adminpassword':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard.html'))
    return render_template('login.html', error=error)