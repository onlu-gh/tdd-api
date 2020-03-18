import Code
import unittest
from unittest.mock import patch, Mock, MagicMock


class TestCode(unittest.TestCase):
    """
    # Feature #1
    """

    def test_get_all_characters(self):
        self.assertEqual(str(len(Code.get_characters())),
                         Code.get_characters()[-1][0])
        with patch('Code.requests.get') as mocked_get:
            mocked_get.return_value.content = '{"results":' \
                                              '[{"id":1,"name":' \
                                              '"Rick Sanchez",' \
                                              '"status":"Alive",' \
                                              '"species":"Human",' \
                                              '"type":"","gender":' \
                                              '"Male"}]}'.encode()
            test = Code.get_characters()
            mocked_get.assert_called_with('https://rickandmortyapi.'
                                          'com/api/character/')
            self.assertEqual(test, [['1', 'Rick Sanchez', 'Alive',
                                     'Human', 'Male']])

    def test_get_single_character(self):
        self.assertEqual(len(Code.get_characters(5)), 1)
        self.assertEqual(Code.get_characters(5)[0][0], '5')

        self.assertEqual(Code.get_characters(100000), 'error')
        self.assertEqual(Code.get_characters(-10), 'error')

        self.assertEqual(Code.get_characters('a'), 'error')

        mocked_parameter = MagicMock()
        ret_val = Code.get_characters(mocked_parameter)
        self.assertEqual(dir(mocked_parameter)[0], '__ne__')
        self.assertEqual(ret_val, 'error')

    def test_get_multiple_character(self):
        char_list = Code.get_characters([1, 2, 4, 6])
        self.assertEqual(len(char_list), 4)
        self.assertEqual(char_list[0][0], '1')
        self.assertEqual(char_list[1][0], '2')
        self.assertEqual(char_list[2][0], '4')
        self.assertEqual(char_list[3][0], '6')

        self.assertEqual(Code.get_characters([]), 'error')
        self.assertRaises(TypeError, Code.get_characters(), ['a'])

        mocked_parameter = Mock()
        ret_val = Code.get_characters(mocked_parameter)
        self.assertFalse(mocked_parameter.called)
        self.assertEqual(ret_val, 'error')

    def test_get_characters_single_filter(self):
        char_list = Code.get_characters(['?', 'species=Human'])
        for char in char_list:
            self.assertIn('human', str.lower(char[3]))

    def test_get_characters_multi_filter(self):
        char_list = Code.get_characters(['?', 'species=Alien',
                                         'status=Alive',
                                         'gender=Unknown'])
        for char in char_list:
            self.assertIn('alien', str.lower(char[3]))
            self.assertIn('alive', str.lower(char[2]))
            self.assertIn('unknown', str.lower(char[4]))

    """
    # Feature #2
    """

    def test_get_all_episodes(self):
        self.assertEqual(str(len(Code.get_episodes())),
                         Code.get_episodes()[-1][0])
        with patch('Code.requests.get') as mocked_get:
            mocked_get.return_value.content = '{"results":' \
                                              '[{"id":1,"name":' \
                                              '"Pilot",' \
                                              '"air_date":' \
                                              '"December 2, 2013",' \
                                              '"episode":"S01E01"' \
                                              '}]}'.encode()
            test = Code.get_episodes()
            mocked_get.assert_called_with('https://rickandmortyapi.'
                                          'com/api/episode/')
            self.assertEqual(test, [['1', 'Pilot', 'December 2, 2013',
                                     'S01E01']])

    def test_get_single_episode(self):
        self.assertEqual(len(Code.get_episodes(9)), 1)
        self.assertEqual(Code.get_episodes(9)[0][0], '9')

        self.assertEqual(Code.get_episodes(200000), 'error')
        self.assertEqual(Code.get_episodes(-25), 'error')

        self.assertEqual(Code.get_episodes('b'), 'error')

        mocked_parameter = MagicMock()
        ret_val = Code.get_episodes(mocked_parameter)
        self.assertEqual(dir(mocked_parameter)[0], '__ne__')
        self.assertEqual(ret_val, 'error')

    def test_get_multiple_episodes(self):
        ep_list = Code.get_episodes([8, 10, 15, 16])
        self.assertEqual(len(ep_list), 4)
        self.assertEqual(ep_list[0][0], '8')
        self.assertEqual(ep_list[1][0], '10')
        self.assertEqual(ep_list[2][0], '15')
        self.assertEqual(ep_list[3][0], '16')

        self.assertEqual(Code.get_episodes([]), 'error')
        self.assertRaises(TypeError, Code.get_episodes(), ['b'])

        mocked_parameter = Mock()
        ret_val = Code.get_episodes(mocked_parameter)
        self.assertFalse(mocked_parameter.called)
        self.assertEqual(ret_val, 'error')

    def test_get_episodes_single_filter(self):
        ep_list = Code.get_episodes(['?', 'episode=S02'])
        for ep in ep_list:
            self.assertIn('S02', str.upper(ep[3]))

    def test_get_episodes_multi_filter(self):
        ep_list = Code.get_episodes(['?', 'name=Rick',
                                     'episode=S03'])
        for ep in ep_list:
            self.assertTrue('S01' in str.upper(ep[3]) or
                            'S03' in str.upper(ep[3]))

    if __name__ == '__main__':
        unittest.main()
