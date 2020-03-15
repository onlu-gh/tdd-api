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

        self.assertEqual(len(Code.get_characters(100000)), 0)

        self.assertEqual(len(Code.get_characters(-10)), 0)

    if __name__ == '__main__':
        unittest.main()
