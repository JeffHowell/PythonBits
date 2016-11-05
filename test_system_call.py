import unittest
from system_caller import SystemCaller



class MyTestCase(unittest.TestCase):

    uut = None

    def setUp(self):
        self.uut = SystemCaller()

    def test_successful_return_code(self):
        self.assertEqual(0, self.uut.system_call("ls"))

    def test_unsuccessful_return_code(self):
        self.assertEqual(1, self.uut.system_call(["ls", "cheese_monkey"], True))

    def test_successful_return_code_os_system(self):
        self.assertEqual(0, self.uut.os_system_call("true"))

    def test_unsuccessful_return_code_os_system(self):
        self.assertNotEqual(0, self.uut.os_system_call("false"))

    def test_successful_os_popen(self):
        output = self.uut.subprocess_check_output_call("ls -al")
        self.assertEqual(True, output.startswith('total'))

if __name__ == '__main__':
    unittest.main()
