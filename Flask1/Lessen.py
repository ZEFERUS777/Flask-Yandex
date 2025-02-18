from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    with open('dis.html', 'r', encoding='utf-8') as html_file:
        html = html_file.read()

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=5011,
            debug=True)