from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html',name="home")

@app.route("/about")
def about():
    return render_template('about.html',name="about")

@app.route("/signin")
def signin():
    return render_template('signin.html',name="signin")

@app.route("/signup")
def signup():
    return render_template('signup.html',name="signup")

if __name__=='__main__':
    app.run()