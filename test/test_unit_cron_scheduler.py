import unittest

from cron_scheduler import *

class TestCronScheduler(unittest.TestCase):
    def test_cron_scheduler_positive(self):
        args_list = [
            (1, 1, 1, [True, True, True, True, True, True, True]),
            (2, 7, 15, [True, True, True, True, True, False, False]),
            (5, 0, 23, [False, True, False, False, False, False, False]),
            (1, 0, 0, [True, True, True, True, True, True, True]),
        ]
        results = [
            '*/1 1-1 * * 0,1,2,3,4,5,6',
            '*/2 7-15 * * 1,2,3,4,5',
            '*/5 0-23 * * 2',
            '*/1 0-0 * * 0,1,2,3,4,5,6',
        ]

        for i, args in enumerate(args_list):
            self.assertEqual(generate_cron_line(*args), results[i])

    def test_cron_scheduler_negative(self):
        args_list = [
            (0, 1, 1, [True, True, True, True, True, True, True]),
            (1, 1, 1, [False, False, False, False, False, False, False]),
            (1, 2, 1, [True, True, True, True, True, True, True]),
            (-1, 1, 1, [True, True, True, True, True, True, True]),
            (1, 23, 25, [True, True, True, True, True, True, True]),
            (1, 1, 1, [True, True, True, True, True, True]),
            (1, 1, 1, [True, True, True, True, True, True, True, True]),
            (1, 25, 26, [True, False, False, False, False, False, False]),
            (1, -1, 1, [True, False, False, False, False, False, False]),
            (1, 1, -1, [True, True, True, True, True, True, False]),
        ]

        for args in args_list:
            self.assertRaises(Exception, generate_cron_line, *args)

if __name__ == '__main__':
    unittest.main()
