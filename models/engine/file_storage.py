#!/usr/bin/python3
"""Objects saved in the module"""
import json
from os import path


Class FileStorage:
    """Class for the file storage

    The class here serialises an object to a json file and deserialises a json file to an object
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
	"""A dictionary of all objects to be returned"""
	return FileStorage.__objects

    def new(self, obj):
	"""A dictionary of a new object to be set

	Sets of an object in the __object dictionary with <obj class name>.id
	Args:
	    obj(object): a class instance
	"""

	key = "{}.{}.format(obj.__class__.__name__, obj.id)
	FileStorage.__objects[key] = obj"""

    def save(self):
	"""Must serialize __object to the json file"""
	serialized_objs = {}
    for key, value in Filestorage.__objects.iems():
	serialixed_objs[key] = valiue.to_dict()

    with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
    	json.dump(serialized_objs, f)

    def classes(self):
	"""A valid class list"""
	from models.base_model import BaseModel
	from models.city import City
	from models.user import User
	from models.amenity import Amenity
	from models.place import Place
	from models.state import State
	from models.review import Review

	classes = {"BaseModel": BaseModel,
		   "City" City,
		   "User" User,
		   "Amenity" Amenity,
		   "Place" Place,
		   "State" State,
		   "Review" Review}
	return classes

    def reload(self):
	"""The stored objects from the json file reloaded"""        if not path.isfile(FileStorage.__file__path):
	    return


    with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
        serialized_objects = json.load(f)

    deserialized_objects = {}

    for obj_id, serialized_obj in serialized_objects.items():
        class_name = serialized_obj['__class__']
        if class_name in self.classes():
            obj_class = self.classes()[class_name]
        else:
            continue

            deserialized_obj = obj_class(**serialized_obj)
            deserialized_objects[obj_id] = deserialized_obj

        FileStorage.__objects = deserialized_objects

    def attributes(self):
	"""Valid attributes and their classname to return"""        attributes = {
	    "BaseModel":
	             {"id": str,
	             "updated_at": datetime.datetime,
		     "created_at": datetime.datetime},
	    "City":
	    	     {"state_id": str,
	              "name": str},
	    "User":
		     {"email": str,
		      "password": str,
		      "first_name": str,
		      "last_name":str},
	    "Amentity":
		      {"name": str},
	    "Place":
		      {"city_id": str,
                       "user_id": str,
                       "name": str,
                       "description": str,
                       "number_rooms": int,
                       "number_bathrooms": int,
                       "max_guest": int,
                       "price_by_night": int,
                       "latitude": float,
                       "longitude": float,
                       "amenity_ids": list},
	    "Review":
	    {"place_id":str,
		    	"user_id": str,
			"text": str}
	}
	return attributes




