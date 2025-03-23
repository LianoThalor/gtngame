from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'geheimespasswort'  # nötig für Sessions


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if "number" not in session:
        session["number"] = random.randint(1, 10)

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            if guess == session["number"]:
                message = "🎉 Congratulations! You guessed the number!"
                session.pop("number")  # neues Spiel beim nächsten Laden
            elif guess < session["number"]:
                message = "The number is higher ⬆️"
            else:
                message = "The number is lower ⬇️"
        except ValueError:
            message = "Please enter a valid number."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)