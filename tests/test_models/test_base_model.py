#!/usr/bin/env python3

"""Test module for the model base_class"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_new_object_instantiation(self):
        """Test for creating a new model object"""

        new_model = BaseModel()

        self.assertTrue(hasattr(new_model, "id"))
        self.assertTrue(hasattr(new_model, "created_at"))
        self.assertTrue(hasattr(new_model, "updated_at"))

    def test_new_object_instantiation_two(self):
        """Test for creating a new model object"""

        new_model = BaseModel()

        self.assertTrue(isinstance(new_model.id, str))
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_new_object_instantiation_three(self):
        """Test for creating a new model object from json"""

        new_model = BaseModel()
        new_model.name = "A New Model"
        new_model.number = 102

        model_json = new_model.to_dict()

        recreated_model = BaseModel(**model_json)

        self.assertEqual(new_model.name, recreated_model.name)
        self.assertEqual(new_model.number, recreated_model.number)
        self.assertEqual(new_model.id, recreated_model.id)
        self.assertEqual(new_model.created_at, recreated_model.created_at)
        self.assertIsNot(new_model, recreated_model)

    def test_str_representation(self):
        """Test for string representation of class"""

        new_model = BaseModel()

        str_rep = str(new_model)

        self.assertTrue(new_model.__class__.__name__ in str_rep)
        self.assertTrue(new_model.id in str_rep)
        self.assertTrue(str(new_model.__dict__) in str_rep)

        self.assertEqual(
            "[{}] ({}) {}".format(
                new_model.__class__.__name__, new_model.id, new_model.__dict__
            ), str_rep
        )

    def test_save_method(self):
        """Test for saving a model instance"""

        new_model = BaseModel()

        old_update_time = new_model.updated_at

        new_model.save()

        new_update_time = new_model.updated_at

        self.assertNotEqual(old_update_time, new_update_time)
        self.assertGreater(new_update_time, old_update_time)

    def test_export_to_json(self):
        """Test for exporting model instance to json"""

        new_model = BaseModel()

        json_value = new_model.to_dict()

        self.assertIn("__class__", json_value)
        json_value = new_model.to_dict()
        self.assertEqual(json_value["__class__"], BaseModel.__name__)

        self.assertTrue(isinstance(json_value["created_at"], str))
        self.assertTrue(isinstance(json_value["updated_at"], str))

        self.assertEqual(
            new_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            json_value["created_at"]
        )

        self.assertEqual(
            new_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            json_value["updated_at"]
        )
