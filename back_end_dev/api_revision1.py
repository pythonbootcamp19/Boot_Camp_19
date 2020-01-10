from flask import Flask, request
import json
from tinydb import TinyDB, Query

db = TinyDB('revisiondb.json')
app = Flask(__name__)

details_list = []

@app.route('/')
def welcome_user():
    name = request.args.get("name")
    phone = request.args.get("phone")
    details_list.append(name)
    details_list.append(phone)
    db.insert({"name":name, "phone":phone})
    details_list1 = db.all()
    details_json = json.dumps(details_list1)
    return details_json


# @app.route('/show_users')
# def show_user():
#     details_list = db.all()
#     details_json = json.dumps(details_list)
#     return details_json


if __name__=="__main__":
    app.run(debug=True,port=8000)