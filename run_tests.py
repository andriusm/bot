#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest

relativePath = os.path.dirname(__file__)
if len(relativePath) > 0:
	relativePath += "/"

sys.path.insert(0, relativePath + "src")
sys.path.insert(0, relativePath + "tests")

from test_suite import BotTestSuite

bot_suite = BotTestSuite()
runner = unittest.TextTestRunner()
runner.run(bot_suite.suite())