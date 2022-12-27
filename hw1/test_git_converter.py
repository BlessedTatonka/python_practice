from git_converter import *
import unittest

class TestGitConverter(unittest.TestCase):
    def test_prepare_title(self):
        self.assertEqual(prepare_title('# title'), '+ [](#)\n\n## \n\n')

    def test_prepare_desc(self):
        self.assertEqual(prepare_desc('# description'), '\n\n')

    def test_wrong_path(self):
        convert_to_md('no_such_file', 'no_such_file')
        convert_to_md('no_such_file')
        convert_to_md()
    		
if __name__ == '__main__':
    unittest.main()
