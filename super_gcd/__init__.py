from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


def gcd(x, y):
    """Returns the greatest common denominator of x and y"""
    for i in range(min(x, y) + 1, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        try:
            x = int(request.form["number_1"])
            y = int(request.form["number_2"])
            xy_gcd = gcd(x, y)
            message = f"The GCD is {xy_gcd}."
        except (KeyError, ValueError):
            message = "Invalid value!"
        return render_template("index.html", message=message)
