import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.GTN_series = pd.read_excel("pass_data/GTN.xlsx",
                                       usecols=["employee_id"],
                                       squeeze=True)
        cls.payrun_series = pd.read_excel("pass_data/Payrun.xlsx",
                                          skiprows=[1],
                                          usecols=["Employee ID"],
                                          squeeze=True)

    def test_employees_in_payrun_and_missing_in_GTN(self):
        payrun_series_cleaned = self.payrun_series.dropna()
        payrun_series_reformated = payrun_series_cleaned.astype("int64")
        series_match = payrun_series_reformated.equals(self.GTN_series)
        self.assertFalse(series_match,
                         "The Employees in Payrun ARE present in GTN")


if __name__ == '__main__':
    unittest.main()
