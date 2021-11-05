import unittest
import pandas as pd


class MyLineBreakTestCase(unittest.TestCase):
    """
    The below tests the GTN file has line breaks
    """

    def setUp(self):
        self.GTN_df = pd.read_excel("pass_data/GTN.xlsx")

    def tearDown(self):
        self.GTN_df = ""

    def test_GTN_file_with_no_line_breaks(self):
        dropped_line_breaks = self.GTN_df.dropna(how="all")
        self.assertEqual(len(dropped_line_breaks),
                         len(self.GTN_df),
                         "GTN file has lineBreaks")

    def test_GTN_file_with_line_breaks(self):
        self.GTN_df_has_breaks = pd.read_excel("fail_data/GTNLineBreaks.xlsx")
        dropped_line_breaks = self.GTN_df_has_breaks.dropna(how="all")
        self.assertNotEqual(len(dropped_line_breaks),
                            len(self.GTN_df_has_breaks),
                            "GTN file has lineBreaks")


if __name__ == '__main__':
    unittest.main()
