from flask import Flask

app = Flask(__name__)


@app.route('/')
def Name_missions():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def get_divisions():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


if __name__ == '__main__':
    app.run(
        port=8080,
        host='127.0.0.1',
        debug=True
    )
