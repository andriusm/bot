import os
import logging

class Logger():
	def __init__(self):
		logdir = "log"
		logname = "bot"
		format = '%(asctime)s %(levelname)s %(message)s'
		level = logging.DEBUG

		if not os.path.exists(logdir):
			os.makedirs(logdir)
		self.logger = logging.getLogger(logname)
		hdlr = logging.FileHandler(logdir + '/' + logname)
		formatter = logging.Formatter(format)
		hdlr.setFormatter(formatter)
		self.logger.addHandler(hdlr) 
		self.logger.setLevel(level)

	def info(self, msg):
		self.logger.info(msg)

	def warn(self, msg):
		self.logger.warn(msg)

	def error(self, msg):
		self.logger.error(msg)