#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from logger import Logger

class Bot():
	""" Bot prototype """

	modules = {}
	moduleNames = []
	cfgFile = "cfg/bot.properties"

	def __init__(self):
		self.log = Logger()
		self.log.info("--------------------------------------------------------------------------------")

	def __cleanup(self, data):
		return [item.strip() for item in data]

	def read_configuration(self):
		self.log.info("Reading configuration")
		if not os.path.exists(self.cfgFile):
			self.log.error("Configuration file '"+ self.cfgFile +"' not found")
			return
		data = [self.__cleanup(line.strip().split("=")) for line in open(self.cfgFile)]
		self.cfg = dict(data)

	def loadModule(self, moduleName):
		self.modules.update( {moduleName : __import__(moduleName)} )

	def load_modules(self):
		self.log.info("Loading modules")
		self.moduleNames = self.__cleanup(self.cfg["modules"].split(","))
		for moduleName in self.moduleNames:
			self.loadModule(moduleName)
		print self.modules['rss']

	def run(self):
		self.log.info("Running...")

	def start(self):
		print "Starting..."
		self.read_configuration()
		self.load_modules()
		self.run()

def main():
	Bot().start()

if __name__ == '__main__':
	main()