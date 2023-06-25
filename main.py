from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", bmi="")


@app.route("/calculate", methods=["POST"])
def calculate():
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    bmi = weight / (height / 100) ** 2
    # the formula for it
    return render_template("index.html", bmi=bmi)


if __name__ == "__main__":
    app.run(debug=True)
