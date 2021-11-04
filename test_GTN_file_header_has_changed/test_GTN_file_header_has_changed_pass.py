import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.GTN_df = pd.read_excel("pass_data/GTN.xlsx", header=None)

    def test_for_header_structure_before_change(self):
        GTN_dtype = self.GTN_df.dtypes
        GTN_dtype = GTN_dtype.value_counts()
        GTN_dtype_count = len(GTN_dtype)
        self.assertEqual(GTN_dtype_count, 1)

    def test_for_header_structure_after_change(self):
        self.GTN_df = pd.read_excel("fail_data/GTNTwoHeaders.xlsx")
        GTN_dtype = self.GTN_df.dtypes
        GTN_dtype_count = len(GTN_dtype)
        self.assertGreater(GTN_dtype_count, 1)


if __name__ == '__main__':
    unittest.main()