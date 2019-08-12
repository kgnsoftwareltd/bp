from flask import Flask
app = Flask(__name__)
@app.route('/')
def testroute():
    return "This is a test/demo for BP"
