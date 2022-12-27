import converter as con
import converter_with_modules as conm
import unittest

class TestConverter(unittest.TestCase):

    def convert_and_get_data(self, conversion_method, args):
        conversion_method(args[0], args[1])
        with open(args[1], 'r') as fin:
            con_result = fin.readlines()
        print(con_result)
        return con_result


    def test_simple(self):
        args = ['tests/input1.csv', 'tests/output1.json']
        
        self.assertEqual(self.convert_and_get_data(con.convert_csv_to_json, args), 
                         self.convert_and_get_data(conm.convert_csv_to_json, args))


    def test_some_misses(self):
            args = ['tests/input2.csv', 'tests/output2.json']
            
            self.assertEqual(self.convert_and_get_data(con.convert_csv_to_json, args), 
                            self.convert_and_get_data(conm.convert_csv_to_json, args))


    def test_empty_file(self):
            args = ['tests/input3.csv', 'tests/output3.json']
            
            self.assertEqual(self.convert_and_get_data(con.convert_csv_to_json, args), 
                            self.convert_and_get_data(conm.convert_csv_to_json, args))

    		
if __name__ == '__main__':
    unittest.main()
