import unittest
import cron_exp_parser

class TestCronExpParsingMethods(unittest.TestCase):
    # '1 1 1 1 1 ls'
    test_dict1 = {
                'minute': '1', 
                'hour': '1', 
                'day of month': '1', 
                'month': '1', 
                'day of week': '1', 
                'command': 'ls'
            }

    # */15 0 1,15 * 1-5 /usr/bin/find
    test_dict2 = {
                'minute': '0 15 30 45', 
                'hour': '0', 
                'day of month': '1 15', 
                'month': '1 2 3 4 5 6 7 8 9 10 11 12', 
                'day of week': '1 2 3 4 5', 
                'command': '/usr/bin/find'
            }

    def test_cron_exp_parser1(self):
        self.assertEqual(cron_exp_parser.cron_exp_parse('1 1 1 1 1 ls'), self.test_dict1)

    def test_cron_exp_parser2(self):
        self.assertEqual(cron_exp_parser.cron_exp_parse('*/15 0 1,15 * 1-5 /usr/bin/find'), self.test_dict2)

    def test_generate_table_string1(self):
        self.assertEqual(cron_exp_parser.generate_table_string(self.test_dict1, 14), 'minute         1\nhour           1\nday of month   1\nmonth          1\nday of week    1\ncommand        ls\n')


if __name__ == '__main__':
    unittest.main()
    