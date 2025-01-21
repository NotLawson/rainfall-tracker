# Rainfall Tracker

This is a personal tracker for the rainfall up at Cooran. There is limited internet availability up there, so this can be self hosted.

It consists of 2 parts:
- Main Python Script: Runs on the NAS, provides webpage and logs data in the database
- Database Python Script: Manages the database using a JSON file

![A screenshot of the year view](docs/year.png.png "Year View")
![A screenshot of the month view](docs/month.png.png "Month View")

## Quick start

> Want the run a demo? Go to the example branch to download some demo data

Go to the latest [release](https://github.com/NotLawson/rainfall-tracker/releases) and download the source code.

Install `flask` via `pip` (`pip install flask`)

Edit configuration and create year files (See Configuration)

Run `main.py`. It will run using the port specified in the config file

## Configuration

The default configuration file looks like this:
~~~
{
    "port":8080,
    "years":["example"]
}
~~~
- `port`: Sets what port the app should run on
- `years`: Specify the year files to load

### Year files

Year files are where your rainfall data is stored. They also contain meta data about the year.

An example year file should look like this

`/db/data/2025.json`
~~~
{
    "year":"2025",
    "01":[{"total":234, "avg":3.4}, 2, 0, 5...],
    "02":[{"total":124, "avg":5.6}, 4, 6, 2...],
    ...
}
~~~
- `year`: The year identifier. It MUST match the filename without the extention. e.g. `year1.json` = `"year":"year1"`, `Some Year.json` = `"year":"Some Year"`

There is a full default file in the `data` folder (`example.json`). To create a new year, duplicate that and change the metadata.

## Todo

- [ ] Finish documentation
- [x] Add a configuration file
- [ ] Add automatic data recording (e.g. from a local weather station via Home Assistant)
- [ ] Add CSV/Excel exporting of data
- [ ] Record temperature and Humidity
- [x] Allow mulitple years
- [x] Add more graphs

## File tree
~~~
/-
 |- db/ - contains the database
 |    |- __init__.py - This is the database library
 |    |- data/
 |           |- example.json - This is the template file for other year files
 |           | (add more years by duplicating the example and adjusting config)
 |           | (filename MUST match year name)
 |- static/ - Static files for the web app
 |        |- css.css - Main css file for all pages. Feel free to edit this, but backup your custom theme
 |        |  before updating as it may be overwritten
 |- templates/ - Contains the HTML templates served by Flask
 |           |- day.html - HTML template for editing a specific day
 |           |- month.html - HTML template for viewing a specific month
 |           |- index.html (aka year.html) - HTML template for viewing and switching years, also the  
 |           |  homepage
 |           |- day_not_found.html - HTML template used when trying to edit a day out of order
 |- config.json - See Configuration
 |- main.py - Main script
 |- README.md - Documentation, this file
~~~

## Acknowledgements

### Libraries
- [`flask`](https://flask.palletsprojects.com/en/stable/) ([here](https://github.com/search?q=repo%3ANotLawson%2Frainfall-tracker%20flask&type=code))
- [`chart.js`](https://www.chartjs.org/) ([here](https://github.com/search?q=repo%3ANotLawson%2Frainfall-tracker%20chart.js&type=code))

### Contributors
- [`@NotLawson`](https://github.com/NotLawson)
