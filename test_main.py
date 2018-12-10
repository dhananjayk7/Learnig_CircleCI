import unittest
import main


class Test_main(unittest.TestCase):


    def test_main(self):
        obj = main.Main_Class("testing")
        self.assertEqual(obj.name, "testing")
