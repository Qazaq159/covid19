from app import app
from flask import redirect, render_template
from test import Covid19

@app.route("/")
def mainpage():
    info = Covid19()
    data = [info.data['recovered'], info.data['deaths'], info.data['confirmed']]


    print(data)
    return render_template("index.html", country=info.data['country'],
                           recovered=data[0],
                           deaths=data[1],
                           process=data[2] - (data[0] + data[1]),
                           confirmed=data[2])


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def other(path):
    return redirect('/')
