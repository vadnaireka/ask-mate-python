from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add-question')
def add_questuion():
    return render_template('add_question.html')

if __name__ == '__main__':
    app.run()
