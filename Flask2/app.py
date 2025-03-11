from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('form.html')


professions = [
    'инженер-исследователь',
    'пилот',
    'строитель',
    'врач',
    'климатолог',
    'специалист по радиационной защите',
    'астрогеолог',
    'метеоролог',
    'киберинженер'
]


@app.route('/list_prof/<list_type>')
def prof(list_type):
    return render_template('profession.html',
                           list_type=list_type,
                           professions=professions)


@app.route('/login')
def login_form():
    return render_template('form.html')


@app.route('/results/<name>/<step>/<balls>')
def results(name, step, balls):
    return render_template('result.html',
                           name=name,
                           step=step,
                           balls=balls)

if __name__ == '__main__':
    app.run(debug=True)
