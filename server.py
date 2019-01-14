from flask import Flask, render_template, redirect, request, session
import csv
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_list():
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = reversed(list(data_file))
    return render_template('list.html', data=data)



@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        id += 1
        submission_time = time.time()
        view_number = 0
        vote_number = 0
        title = request.form['title']
        message = request.form['message']
        image = ''
        fieldnames = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
        with open('sample_data/question.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'id': id, 'submission_time': submission_time, 'view_number': view_number, 'vote_number': vote_number,
                         'title': title, 'message': message, 'image': image})
    return render_template('add_question.html', )


if __name__ == '__main__':
    app.run()
