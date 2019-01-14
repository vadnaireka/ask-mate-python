from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_list():
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
    return render_template('list.html', data=data)



@app.route('/add-question')
def add_questuion():
    return render_template('add_question.html')

if __name__ == '__main__':
    app.run()
