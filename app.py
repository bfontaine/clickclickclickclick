# -*- coding: UTF-8 -*-

from random import randint

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

def random_clicks(n=5):
    return ["click"] * randint(1, n)

def random_url():
    if randint(0, 999) == 0:
        # Good ol' Rick
        return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    parts = []
    # subdomains
    for _ in range(randint(0, 3)):
        parts.append("".join(random_clicks()))
        parts.append(".")

    # main domain
    parts.append("clickclickclickclick.click/")

    # path "dirs"
    for _ in range(randint(0, 4)):
        parts.append("".join(random_clicks()))
        parts.append("/")

    # query params
    first_param = True
    for _ in range(randint(0, 3)):
        parts.append("?" if first_param else "&")
        parts.append("%s=%s" % ("".join(random_clicks()),
                                "".join(random_clicks())))

    if randint(0, 1) == 1:
        parts.append("#")
        parts.append("".join(random_clicks()))

    return "http://%s" % "".join(parts)

@app.route('/')
@app.route('/<path:clicks>')
def home(clicks=None):
    return render_template("home.html",
            title=" ".join(random_clicks()).capitalize(),
            next_url=random_url())

@app.route('/<path:path>')
def catchall():
    return redirect(url_for("home"))
