from flask import Flask, render_template, request
import db

current_year = db.Year("2025")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", year=current_year)

@app.route("/day/<month>/<day>", methods = ["GET", "POST"])
def day(month, day):
    if request.method == "POST":
        rainfall = float(request.form.get("rainfall"))
        try:
            current_year.put(month, int(day), rainfall)
            return render_template("day.html", data = {
                "day":day,
                "month":month,
                "rainfall":rainfall
            })
        except IndexError:
            return render_template("day_not_found.html", data={
                "day":day,
                "month":month,
            }, int=int)
    try: rainfall = current_year.get(month, int(day))
    except IndexError:
        rainfall = 0
    return render_template("day.html", data={
        "day":day,
        "month":month,
        "rainfall":rainfall
    })

@app.route("/month/<month>")
def month(month):
    data = current_year.data(month)
    rainfall_data = current_year.json[month][1:]

    return render_template("month.html", data=data, rainfall_data=rainfall_data, month=month)

app.run("0.0.0.0", "8080", debug=True)