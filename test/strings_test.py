# test/strings_test.py
from ma13_lambdata.state_fxn import StateNames
from ma13_lambdata.null_fxn import col_nulls

import unittest

class TestStrings(unittest.TestCase):
    """
    class for function tests
    """
    def test_state_fxn(self):
        custom_df = CustomFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        assert custom_df.columns.tolist() == ["abbrev"]
        #self.assertEqual(custom_df.columns.tolist(), ["abbrev"])
        custom_df.state_convert() #test should always invoke functionality directly
        #self.assertEqual(custom_df.columns.tolist(), ["abbrev", "state_name"])
        assert custom_df.columns.tolist() == ["abbrev", "state_name"]

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_col_nulls(self):
        test_df = pd.DataFrame(np.random.randint(0, 100, size=(15, 3)), columns=list('ABCD'))
        self.assertTrue(col_nulls == 'Your dataframe contains no null values')



if __name__ == '__main__':
    unittest.main()
