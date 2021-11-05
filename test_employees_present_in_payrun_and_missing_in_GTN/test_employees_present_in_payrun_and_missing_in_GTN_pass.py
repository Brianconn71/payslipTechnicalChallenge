import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payrun_series = pd.read_excel("pass_data/Payrun.xlsx",
                                          skiprows=[1],
                                          usecols=["Employee ID"],
                                          squeeze=True)
        cls.GTN_series = pd.read_excel("fail_data/GTNWrongEmployeeId.xlsx",
                                       usecols=["employee_id"],
                                       squeeze=True)

    def test_employees_in_payrun_and_missing_in_GTN(self):
        payrun_series_cleaned = self.payrun_series.dropna()
        payrun_series_reformated = payrun_series_cleaned.astype("int")
        series_match = payrun_series_reformated.equals(self.GTN_series)
        self.assertFalse(series_match,
                         "The Employees are present in Payrun AND in GTN file")


if __name__ == '__main__':
    unittest.main()
