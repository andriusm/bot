#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from example import Example

#TODO: edit sample test case
class TestConfiguration(unittest.TestCase):

	def setUp(self):
		self.ex = Example()

	def tearDown(self):
		del(self.ex)

	def testVariable(self):
		expected = 120
		result = self.ex.fact(5)
		self.assertEqual(expected, result)

if __name__ == '__main__':
	unittest.main()