import json
from flask import Flask, flash, request, render_template
from pip._vendor import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


@app.route("/")
def index():
    flash("Do you wanna play a Guess Number Games?")
    url = "https://guess-number-rest.azurewebsites.net/play"
    response = requests.get(url)
    contento = response.json().values()
    content = list(contento)[0]
    return render_template("index.html", content=content)


@app.route("/play", methods=["POST"])
def greeter():
    aws_service = request.form["yes_no"]
    if aws_service == "Yes":
        # if request.form.get("submit") == "PLAY":
        return render_template("options2.html")
    return render_template("options1.html", aws_service=aws_service)


@app.route("/enter_guess", methods=["POST"])
def greetery():
    url = "https://guess-number-rest.azurewebsites.net/guess"
    num = request.form.get("guess_input")
    contenty = request.form.get("id_input")
    json_data = {
        "message": contenty,
        "data": num,
    }
    contento_guess = requests.post(url, json=json_data).json().values()
    responso = requests.get(url, json=json_data).json().values()
    responsefinal = list(responso)[0]
    if responsefinal == "Correct You win!":
        return render_template(
            "win.html",
            num=num,
            contenty=contenty,
            responsefinal=responsefinal,
            contento_guess=contento_guess,
        )
    return render_template(
        "options.html",
        num=num,
        contenty=contenty,
        responsefinal=responsefinal,
        contento_guess=contento_guess,
    )
