import unittest
import main


class Test_main(unittest.TestCase):


    def test_main(self):
        obj = main.Main_Class("testing")
        self.assertEqual(obj.name, "testing")

    def test_add(self):

        self.assertEqual(main.Main_Class.add(10,5),15)

if __name__ == '__main__':
    unittest.main()