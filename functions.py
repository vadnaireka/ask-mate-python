import csv
import database_common

fieldnames_question = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
fieldnames_answer = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

def delete_question_and_answers_by_user_id(id):
    #deleting questions by id
    with open('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
        new_data = []
        for line in data:
            if line['id'] != str(id):
                new_data.append(line)
    with open('sample_data/question.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_question)
        writer.writeheader()
        writer.writerows(new_data)
    with open ('sample_data/question.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = reversed(list(data_file))
    # deleting answers by id
    with open('sample_data/answer.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
        new_data = []
        for line in data:
            if line['id'] != str(id):
                new_data.append(line)
    with open('sample_data/answer.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_answer)
        writer.writeheader()
        writer.writerows(new_data)


@database_common.connection_handler
def list_questions(cursor):
    cursor.execute("""
                    SELECT title, id FROM question
                    """)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def display_question(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    where id = %s
                    """, id)
    question_data = cursor.fetchall()
    return question_data


@database_common.connection_handler
def display_answer(cursor, id):
    cursor.execute("""
                    SELECT * FROM answer
                    where question_id = %s
                    """, id)
    answer_data = cursor.fetchall()
    return answer_data
