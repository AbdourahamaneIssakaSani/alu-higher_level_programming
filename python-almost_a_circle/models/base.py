#!/usr/bin/python3
"""Class Base"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                for obj in list_objs:
                    file.write(cls.to_json_string([obj.to_dictionary()]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or \
                len(json_string) == 0:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(4, 3)
        if cls.__name__ == "Square":
            dummy_instance = cls(4)
        dummy_instance.update(**dictionary)
        return dummy_instance
