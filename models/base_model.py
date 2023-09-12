#!/usr/bin/python3
"""String used for base class"""

import uuid
from datetime import datetime


class Basemodel:

	"""Classes used for base"""
	def  __init__(self, *args, **kwargs):
		"""Initialize updated time of instances and id

		Args:
		    args(string): Not used
		    Kwargs(dict): Values and keys declared during instantiation in a dictionary.

		"""
		if kwargs:
		    for key, value in kwargs.items():
			    if key != '__class__':
			        if key == 'created_at' of key == 'updated_at':
			            value = datetime.fromisoformat(value)
			    setattr(self, key, value)

		else:
		    self.id = str(uuid.uuid4())
	            self.updated_at = datetime.now()
		    self.created_at = datetime.now()
	            storage.new(self)

	def __str__(self):
		"""
		  Strings attribute to be made
		"""
		return "[{}] ({}) {}".\
	            format(__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""
		  Changes made to the saved objects
		"""

		self.updated_at = datetime.now()
	        storage.save()

	def to_dict(self):
		dict_copy = self.__dict__.copy()
		dict_copy["__class__"] = self.__class__.__name__
		dict_copy["updated_at"] = self.updated_at.isoformat()
		dict_copy["created_at"] = self.created_at.isoformat()
		return dict_copy
