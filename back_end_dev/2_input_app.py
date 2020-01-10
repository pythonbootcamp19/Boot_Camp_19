from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get("name")
    result = f'Hello {name}, How are you today?'
    return result

@app.route('/add')
def addition():
    # http://127.0.0.1:5000/add?first_no=3&second_no=5
    first_no = request.args.get('first_no')
    second_no = request.args.get('second_no')
    if first_no != None and second_no != None:
        addition_output = int(first_no) + int(second_no)
        response = f"The sum of these two numbers is {addition_output}"
    else:
        response = "Please pass two numbers in the url."

    return response

@app.route('/subtract')
def subtract():
    first_no = request.args.get('first_no')
    second_no = request.args.get('second_no')
    values_present = first_no != None and second_no != None
    both_digits = first_no.isdigit() and second_no.isdigit()
    if values_present == True and both_digits == True:
        subtract_output = int(first_no) - int(second_no)
        response = f"The sum of these two numbers is {subtract_output}"
    else:
        response = "please pass two numbers in the url"

    return response

@app.route('/divide')
def divide():
    first_no = request.args.get('first_no')
    second_no = request.args.get('second_no')
    if first_no != None and second_no != None:
        divide = int(first_no) / int(second_no)
        response = f"The sum of these two nubers is {divide}"
    else:
        response = "please pass two numbers in the url"

    return response

@app.route('/multiply')
def multiply():
    first_no = request.args.get('first_no')
    second_no = request.args.get('second_no')
    if first_no != None and second_no != None:
        multiply = int(first_no) * int(second_no)
        response = f"The sum of these two numbers is {multiply}"
    else:
        response = f"please pass two numbers in the url"

    return response


if __name__ == "__main__":
    app.run(debug=True)