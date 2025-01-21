import json, os

cdir = os.path.dirname(os.path.realpath(__file__))

class Year:
    def __init__(self, year):
        self.year = year
        self.file = open(f"{cdir}/data/{year}.json", "w+")
        self.json = json.load(self.file)

    def load(self):
        self.json = json.load(self.file)
    
    def get(self, month, day):
        return self.json[month][day]
    
    def put(self, month, day, rainfall):
        length = len(self.json[month]) - 1
        if length + 1 == day:
            self.json[month].append(rainfall)
        elif length >= day:
            self.json[month][day] = rainfall
        else: raise IndexError

        days = self.json[month]
        del days[0]

        total = 0
        for val in days:
            total += val
        
        try: avg = total/length
        except ZeroDivisionError: avg = 0

        self.json[month][0] = {
            "total": total, 
            "avg": avg
        }

    def data(self, month):
        return self.json[month][0]