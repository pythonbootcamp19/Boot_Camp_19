from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def welcome_user():
    name = request.args.get('name')
    phone = request.args.get('phone')

    if name == None and phone == None:
        return "Please enter the details"
    else:
        return "You're details is updated"


if __name__=="__main__":
    app.run(debug=True)