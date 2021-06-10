import unittest

from command import Command


class TestCommand(unittest.TestCase):
    def test_breaks_lines_into_html(self):
        input = 'a line'
        expected = f'{input}<br/>'
        actual = Command.to_html(input)
        #assert actual == expected
        self.assertEqual(actual, expected)
