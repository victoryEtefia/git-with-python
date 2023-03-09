from flask import Flask


app=Flask(__name__)

@app.route("/")
def myhome():
    return "hello world 7"