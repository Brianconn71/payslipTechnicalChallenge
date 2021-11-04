import unittest
import pandas as pd


def check_columns_type(series):
    for cell in series.values:
        if cell == int or float:
            continue
        else:
            return False
    return True


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.GTN_file = pd.read_excel("pass_data/GTN.xlsx")

    def test_pay_elements_in_GTN_are_numeric(self):
        pay_elements = self.GTN_file.dtypes[4:]
        self.assertTrue(check_columns_type(pay_elements))


if __name__ == '__main__':
    unittest.main()