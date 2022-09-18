#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.testcase.test.test_api import DemoAPI, DemoAPI2


class RunTcClass:

    def __init__(self):
        self.suites = unittest.TestLoader()
        self.suit = unittest.TestSuite()

    def run(self, testcase_class, verbosity=2):
        """
        :param testcase_class: 引入的类名
        :param verbosity:
        """
        if isinstance(testcase_class, list):
            for _ in testcase_class:
                suites = self.suites.loadTestsFromTestCase(_)
                self.suit.addTest(suites)
        else:
            suites = self.suites.loadTestsFromTestCase(testcase_class)
            self.suit.addTest(suites)

        runner = unittest.TextTestRunner(verbosity=verbosity)
        runner.run(suite_tc.suit)


if __name__ == '__main__':
    suite_tc = RunTcClass()
    suite_tc.run([
        DemoAPI,
        DemoAPI2
    ])
