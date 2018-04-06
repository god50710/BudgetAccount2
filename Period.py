class Period:
    def __init__(self, start_time, end_time):
        if start_time and end_time and start_time < end_time:
            self.start_time = start_time
            self.end_time = end_time
        else:
            raise Exception

    def effective_days(self, budget):
        effective_start_time = self.start_time
        if budget.first_day() > self.start_time:
            effective_start_time = budget.first_day()

        effective_end_time = self.end_time
        if budget.last_day() < self.end_time:
            effective_end_time = budget.last_day()
        return (effective_end_time - effective_start_time).days + 1