import database_common

fieldnames_question = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
fieldnames_answer = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


@database_common.connection_handler
def new_answer(cursor, id):
    cursor.execute("""
                   SELECT title, message FROM question
                   WHERE id=;
                    """,
                   )
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def delete_allcomments_by_question_id(cursor, id):
    cursor.execute("""
                    delete from comment
                    where question_id = %(id)s
                    """, {'id': id})
    delete_answers_by_question_id(id)


@database_common.connection_handler
def delete_answers_by_question_id(cursor, id):
    cursor.execute("""
                    delete from answer
                    where question_id = %(id)s
                    """, {'id': id})


@database_common.connection_handler
def delete_all_comments_by_question_id(cursor, id):
    cursor.execute("""
                    delete from comment
                    where question_id = %(id)s;
                    """, {'id': id})


@database_common.connection_handler
def delete_answer_by_answer_id_from_comments(cursor, id):
    cursor.execute("""
                    delete from comment
                    where  answer_id = %(id)s;  
                    """, {'id': id})


@database_common.connection_handler
def delete_answer_by_answer_id(cursor, id):
    cursor.execute("""
                    delete from answer
                    where  id = %(id)s;  
                    """, {'id': id})


@database_common.connection_handler
def delete_comment_by_question_id(cursor, id):
    cursor.execute("""
                    delete from comment
                    where id = %(id)s
                    """, {'id': id})\


@database_common.connection_handler
def delete_question_tag_by_question_id(cursor, id):
    cursor.execute("""
                    delete from question_tag
                    where question_id = %(id)s
                    """, {'id': id})


@database_common.connection_handler
def delete_question_by_question_id(cursor, id):
    cursor.execute("""
                    delete from question
                    where id = %(id)s
                    """, {'id': id})


@database_common.connection_handler
def list_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question
                    order by submission_time desc 
                    """)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def list_five_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question
                    order by submission_time desc 
                    LIMIT 5
                    """)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def sort_questions(cursor, column, order):
    cursor.execute("""
                    SELECT * FROM question
                    order by %(column)s %(order)s
                    """, {'column': column, 'order': order})
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def display_question(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    where id = %(id)s
                    """, {'id': id})
    question_data = cursor.fetchall()
    return question_data


@database_common.connection_handler
def display_comment(cursor, id):
    cursor.execute("""
                    SELECT * FROM comment
                    where question_id = %s
                    """, id)
    comment_data = cursor.fetchall()
    return comment_data


@database_common.connection_handler
def display_comment_for_answer(cursor):
    cursor.execute("""
                    SELECT * FROM comment
                    where answer_id is not null
                    """)
    comment_data = cursor.fetchall()
    return comment_data


@database_common.connection_handler
def display_comment_for_question(cursor, id):
    cursor.execute("""
                    SELECT * FROM comment
                    where question_id = %(id)s
                    """, {'id': id})
    comment_data = cursor.fetchall()
    return comment_data


@database_common.connection_handler
def display_answer(cursor, id):
    cursor.execute("""
                    SELECT * FROM answer
                    where question_id = %(id)s
                    """, {'id': id})
    answer_data = cursor.fetchall()
    return answer_data


@database_common.connection_handler
def display_answer_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM answer
                    where id = %(id)s
                    """, {'id': id})
    answer_data = cursor.fetchall()
    return answer_data


@database_common.connection_handler
def add_question(cursor, submission_time, view_number, vote_number, title, message, image):
    cursor.execute("""
                    insert into question (submission_time, view_number, vote_number, title, message, image)
                    values (%s, %s, %s, %s, %s, %s)
                    """, (submission_time, view_number, vote_number, title, message, image))


@database_common.connection_handler
def add_answer(cursor, submission_time, vote_number, question_id, message, image):
    cursor.execute("""
                    insert into answer (submission_time, vote_number, question_id, message, image)
                    values (%s, %s, %s, %s, %s)
                    """, (submission_time, vote_number, question_id, message, image))


@database_common.connection_handler
def add_comment_to_question(cursor, question_id, message, submission_time, edited_count):
    cursor.execute("""
                    insert into comment (question_id, message, submission_time, edited_count)
                    values (%s, %s, %s, %s)
                    """, (question_id, message, submission_time, edited_count))


@database_common.connection_handler
def add_comment_to_answer(cursor, answer_id, message, submission_time, edited_count):
    cursor.execute("""
                    insert into comment (answer_id, message, submission_time, edited_count)
                    values (%s, %s, %s, %s)
                    """, (answer_id, message, submission_time, edited_count))


@database_common.connection_handler
def search_question(cursor, search):
    cursor.execute("""
                    SELECT * FROM question
                    where title like %(search_phrase)s or message like %(search_phrase)s
                    """, {'search_phrase': search})
    search_data = cursor.fetchall()
    return search_data


@database_common.connection_handler
def search_answer(cursor, search):
    cursor.execute("""
                    SELECT * FROM answer
                    where message like %(search_phrase)s
                    """, {'search_phrase': search})
    search_data = cursor.fetchall()
    return search_data


@database_common.connection_handler
def delete_comment_from_database(cursor, id):
    cursor.execute("""
                    delete from comment
                    where  id = %(id)s
                    """, {'id': id})


@database_common.connection_handler
def delete_comment_by_answer_id(cursor, answer_id):
    cursor.execute("""
                    delete from comment
                    where  answer_id = %(answer_id)s
                    """, {'answer_id': answer_id})


@database_common.connection_handler
def get_comments_by_question_id(cursor, question_id):
    cursor.execute("""
                    select answer_id from comment
                    where  id = %(question_id)s
                    """, {'question_id': question_id})
    answer_ids = cursor.fetchall()
    return answer_ids



@database_common.connection_handler
def update_answer(cursor, answer_id, updated_message, updated_image):
    cursor.execute("""
                    UPDATE answer
                    SET message = %s, image = %s
                    WHERE id = %s
                    """, (updated_message, updated_image, answer_id));


@database_common.connection_handler
def up_view_number(cursor, id):
    cursor.execute("""
                    UPDATE question
                    SET view_number = view_number + 1
                    WHERE id = %(id)s
                    """, {'id': id});




@database_common.connection_handler
def get_comment_before_edit(cursor, id):
    cursor.execute("""
                    SELECT * FROM comment
                    where id = %(id)s
                    """, {'id': id})
    comment = cursor.fetchall()
    return comment


@database_common.connection_handler
def update_comment(cursor, comment_id, updated_message, submission_time):
    cursor.execute("""
                    UPDATE comment
                    SET message = %s, submission_time=%s, edited_count = (edited_count+1)
                    WHERE id = %s
                    """, (updated_message, submission_time, comment_id))
