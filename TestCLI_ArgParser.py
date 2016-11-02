import unittest
import argparse
from CLI_ArgParser import parse_cmd_line_args

class ArgumentParserError(Exception):
    pass


class MockArgumentParser(argparse.ArgumentParser):
    """
    Mock ArgumentParser so that it throws an exception rather than exit on a bad parameter
    """

    def error(self, message):
        raise ArgumentParserError(message)


class TestFirstMethods( unittest.TestCase):

    def test_parse_cmd_line_args_accepts_foo_switch(self):
        result = parse_cmd_line_args(['-foo'], MockArgumentParser)
        self.assertTrue(self, result.foo)

    @unittest.expectedFailure
    def test_parse_cmd_line_args_rejects_baz_switch_without_param(self):
            parse_cmd_line_args(['-baz'], MockArgumentParser)

    def test_parse_cmd_line_args_accepts_baz_with_param(self):
        result = parse_cmd_line_args(['-baz mumble'], MockArgumentParser)

        self.assertEqual("-baz mumble", result.mumble)

