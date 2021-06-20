from flask import Flask, render_template, url_for, redirect, request

import db

app = Flask(__name__)
data = db.readsheet()[0].to_records()


@app.route('/')
def home():
    global data
    return render_template("index.html", datas=data)
    # return 'News API is UP!<br><br>A part of <a href="https://t.me/sjprojects">Sj Projects</a>'


@app.route('/news')
def news():
    global data
    data = db.readsheet()[0]
    reqcat = request.args.get("cat")
    if reqcat is not None:
        data = data.loc[data["Category"] == reqcat]
    data = data.to_records()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, use_reloader=False)
