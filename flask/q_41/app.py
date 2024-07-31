# 41. Write a Flask route that accepts a parameter in the URL and displays it on the page.
from flask import Flask, request

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello, " + name

if __name__ == "__main__":
    app.run()

