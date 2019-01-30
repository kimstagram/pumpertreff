from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = "development-key"
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db.init_app(app)
    return app

app = create_app()



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if 'email' in session:
        return redirect(url_for('index'))
    form = SignupForm()

    if request.method == 'POST':
        if form.validate_on_submit:
            newuser = User(form.name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('home'))
        else:
            return render_template("signup.html", form = form)
    elif request.method == 'GET':
        return render_template('signup.html', form = form)

@app.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if 'email' in session:
        return redirect(url_for('index'))
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email = email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
        else:
            return render_template("login.html", form=form)
    elif request.method == "GET":
        return render_template("login.html", form = form)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)