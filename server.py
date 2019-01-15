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


@app.route('/question/<id>', methods=['GET', 'POST'])
def route_question(id=None, story=None):
    if request.method == 'GET':
        with open('sample_data/question.csv', 'r') as file:
            data_file = csv.DictReader(file)
            data = list(data_file)
            for line in data:
                if line['id'] == str(id):
                    story = line
        with open ('sample_data/answer.csv', 'r') as file:
            answer_file = csv.DictReader(file)
            story_answer = list(answer_file)
    if request.method == 'POST':
        with open ('sample_data/answer.csv', 'r') as file:
    return render_template('question.html', story=story, story_answer=story_answer)


@app.route("/question/<id>/new-answer")
def new_answer(id=id):
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
        for line in data:
            if line['id'] == id:
                story = line
    return render_template('new_answer.html', story=story)

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
