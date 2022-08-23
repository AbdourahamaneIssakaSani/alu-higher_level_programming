#!/usr/bin/python3
"""Class Square that inherit from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """"
            Class Square inheriting Rectangle
            Attr :
                    id: number
                    size: number
                    x: number
                    y: number
        """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) <{}>/<{}> - {}" \
            .format(self.id, self.x, self.y, self.size)
