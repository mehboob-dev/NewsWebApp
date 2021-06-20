from flask import Flask, render_template

import db

app = Flask(__name__)


@app.route('/')
def home():
    data = db.readsheet()[0].to_records()
    return render_template("index.html", datas=data)


@app.route('/<cat>')
def news(cat):
    data = db.readsheet()[0]
    if cat is not None:
        data = data.loc[data["Category"] == cat]
    data = data.to_records()
    return render_template("index.html", datas=data)


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, use_reloader=False)
