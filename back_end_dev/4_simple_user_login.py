from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!. This is Vik'


if __name__ == "__main__":
    app.run(debug = True)
