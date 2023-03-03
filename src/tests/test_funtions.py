import unittest
import os
from functions.Functions import Functions as Selenium

basedir = os.path.abspath(os.path.join(__file__, "../.."))
json_file = basedir + "/pages/enganche.json"

class TestGetJsonFile(unittest.TestCase):

    def test_get_json_file(self):
        print('Test valores permitidos')
        with open(json_file, 'r') as f:
            expected_contents = f.read()
        assert(Selenium.get_json_file(self,file='enganche'), expected_contents)


