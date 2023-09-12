#!/usr/bin/python3
"""BaseModel class cases to be tested"""
import sys
import unittest
from datetime import datetime
sys.path.insert(0, '../..')
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
	"""BaseModel class cases to be tested"""
	def setup(self):
		"""Default object for methods"""
		self.obj = BaseModel()

	def test_init(self)
	    """Object attributes to be tested"""
	    self.assertIsInstance(self.obj.id, str)
	    self.assertIsInstance(self.obj.created_at, datetime)

	def test_str(self):
		"""Testing the string method is properly returned"""
		self.assertEqual(self.obj.__str__, self.obj.__str__)
	
	def test_to_dict(self):
        """Dict method testing"""
        obj_dict = self.obj.to_dict()
        self.assertIsInstance(self.obj.to_dict(), dict)
        self.assertTrue(self.obj.to_dict())
        self.assertTrue(obj_dict['__class__'] == 'BaseModel')

	def test_save(self):
        """The save method to be tested"""
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertNotEqual(self.obj.save(), "")
        self.assertNotEqual(self.obj.updated_at, self.obj.save())
        self.assertEqual(self.obj.save(), self.obj.updated_at)
        self.assertEqual(self.obj.save(), None)


	if __name__ = '__main__':
	    unittest.main()
	    BaseModel()
