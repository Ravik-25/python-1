from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    web_title = "ini halaman utama"
    return render_template('home.html',web_title= web_title )

@app.route("/about")
def about():
    web_title = "halaman about"
    return render_template('about.html', web_title = web_title)

