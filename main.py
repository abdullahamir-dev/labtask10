from flask import flask
app = flask(_name_)
@app.route ('/')
def helloworld():
    return 'Hello, World!' 

    