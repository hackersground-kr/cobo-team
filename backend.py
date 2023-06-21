from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, static_folder="static")


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/hello")
def hello_flask():
    return "<h1>Hello Flash!</h1>"


@app.route("/first")
def hello_first():
    return "<h3>Hello First</h3>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
