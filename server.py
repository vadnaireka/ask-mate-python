from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def route_index():
    fieldnames = ['ID', 'Story Title', 'User Story', 'Acceptance criteria', 'Business value', 'Estimation', 'Status']
    if request.method == 'POST':
        if request.form['id']:
            with open('data.csv', 'r+') as file:
                data_file = csv.DictReader(file)
                data = list(data_file)
                for line in data:
                    if line['ID'] == str(request.form['id']):
                        line['Story Title'] = request.form['title']
                        line['User Story'] = request.form['story']
                        line['Acceptance criteria'] = request.form['criteria']
                        line['Business value'] = request.form['Business_Value']
                        line['Estimation'] = request.form['Estimation']
                        line['Status'] = request.form['Status']
            with open('data.csv', 'w') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
            with open('data.csv', 'a') as file:
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                for line in data:
                    writer.writerow({'ID': line['ID'], 'Story Title': line['Story Title'], 'User Story': line['User Story'],
                                                'Acceptance criteria': line['Acceptance criteria'], 'Business value': line['Business value'],
                                                'Estimation': line['Estimation'], 'Status': line['Status']})
        if request.form['id'] == 'new':
            with open ('id.txt', 'r') as id_file:
                id_from_file = id_file.read()
                new_id = str(int(id_from_file) + 1)
            with open ('id.txt', 'w') as id_file:
                id_file.write(new_id)
            id = id_from_file
            title = request.form['title']
            story = request.form['story']
            criteria = request.form['criteria']
            business_value = request.form['Business_Value']
            estimation = request.form['Estimation']
            with open('data.csv', 'a') as data_file:
                writer = csv.DictWriter(data_file, fieldnames=fieldnames)
                writer.writerow({'ID': id, 'Story Title': title, 'User Story': story, 'Acceptance criteria': criteria,
                                           'Business value': business_value, 'Estimation': estimation})
    with open ('data.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
    return render_template('index.html', data=data)


@app.route('/story/<id>')
@app.route('/story', methods=['GET'])
def route_story(id=None, story=None):
    with open ('data.csv', 'r') as file:
        data_file = csv.DictReader(file)
        data = list(data_file)
        if id:
            for line in data:
                if line['ID'] == str(id):
                    story = line
    return render_template('story.html', data=data, id=id, story=story)



if __name__ == "__main__":
    app.secret_key = 'what is this?'  # Change the content of this string
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )