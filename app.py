from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
from main import start_watching


app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute-python-function')
def execute_python_function():
    # 파이썬 함수 실행 코드 작성
    response = start_watching()
    return jsonify(response)

# @app.route("/hello")
# def hello_flask():
#     return "<h1>Hello Flash!</h1>"


# @app.route("/first")
# def hello_first():
#     return "<h3>Hello First</h3>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
