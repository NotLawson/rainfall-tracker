# Rainfall Tracker

This is a personal tracker for the rainfall up at Cooran. There is limited internet availability up there, so this can be self hosted.

It consists of 2 parts:
- Main Python Script: Runs on the NAS, provides webpage and logs data in the database
- Database Python Script: Manages the database using a JSON file

## Getting started

Download/clone this repository

Install `Flask`

Run `main.py`
It will use the port `8080`, but can be easily changed in the code.

## Todo

- [ ] Finish documentation
- [x] Add a configuration file
- [ ] Add automatic data recording (e.g. from a local weather station via Home Assistant)
- [ ] Add CSV/Excel exporting of data
- [ ] Record temperature and Humidity
- [x] Allow mulitple years
- [x] Add more graphs
