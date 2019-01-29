import csv

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
