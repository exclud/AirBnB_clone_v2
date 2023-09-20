#!/usr/bin/python3
""" Module for testing console"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand

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
