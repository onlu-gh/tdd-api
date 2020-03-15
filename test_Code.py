import unittest
import Code


# from unittest import mock
# from unittest.mock import patch, MagicMock


class TestCode(unittest.TestCase):
    def test_get_all_characters(self):
        self.assertEqual(str(len(Code.get_all_characters())), Code.get_all_characters()[-1][0])

    if __name__ == '__main__':
        unittest.main()
