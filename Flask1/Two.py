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


@app.route('/promotion_image')
def promotion_image():
    return """
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/html" xmlns="http://www.w3.org/1999/html">
    <HEAD>
        <meta charset="UTF-8">
        <title>Привет, Марс!</title>
        <style>
            #String_0 {
                color: red;
            }
            #String_1 {
                background-color: rgba(179, 177, 173, 0.3);
                margin-top: 10px;
            }
            #String_2 {
                background-color: rgba(96, 171, 104, 0.3);
                margin-top: 10px;
            }
            #String_3 {
                background-color: rgba(134, 138, 134, 0.3);
                margin-top: 10px;
            }
            #String_4 {
                background-color: rgba(240, 233, 158, 0.3);
                margin-top: 10px;
            }
            #String_5 {
                background-color: rgba(209, 91, 73, 0.4);
                margin-top: 10px;
            }
        </style>
    </HEAD>
    <p id="String_0">Жди нас, Марс!</p>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROUiiXpSgztvy9YjQVkjcF5u22Aqte6aFLxw&s"
         alt="Mars" width="300" height="300">
    <p id="String_1">Человечество вырастает из детства.</p>
    <p id="String_2">Человечеству мала одна планета.</p>
    <p id="String_3">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p id="String_4">И начнем с Марса!</p>
    <p id="String_5">Присоединяйся!</p>
    </html>"""


if __name__ == '__main__':
    app.run(
        port=8080,
        host='127.0.0.1',
        debug=True
    )
