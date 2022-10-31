#!/usr/bin/env python3

"""Tests for the file storage module"""


import unittest
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for file storage"""

    def test_add_new_object_to_storage(self):
        """Test for adding a new object to storage"""

        new_model = BaseModel()

        self.assertIn("BaseModel." + new_model.id, storage.all())
        self.assertIn(new_model, storage.all().values())
