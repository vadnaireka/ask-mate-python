from flask import Flask, render_template, redirect, request, session, url_for, send_from_directory
import csv
import time
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = '/UPLOAD_FOLDER'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def route_list():
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = reversed(list(data_file))
    return render_template('list.html', data=data)


@app.route('/question/<id>', methods=['GET', 'POST'])
def route_question(id=None, story=None):
    if request.method == 'POST':
        with open ('sample_data/answer.csv', 'r') as file:
            data_file = csv.DictReader(file)
            all_answers = list(data_file)
            answer_ids = []
            for line in all_answers:
                answer_ids.append(line['id'])
        answer_id = int(answer_ids[-1]) +1
        submission_time = time.time()
        vote_number=0
        question_id= id
        message = request.form['message']
        image = request.form['message']
        fieldnames = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
        with open('sample_data/answer.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'id': answer_id, 'submission_time': submission_time, 'vote_number': vote_number, 'question_id':question_id,
                             'message': message, 'image': image})
    with open('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
        for line in data:
            if line['id'] == str(id):
                story = line
    with open('sample_data/answer.csv', 'r') as file:
        answer_file = csv.DictReader(file)
        story_answer = list(answer_file)
    return render_template('question.html', story=story, story_answer=story_answer)


@app.route('/question/<id>', methods=['GET', 'POST'])
def pic_to_question():
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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


@app.route('/add-question')
def check_allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        image = request.form['image']
        fieldnames = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
        with open('sample_data/question.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'id': id, 'submission_time': submission_time, 'view_number': view_number, 'vote_number': vote_number,
                         'title': title, 'message': message, 'image': image})


@app.route('/add-question', methods=['POST'])
def add_image():
    image = request.files['image']
    if image and check_allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('route_list', filename=filename))


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
