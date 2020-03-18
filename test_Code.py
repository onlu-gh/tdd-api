import unittest
import Code


# from unittest import mock
# from unittest.mock import patch, MagicMock


class TestCode(unittest.TestCase):
    """
    # Feature #1
    """
    def test_get_all_characters(self):
        self.assertEqual(str(len(Code.get_characters())),
                         Code.get_characters()[-1][0])

    def test_get_single_character(self):
        self.assertEqual(len(Code.get_characters(5)), 1)
        self.assertEqual(Code.get_characters(5)[0][0], '5')

        self.assertEqual(Code.get_characters(100000), 'error')
        self.assertEqual(Code.get_characters(-10), 'error')

        self.assertEqual(Code.get_characters('a'), 'error')

    def test_get_multiple_character(self):
        char_list = Code.get_characters([1, 2, 4, 6])
        self.assertEqual(len(char_list), 4)
        self.assertEqual(char_list[0][0], '1')
        self.assertEqual(char_list[1][0], '2')
        self.assertEqual(char_list[2][0], '4')
        self.assertEqual(char_list[3][0], '6')

        self.assertEqual(Code.get_characters([]), 'error')
        self.assertRaises(TypeError, Code.get_characters(), ['a'])

    def test_get_characters_single_filter(self):
        char_list = Code.get_characters(['?', 'species=Human'])
        for char in char_list:
            self.assertIn('human', str.lower(char[3]))

    def test_get_characters_multi_filter(self):
        char_list = Code.get_characters(['?', 'species=Alien', 'status=Alive', 'gender=Unknown'])
        for char in char_list:
            self.assertIn('alien', str.lower(char[3]))
            self.assertIn('alive', str.lower(char[2]))
            self.assertIn('unknown', str.lower(char[4]))

    if __name__ == '__main__':
        unittest.main()
