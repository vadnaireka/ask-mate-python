from flask import Flask, render_template, redirect, request, session, url_for
import csv
import time
import functions

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_list():
    data = functions.list_questions()

    return render_template('list.html', data=data)


@app.route('/question/<id>', methods=['GET', 'POST'])
def route_question(id=id, story=None):
    questions = functions.display_question(id)
    answers = functions.display_answer(id)
    return render_template('question.html', questions=questions, answers=answers)


@app.route("/question/<id>/new-answer")
def new_answer(id=id):
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
        for line in data:
            if line['id'] == id:
                story = line
    return render_template('new_answer.html', story=story)

@app.route('/add-question')
def route_add_question():
    return render_template('add_question.html')


@app.route('/add-question', methods=['GET', 'POST'])
def route_save_question():
    if request.method == 'POST':
        all_id = []
        file = open('sample_data/question.csv')
        csv_file = csv.reader(file)
        for row in csv_file:
            all_id.append(row[0])
        last_id = all_id[-1]
        id = int(last_id) + 1
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
        return redirect(url_for('route_list'))


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
