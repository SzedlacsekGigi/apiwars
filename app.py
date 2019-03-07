from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    if request.method == 'GET':
        return render_template('registration.html')
    if request.method == 'POST':
        username = request.form['registrationUsername']
        hash = database_common.hash_password(request.form['registrationPassword'])


@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
