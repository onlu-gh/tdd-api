import unittest
import Code


# from unittest import mock
# from unittest.mock import patch, MagicMock


class TestCode(unittest.TestCase):

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

    if __name__ == '__main__':
        unittest.main()
