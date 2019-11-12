class Car:
    def __init__(self,year,make,speed=0):
        self.__year = year
        self.__make = make
        self.__speed = speed

    def set_year(self,year):
        self.__year = year

    def set_make(self,make):
        self.__make = make

    def set_speed(self,speed):
        self.__speed = speed

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self,speed=5):
        self.__speed += speed
        return self.get_speed()

    def decelerate(self,speed=5):
        self.__speed -= speed
        return self.get_speed()

