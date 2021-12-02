from quart import Quart
from quart import render_template, redirect, url_for

app = Quart("SpamBot")

@app.route("/")
async def home():
    return await render_template("index.html")

@app.route("/home")
async def homepage():
    return redirect(url_for("home"))

app.run(host = "0.0.0.0")
