import os
from flask import Flask, render_template, request

'''
To run through Command Prompt:
    set FLASK_ENV=development
    set FLASK_APP=app
    flask run
'''

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route('/request')
def request():
    return render_template("google-request.html")

# @app.route('/request/edna-known')
# def known():
#     return render_template("known.html")
#
# @app.route('/request/edna-unknown')
# def unknown():
#     return render_tempalte("unknown.html")

@app.route('/sent', methods=['POST'])
def sent():
    return render_template("sent.html", title="Request Sent!")


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
