import unittest
import pandas as pd


def check_columns_type(series):
    for cell in series.values:
        if cell == "int64" or cell == "float64":
            continue
        elif cell == object:
            return False
    return True


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.GTN_file = pd.read_excel("fail_data/GTNNotNumeric.xlsx")

    def test_pay_elements_in_GTN_are_numeric(self):
        pay_elements = self.GTN_file.dtypes[4:]
        self.assertTrue(check_columns_type(pay_elements), "Pay Elements in GTN file are NOT all numeric")


if __name__ == '__main__':
    unittest.main()