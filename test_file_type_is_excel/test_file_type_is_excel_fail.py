import unittest
import pathlib


class MyFileTypeTestCase(unittest.TestCase):
    """
    The below tests check if the file types are in .xlsx format
    """

    def setUp(self):
        self.GTN_file_ext = pathlib.Path("fail_data/fail_test.txt").suffix
        self.payslip_file_ext = pathlib.Path("fail_data/fail_test.txt").suffix

    def tearDown(self):
        self.GTN_file_ext = ""
        self.payslip_file_ext = ""

    def test_check_both_files_are_excel_files(self):
        self.assertNotEqual(self.GTN_file_ext,
                            self.payslip_file_ext,
                            "Both files are in .xlsx format")

    def test_check_GTN_file_is_not_a_excel_file(self):
        self.GTN_file_ext = pathlib.Path("fail_data/fail_test.txt").suffix
        self.assertNotEqual(self.GTN_file_ext,
                            self.payslip_file_ext,
                            "The GTN file is in .xlsx format")

    def test_check_payslip_file_is_not_a_excel_file(self):
        self.payslip_file_ext = pathlib.Path("fail_data/fail_test.txt").suffix
        self.assertNotEqual(self.GTN_file_ext,
                            self.payslip_file_ext,
                            "The payrun file is in .xlsx format")

    def test_check_both_files_are_not_excel_files(self):
        self.GTN_file_ext = pathlib.Path("fail_data/fail_test.txt").suffix
        self.payslip_file_ext = pathlib.Path("fail_data/fail_test.txt").suffix
        self.assertNotEqual(self.GTN_file_ext,
                            self.payslip_file_ext,
                            "Both files are not in .xlsx format")


if __name__ == '__main__':
    unittest.main()
