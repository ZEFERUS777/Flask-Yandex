from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Колонизация Марса')  # Значение по умолчанию
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run(debug=True,
            host='127.0.0.1',
            port=8080)
