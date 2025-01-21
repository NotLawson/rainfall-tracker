import json, os
cdir = os.path.dirname(os.path.realpath(__file__))

class Year:
    def __init__(self, year):
        self.year = year
        self.file = f"{cdir}/data/{year}.json"
        self.json = json.load(open(self.file, "r"))

    def load(self):
        self.json = json.load(open(self.file, "r"))
    
    def get(self, month, day):
        return self.json[month][day]
    
    def put(self, month, day, rainfall):
        length = len(self.json[month]) - 1
        if length + 1 == day:
            self.json[month].append(rainfall)
        elif length >= day:
            self.json[month][day] = rainfall
        else: raise IndexError

        days = self.json[month][1:]


        total = 0
        for val in days:
            total += val
        
        try: avg = total/(length+1)
        except ZeroDivisionError: avg = 0

        self.json[month][0] = {
            "total": total, 
            "avg": avg
        }

        file = open(self.file, "w")
        file.write(json.dumps(self.json))
        file.close()

    def data(self, month):
        return self.json[month][0]
