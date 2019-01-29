import csv
import database_common

fieldnames_question = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
fieldnames_answer = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


@database_common.connection_handler
def delete_answers_by_question_id(cursor, id):
    cursor.execute("""
                    delete from answer
                    where  question_id = %s;  
                    """, id)

@database_common.connection_handler
def delete_question_by_question_id(cursor, id):
    cursor.execute("""
                    delete from question
                    where  id = %s;  
                    """, id)

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


@database_common.connection_handler
def add_question(cursor, submission_time, view_number, vote_number, title, message, image):
    cursor.execute("""
                    insert into question (submission_time, view_number, vote_number, title, message, image)
                    values (%s, %s, %s, %s, %s, %s)
                    """, (submission_time, view_number, vote_number, title, message, image))



