from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello CSCI 4795/6795. This is index page."
@app.route("/about")
def about():
    return "Hello CSCI 4795/6795. This is about page."
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)