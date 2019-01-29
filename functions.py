import database_common


@database_common.connection_handler
def new_answer(cursor, id):
    cursor.execute("""
                   SELECT title, message FROM question
                   WHERE id=;
                    """,
                   )
    names = cursor.fetchall()
    return names
