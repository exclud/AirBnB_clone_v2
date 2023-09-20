#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from console import HBNBCommand


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
        self.assertIn(new, temp.values())

    def test_all_with_cls(self):
        """ __objects is properly returned with class filter"""
        new = BaseModel()
        temp = storage.all(cls=BaseModel)
        self.assertIsInstance(temp, dict)
        self.assertIn(new, temp.values())
        self.assertTrue(all(isinstance(v, BaseModel) for v in temp.values()))

    def test_all_with_no_cls(self):
        """ __objects is properly returned with no class filter"""
        new = BaseModel()
        temp = storage.all(cls=None)
        self.assertIsInstance(temp, dict)
        self.assertIn(new, temp.values())

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
        
    def test_delete(self):
        """ FileStorage delete method """
        new = BaseModel()
        key = new.__class__.__name__ + '.' + new.id
        storage.delete(new)
        self.assertNotIn(key, storage.all())

    def test_delete_non_existent(self):
        """ FileStorage delete method with non-existent object """
        new = BaseModel()
        key = new.__class__.__name__ + '.' + new.id
        storage.delete(new)
        new.id = "12345"
        self.assertNotIn(key, storage.all())

    def test_delete_none(self):
        """ FileStorage delete method with None """
        storage.delete(None)
        self.assertEqual(len(storage.all()), 1)
    

class TestConsole(unittest.TestCase):
    """ Class to test the console module """

    def setUp(self):
        """ Set up for the tests """
        self.console = HBNBCommand()

    def test_do_create_no_args(self):
        """ Test 'do_create' method with no arguments """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class(self):
        """ Test 'do_create' method with invalid class name """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_create_valid_class(self):
        """ Test 'do_create' method with valid class name """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) != 0)
