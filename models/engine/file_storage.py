#!/usr/bin/python3
"""
    0x00. AirBnB clone - The console
    FileStorage class module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Class that serializes object/instances to a JSON file
    and deserializes JSON file to objects/instances
    """

    __file_path = 'file.json'
    __objects = {}

    CLASS = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }


    def all(self):
        """
        function that returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        function that sets in __objects the obj with key <obj class name>.id
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        function that serializes __objects to the JSON file
        """
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """
        function that deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                f_contents = f.read()
                dict_obj_dicts = json.loads(f_contents)
            for key, value in dict_obj_dicts.items():
                FileStorage.__objects[key] = FileStorage.CLASS[key.split('.')[0]](**value)
        except FileNotFoundError:
            pass
