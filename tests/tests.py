import unittest
from names import get_formatted_name


class NameTest(unittest.TestCase):
    def test_first_middle_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin', 's')
        self.assertEqual(formatted_name, 'Janis S Joplin')

    def test_last_first_name(self):
        self.assertEquals('Janis Joplin', get_formatted_name('Janis', 'Joplin'))


unittest.main(verbosity=2)  # tells python to run the tests
