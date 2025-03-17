class Car:
    def __init__(self, model, year, speed):
        self.__model = model
        self.__year = year
        self.__speed = 0
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed

c = Car("Zen", 2023, 90)
print(f"Before modification: {c.__dict__}")

c.set_speed(200)
print(f"After modification: {c.__dict__}")
