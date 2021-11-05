import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        GTN_columns = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        payrun_columns = [25, 26, 27,
                          28, 29, 30,
                          31, 32, 33,
                          34, 35, 36,
                          37, 38, 39,
                          40, 41, 42,
                          43, 44, 45,
                          46, 47, 48,
                          49, 50, 51,
                          52, 53]
        cls.GTN_df = pd.read_excel("pass_data/GTN.xlsx",
                                   usecols=GTN_columns)
        cls.payrun_df = pd.read_excel("pass_data/Payrun.xlsx",
                                      skiprows=[1],
                                      usecols=payrun_columns)

    def test_GNT_and_payrun_dataframe_are_not_equal(self):
        dataframe_equals_result = self.GTN_df.equals(self.payrun_df)
        self.assertFalse(dataframe_equals_result,
                         "GTN file DOES map to payrun file")


if __name__ == '__main__':
    unittest.main()
