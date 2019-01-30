from flask import Flask, render_template, redirect, request, session, url_for
from datetime import datetime
import functions

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def route_list():
    if request.method == 'POST':
        column = request.form['column']
        order = request.form['order']
        data = functions.sort_questions(column, order)
    if request.method == 'GET':
        data = functions.list_questions()
    return render_template('list.html', data=data)


@app.route('/question/<id>', methods=['GET', 'POST'])
def route_question(id=id, ):
    question = functions.display_question(id)
    answers = functions.display_answer(id)
    question_comments = functions.display_comment_for_question(id)
    answer_comments = functions.display_comment_for_answer()
    return render_template('question.html', question=question, answers=answers, answer_comments=answer_comments,
                           question_comments=question_comments)


@app.route("/question/<id>/new-answer", methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'GET':
        questions = functions.display_question(id)
        question = questions[0]
        return render_template('new_answer.html', question=question)
    if request.method == 'POST':
        submission_time = datetime.now()
        vote_number = 0
        questions = functions.display_question(id)
        question = questions[0]
        question_id = question['id']
        message = request.form['message']
        image = request.form['image']
        functions.add_answer(submission_time, vote_number, question_id, message, image)
        return redirect(url_for('route_question', id=question['id']))


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


@app.route('/question/<question_id>/new_comment/', methods=['GET', 'POST'])
def add_new_comment(question_id):
    questions = functions.display_question(question_id)
    answers = functions.display_answer(question_id)
    if request.method == 'GET':
        return render_template('new_comment.html', questions=questions, answers=answers)
    if request.method == 'POST':
        message = request.form['comment']
        submission_time = datetime.now()
        edited_count = 0
        functions.add_comment_to_question(question_id, message, submission_time, edited_count)
        return redirect(url_for('route_question', id=question_id))


@app.route('/question/<question_id>/<answer_id>/new_comment', methods=['GET', 'POST'])
def add_comment_to_answer(question_id, answer_id):
    questions = functions.display_question(question_id)
    answers = functions.display_answer_by_id(answer_id)
    if request.method == 'GET':
        return render_template('new_comment_to_answer.html', questions=questions, answers=answers)
    if request.method == 'POST':
        message = request.form['comment']
        submission_time = datetime.now()
        edited_count = 0
        functions.add_comment_to_answer(answer_id, message, submission_time, edited_count)
        return redirect(url_for('route_question', id=question_id, answer_id=answer_id))


@app.route('/search', methods=['GET'])
def search_question():
    search_phrase = request.args.get('search_phrase')
    search = ('%' + search_phrase + '%')
    search_data = functions.search_question(search)
    search_answer = functions.search_answer(search)
    return render_template('search.html', data=search_data, answer_data=search_answer)

@app.route('/answer/<answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    if request.method == 'GET':
        answers = functions.display_answer(answer_id)
        answer = answers[0]
        return render_template('edit_answer.html', answer=answer)



if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
