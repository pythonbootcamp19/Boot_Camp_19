#pipenv install flask
#After the installation pipenv run python 1_simple_app.py
#pipenv install requests
#Flask is a framework which is used for web development
#Framework is a code somebody has writtend which you can use to build your app.
#Flask, DJango, are frameworks. Tenser flow is ML framework.
#Flask provids you the ability to add url for your Python functions.
#First 2 lines of codes are boilder code.
#@ is a decorator. It'll attch to your function. It takes the function hello_world

from flask import Flask
import json
app = Flask(__name__)
name = "Vikas"
hometown = "Bombay"
current_city = "Bangalore"
job = "Teacher"

site_info = {'counter':0}


counter = 0

@app.route('/hello')
def hello_world():
    return 'Hello, World!. This is Vik'

@app.route('/about')
def about():
    my_bio = f'''Hello, myself {name}, I am from {hometown},
            and currently living in {current_city},
            working as a {job}'''

    return my_bio

@app.route('/about/json')
def about_json():
    my_bio = {"name": name,
            "hometown": hometown,
            "current_city": current_city,
            "job":job}
    json_my_bio = json.dumps(my_bio)

    return json_my_bio

@app.route('/about/html')
def about_html():
    my_bio_html = f'''
    <html>
        <body>
        <h1> Hello, Myself {name}.</h1> </br>
        <p>I am from {hometown} and currently living in {current_city}</p>
        <p>Working as a {job}</p>
        </body>
    </html>
    '''
    return my_bio_html

@app.route('/count_visits')
def count_visits():
    site_info['counter'] += 1
    message = f"This page have been visited {site_info['counter']} times."
    return message

#IF i am running this code from the same file it'll run. But If you are importing it from any other file if condition will not run.
if __name__ == "__main__":
    app.run(debug = True)
