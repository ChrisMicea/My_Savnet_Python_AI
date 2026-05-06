class WeekDayError(Exception):
    pass

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

class Weeker:
    def __init__(self, day: str):
        if day not in days_of_week:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n: int):
        current_index = days_of_week.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = days_of_week[new_index]

    def subtract_days(self, n: int):
        current_index = days_of_week.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = days_of_week[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")