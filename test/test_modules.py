import unittest

from unittest.mock import patch

from module_a import func_a


class TestBar(unittest.TestCase):

    def test_right_way(self):
        # If you want to patch a function imported in some module,
        # you should use a name of module that the function imported in 
        # insteand of the original function's module name.
        with patch('module_a.a.func_b', self._mock_func):
            self.assertEqual(func_a(), 'mocked function')

    def test_wrong_way(self):
        with patch('module_b.b.func_b', self._mock_func):
            self.assertEqual(func_a(), 'function b')

    def _mock_func(self):
        return 'mocked function'


if __name__ == '__main__':
    unittest.main()
