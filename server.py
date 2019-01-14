from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add-question')
def add_questuion():
    return 'You will be able to add questions here'

if __name__ == '__main__':
    app.run()
