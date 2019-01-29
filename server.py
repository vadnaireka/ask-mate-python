from flask import Flask, render_template, redirect, request, session, url_for
import csv
from datetime import datetime
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


@app.route('/question/<id>/delete')
def delete_question(id):
    functions.delete_answers_by_question_id(id)
    functions.delete_question_by_question_id(id)
    return redirect(url_for('route_list'))


@app.route('/add-question', methods=['GET', 'POST'])
def route_save_question():
    if request.method == 'GET':
        return render_template('add_question.html')
    if request.method == 'POST':
        submission_time = datetime.now()
        view_number = 0
        vote_number = 0
        title = request.form['title']
        message = request.form['message']
        image = ''
        functions.add_question(submission_time, view_number, vote_number, title, message, image)
        return redirect(url_for('route_list'))


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
