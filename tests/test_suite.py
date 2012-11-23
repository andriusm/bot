#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from test_configuration import TestConfiguration

class BotTestSuite(unittest.TestSuite):
	def add(self, test_case):
		tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
		self.addTests(tests)

	def suite(self):
		self.add(TestConfiguration)
		return self