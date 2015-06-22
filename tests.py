import unittest
from selenium import webdriver
from FBEraser import Eraser
from test_settings import email, password

"""
set an email and a password in a
python module called test_settings.py
"""


class EraserTest(unittest.TestCase):

    def setUp(self):
        self.eraser = Eraser(email, password)

    def test_setup(self):
        self.assertIsInstance(self.eraser.driver, webdriver.Firefox)

    def test_login_function(self):
        """
        Login and check the title of the page
        :return:
        """
        self.eraser.login()
        self.assertTrue('Facebook' in self.eraser.driver.title)

    def tearDown(self):
        self.eraser.quit()


if __name__ == '__main__':
    unittest.main()
