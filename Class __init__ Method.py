# __init__ Method
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print_to_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

start = Time(10,45,56)
start.print_to_time() 