from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form["username"] != 'admin' or request.form["password"] != 'admin':
            error = "Invalid Credential, please try again"
        else:
            return redirect(url_for('home'))
    return render_template("login.html", error=error)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
