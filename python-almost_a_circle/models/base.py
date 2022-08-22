#!/usr/bin/python3
"""Class Base"""


class Base:
    """"
        Class Base
        Attr :
                id: number
    """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        self.id = id

    @property
    def id(self):
        """Doc"""
        return self.__id

    @id.setter
    def id(self, value):
        """Doc"""
        if value is None:
            self.__id = self.__nb_objects
        else:
            self.__id = value
