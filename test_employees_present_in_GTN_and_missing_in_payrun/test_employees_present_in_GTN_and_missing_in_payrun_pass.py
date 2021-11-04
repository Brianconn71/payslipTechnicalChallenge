import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payrun_employee_Series = pd.read_excel("fail_data/PayrunWrongEmployeeId.xlsx", skiprows=[1], usecols=["Employee ID"], squeeze=True)
        cls.GTN_employee_Series = pd.read_excel("pass_data/GTN.xlsx", usecols=["employee_id"], squeeze=True)

    def test_employees_in_GTN_and_missing_in_payrun(self):
        payrun_employee_Series_cleaned = self.payrun_employee_Series.dropna()
        payrun_employee_Series_reformated = payrun_employee_Series_cleaned.astype("int64")
        series_match = payrun_employee_Series_reformated.equals(self.GTN_employee_Series)
        self.assertFalse(series_match, "The Employees are present in GTN AND in payrun file")


if __name__ == '__main__':
    unittest.main()