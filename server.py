from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_list():
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
    return render_template('list.html', data=data)



if __name__ == '__main__':
    app.run()
