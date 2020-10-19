__author__ = "yavidor"


class Owl:

    def __init__(self, age=0, name="Moshe"):
        self._age = age
        self._name = name

    def birthday(self):
        self._age += 1

    def getAge(self):
        return self._age

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def __str__(self):
        return "Name: {} \n Age: {}".format(self._name, self._age)