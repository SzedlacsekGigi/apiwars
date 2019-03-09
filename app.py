from flask import Flask, render_template, request, redirect, url_for, session
import functions
import database_common

app = Flask(__name__)
app.secret_key = "Lukeiamyourfather"


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registrate_user():
    if request.method == 'GET':
        return render_template('registration.html')
    if request.method == 'POST':
        user_name = request.form['user_name']
        hash = database_common.hash_password(request.form['password'])
        functions.signup_user(user_name, hash)
        return redirect(url_for('homepage'))


@app.route('/login', methods=['GET','POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_data = functions.get_user_data(user_name)
        verification = database_common.verify_password(request.form['password'], user_data['hash'])
        if user_data['user_name'] == user_name and verification == True:
            session['user_name'] = user_name
            session['id'] = user_data['id']
            return redirect(url_for('homepage'))


@app.route('/logout', methods=['GET'])
def logout_user():
    session.pop('user_name', None)
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
