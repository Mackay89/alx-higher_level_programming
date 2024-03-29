#!/usr/bin/python3
"""
module that defines a base model class.
"""
import json
import csv
import turtle
import os.path


class Base:
    """
    class that defines properties of base.

    This Represent the 'base' for all other classes in project 0x0C*.

    Private class attributes:
    __nb_object (int): Nnumber of instantiated Base.
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """
        Initialize a new base.

        Args:
            id (init): The identity of the new Base.
        """

        if id is not None:
            self.id = id 
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of  list_dictinaries.
        
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json string.

        Args:
            json_strin (str): A JSO str representation of a list of dits.
        Returns:
            If json_string is None or empty - an emty list.
            Otherwise - the python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instatied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictinary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
                new_instance.update(**dictionary)
            elif cls.__name__ == "Square":
                new_instance = cls(1)
                new_instance.update(**dictionary)
            return new_instance
    

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of  instances.

        Reads from '<cls.__name__>.json'.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in listdicts]
        except IOError:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of rectangles or square in CSV file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]

                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())


    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of rectangle or square from CSV file.

        Reads from  "<cls.__name__>.csv".

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ +".csv"
        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    dictionary = ["id", "width", "height", "x", "y"]
                else:
                    dictionary = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, dictionary=dictionary)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangle and Square using the turtle module.

        Args:
            list_rectangles (list): A list of rectangle objects to draw.
            list_squares (list): Alist of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                for rect in list_rectangles:
                    turt.showturtle()
                    turt.up()
                    turt.goto(rect.x, rect.y)
                    turt.down()
                    for i in range(2):
                        turt.forward(rect.width)
                        turt.left(90)
                        turt.forward(rect.height)
                        turt.left(90)
                        turt.hideturtle()


        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
