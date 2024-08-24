class Time:
    # here print_to_time is a method
    def print_to_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

start = Time() # Creating object for the class
start.hour = 10
start.minute = 45
start.second = 56

start.print_to_time() # this start object is accesing the method