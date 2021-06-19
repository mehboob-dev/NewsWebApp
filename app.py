from flask import Flask, render_template, url_for, redirect

import db

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for("news"))
    # return 'News API is UP!<br><br>A part of <a href="https://t.me/sjprojects">Sj Projects</a>'

@app.route('/news')
def news():
    data = db.readsheet()[0].to_records()
    return render_template("index.html", datas = data)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, use_reloader=False)