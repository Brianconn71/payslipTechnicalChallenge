import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payrun_series = pd.read_excel("fail_data/PayrunWrongId.xlsx",
                                          skiprows=[1],
                                          usecols=["Employee ID"],
                                          squeeze=True)
        cls.GTN_series = pd.read_excel("pass_data/GTN.xlsx",
                                       usecols=["employee_id"],
                                       squeeze=True)

    def test_employees_in_GTN_and_missing_in_payrun(self):
        payrun_series_cleaned = self.payrun_series.dropna()
        payrun_series_reformated = payrun_series_cleaned.astype("int64")
        series_match = payrun_series_reformated.equals(self.GTN_series)
        self.assertFalse(series_match,
                         "The Employees are present in GTN AND in payrun file")


if __name__ == '__main__':
    unittest.main()
