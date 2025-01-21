from flask import Flask, render_template, request, redirect
import db

current_year = db.Year("2025")

app = Flask(__name__)

@app.route("/")
def index():
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data = [current_year.data("01")["total"],current_year.data("02")["total"],current_year.data("03")["total"],current_year.data("04")["total"],current_year.data("05")["total"],current_year.data("06")["total"],current_year.data("07")["total"],current_year.data("08")["total"],current_year.data("09")["total"],current_year.data("10")["total"],current_year.data("11")["total"],current_year.data("12")["total"]]
    return render_template("index.html", year=current_year, labels=labels, data=data)

@app.route("/day/<month>/<day>", methods = ["GET", "POST"])
def day(month, day):
    if request.method == "POST":
        rainfall = float(request.form.get("rainfall"))
        try:
            current_year.put(month, int(day), rainfall)
            return redirect("/"+month)
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
    labels = []
    i=1
    for day in rainfall_data:
        labels.append(str(i))
        i+=1

    return render_template("month.html", data=data, rainfall_data=rainfall_data, month=month, labels=labels)

@app.route("/load")
def load():
    current_year.load()
    return "Database Changes Loaded"

app.run("0.0.0.0", "8080", debug=True)