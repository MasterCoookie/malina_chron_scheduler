import unittest

from cron_scheduler import *

class TestCronScheduler(unittest.TestCase):
    def test_cron_scheduler(self):
        args_list = [
            (1, 1, 1, [True, True, True, True, True, True, True]),
            (2, 7, 15, [True, True, True, True, True, False, False]),
        ]
        results = [
            '*/1 1-1 * * 0,1,2,3,4,5,6',
            '*/2 7-15 * * 1,2,3,4,5'
        ]

        for i, args in enumerate(args_list):
            self.assertEqual(generate_cron_line(*args), results[i])

if __name__ == '__main__':
    unittest.main()
