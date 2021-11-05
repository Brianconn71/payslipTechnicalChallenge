import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):
    """
    The below tests check if the GTN header structure has changed
    """

    def setUp(self):
        self.GTN_df = pd.read_excel("fail_data/GTNTwoHeaders.xlsx",
                                    header=None)

    def test_for_header_structure_before_change(self):
        GTN_dtype = self.GTN_df.dtypes
        GTN_dtype = GTN_dtype.value_counts()
        GTN_dtype_count = len(GTN_dtype)
        self.assertEqual(GTN_dtype_count,
                         1, "GTN file has 1 header row")

    def test_for_header_structure_after_change(self):
        self.GTN_df = pd.read_excel("pass_data/GTN.xlsx")
        GTN_dtype = self.GTN_df.dtypes
        GTN_dtype_count = len(GTN_dtype)
        self.assertLess(GTN_dtype_count,
                        1, "GTN file has more than one header row")


if __name__ == '__main__':
    unittest.main()
