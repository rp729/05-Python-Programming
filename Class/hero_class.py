class Hero:
    def __init__(self,name,powers,colors,weakness):
        self.__name = name
        self.__powers = powers
        self.__colors = colors
        self.__weakness = weakness

    def set_name(self,name):
        self.__name = name

    def set_powers(self,powers):
        self.__powers = powers

    def set_colors(self,colors):
        self.__colors = colors

    def set_weakness(self,weakness):
        self.__weakness = weakness

    def get_name(self):
        return self.__name

    def get_powers(self):
        return self.__powers

    def get_colors(self):
        return self.__colors

    def get_weakness(self):
        return self.__weakness