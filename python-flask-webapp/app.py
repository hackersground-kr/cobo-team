from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
from main import start_watching


app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('//execute-python-function', methods=['GET'])
def run_function():
    # 실행하려는 Python 함수를 호출하고 결과를 반환합니다.
    result = start_watching()
    return result

if __name__ == "__main__":
    app.debug = True

    app.run(host="0.0.0.0", port="8080")

# @app.route('/start', methods=['GET'])
# def run_function():
#     start_watching()
#     return "good"

# @app.route('/execute-python-function')
# def execute_python_function():
#     # 파이썬 함수 실행 코드 작성
#     response = start_watching()
#     return jsonify(response)