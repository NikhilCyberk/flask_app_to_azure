
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'



@app.route('/message')
def message():
    return 'this is a message'


if __name__ == '__main__':
    app.run(debug=True)