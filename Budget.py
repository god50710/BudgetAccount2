import calendar
from datetime import datetime


class Budget:
    def __init__(self, time, amount):
        self.time = time
        self.amount = amount

    def first_day(self):
        return datetime.strptime(self.time + "01", "%Y%m%d")

    def last_day(self):
        return datetime.strptime(
            self.time + str(calendar.monthrange(int(self.time[0:3]), int(self.time[4:]))[1]), "%Y%m%d")

    def amount_of_day(self):
        return self.amount / self.last_day().day