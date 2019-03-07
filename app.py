from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/registration')
def registration_page():
    return render_template('registration.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
