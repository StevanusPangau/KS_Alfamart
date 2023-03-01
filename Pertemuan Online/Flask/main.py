from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # return "Hello World"
    param = "Contoh Param"
    param2 = "Param DUa"
    return render_template("index.html", param=param, param2=param2)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
