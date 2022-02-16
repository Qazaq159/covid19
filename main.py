from flask import Flask, redirect, render_template
from test import Covid19

app = Flask(__name__)


@app.route("/")
def mainpage():
    info = Covid19()
    return render_template("index.html", country=info.data['country'],
                           recovered=info.data['recovered'],
                           deaths=info.data['deaths'],
                           process=info.data['confirmed'] - (info.data['recovered'] + info.data['deaths']),
                           confirmed=info.data['confirmed'])


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def other(path):
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=False)
