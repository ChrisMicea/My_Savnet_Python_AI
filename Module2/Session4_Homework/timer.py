class Timer:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds >= 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes >= 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours >= 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer1 = Timer(23, 59, 59)
print(timer1)
timer1.next_second()
print(timer1)
timer1.prev_second()
print(timer1)