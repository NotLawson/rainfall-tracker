from flask import Flask, render_template, request, redirect
import db
import json
import random


current_year = db.Year("2025")

config = json.load(open("config.json"))

port = config["port"]

years = {}
for year in config["years"]:
    years.update({year:db.Year(year)})

app = Flask(__name__)

def year_selector(request):
    year = request.cookies.get("year")
    if year in list(years.keys()):
        return years[year], year
    else:
        return years[config["years"][0]], config["years"][0]

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        year = request.form.get("years")
        if year in list(years.keys()):
            
            response = redirect("/")
            response.set_cookie("year", year)
            return response
    current_year, year_id = year_selector(request)

    years_raindata = {}
    colours = {}
    for year in years.values():
        raindata = [sum(year.json["01"][1:]), sum(year.json["02"][1:]), sum(year.json["03"][1:]), sum(year.json["04"][1:]), sum(year.json["05"][1:]), sum(year.json["06"][1:]), sum(year.json["07"][1:]), sum(year.json["08"][1:]), sum(year.json["09"][1:]), sum(year.json["10"][1:]), sum(year.json["11"][1:]), sum(year.json["12"][1:])]
        years_raindata.update({year.year:raindata})
        colours.update({year.year: f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"})

    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return render_template("index.html", year=current_year, labels=labels, year_id=year_id, years=years, raindata=years_raindata, colours=colours)

@app.route("/day/<month>/<day>", methods = ["GET", "POST"])
def day(month, day):
    current_year, _ = year_selector(request)
    if request.method == "POST":
        rainfall = float(request.form.get("rainfall"))
        try:
            current_year.put(month, int(day), rainfall)
            return redirect("/month/"+month)
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
    current_year, _ = year_selector(request)
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
    current_year, _ = year_selector(request)
    current_year.load()
    return "Database Changes Loaded"


app.run("0.0.0.0", "8080", debug=True)