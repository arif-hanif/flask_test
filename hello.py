import os

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/login', methods=['GET', 'POST'])

def login():
    if flask.request.values and flask.request.method == 'POST':
        return flask.redirect("/")
    else:
        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="Submit">Submit</button></form>'

if __name__ == '__main__':

    app.debug = True
    app.run()

