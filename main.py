from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "MY FIRST WEBSITE!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)