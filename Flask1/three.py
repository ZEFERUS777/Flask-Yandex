from flask import Flask

app = Flask(__name__)


@app.route('/')
def Name_missions():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def get_divisions():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def promotion():
    return """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Hello World</title>
    </head>
    <body>
    <p>Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!<br>
    </body>
    </html>"""


@app.route('/image_mars')
def mars_vision():
    return """
    <!DOCTYPE html>
    <html>
    <HEAD>
        <meta charset="UTF-8">
        <title>Привет, Марс!</title>
    </HEAD>
    <p>Жди нас, Марс!</p>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROUiiXpSgztvy9YjQVkjcF5u22Aqte6aFLxw&s"
         alt="Mars" width="300" height="300">
    <p>Вот она какая, красная планета</p>
    </html>"""



if __name__ == '__main__':
    app.run(
        port=8080,
        host='127.0.0.1',
        debug=True
    )
