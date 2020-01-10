from flask import Flask, request
from tinydb import TinyDB, Query
import json

db = TinyDB('user_db.json')
User = Query() 
app = Flask(__name__)

@app.route('/')
def home():
    message = """
    <html>
        <body>
            <p> Go to <a href='/hello'>/hello</a></p>
            <p> Go to <a href='/user_info'>/user_info</a></p>
            <p> Go to <a href='/user_list'>/user_list</a></p>
        </body>
    </html>
    """
    return message


@app.route('/user_info')
def user_info():
    #http://127.0.0.1:5000/user_info?user_name=vik&phone_no=1234567890
    # user_name = request.args.get('user_name')
    # phone_no = request.args.get('phone_no')

    if user_name == None and phone_no == None:
        response = "Please enter firstname and phone no."
        return response
        # user_name_output = user_name 
        # phone_no_output = phone_no
        
        #db.insert({"user_name":user_name_output, "phone_no":phone_no_output})
        
        #response = f"The user name is: {user_name_output}, phone no. is: {phone_no_output},"
    else:
        user_name = request.args.get('user_name')
        phone_no = request.args.get('phone_no')
        response = db.insert({"user_name":user_name, "phone_no":phone_no})
        print(response)
        return response
name = 'Vik'
phone_no = 1234567890

@app.route('/user_list')
def user_list():
    user_info = {"name":name, "phone_no":phone_no}
    json_user_info = json.dumps(user_info)

    return json_user_info


@app.route('/hello')
def hello_world():
    return 'Hello, World!. This is Vik'

# name = request.args.get('name')
# phone_no = request.args.get('phone_no')


if __name__ == "__main__":
    app.run(debug = True,port = 8000)
