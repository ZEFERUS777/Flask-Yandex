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


@app.route('/astronaut_selection')
def astronaut_selection():
    with open('index.htm.html', 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/choice/<surname>')
def choice(surname):
    return f'''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Surname</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 20px;
                margin: 20px;
            }}

            .str1 {{
                background-color: rgba(0, 255, 0, 0.1);
                padding: 10px;
            }}
            .str2 {{
                background-color: rgba(1, 1, 1, 0.1);
                padding: 10px;
            }}
            .str3 {{
                background-color: rgba(214, 227, 100, 0.2);
                padding: 10px;
            }}
            .str4 {{
                background-color: rgba(255, 149, 125, 0.7);
                padding: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>Моё предложение: {surname}</h1>
        <h2>Эта планета близко к Земле</h2>
        <p class="str1">На ней много необходимых ресурсов;</p>
        <p class="str2">На ней есть вода и атмосфера;</p>
        <p class="str3">На ней есть небольшое магнитное поле;</p>
        <p class="str4">Наконец, она просто красива!</p>
    </body>
</html>'''


if __name__ == '__main__':
    app.run(
        port=8080,
        host='127.0.0.1',
        debug=True
    )
