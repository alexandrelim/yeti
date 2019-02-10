import logging

from logging import FileHandler
from logging import Formatter
from core.config.config import yeti_config

init = False 

USER_LOG_FILE = yeti_config.get('logging', 'filename', None)
userLogger = logging.getLogger("userLogger.messaging")

if USER_LOG_FILE != None :
	init = True 
	LOG_FORMAT = ("%(asctime)s [%(levelname)s]: %(message)s")
	userLogger_file_handler = FileHandler(USER_LOG_FILE)
	userLogger_file_handler.setFormatter(Formatter(LOG_FORMAT))
	userLogger.setLevel(logging.INFO)
	userLogger_file_handler.setLevel(logging.INFO)
	userLogger.addHandler(userLogger_file_handler)

def log(level, message):
	if init == True:
		logFunctions = {10:userLogger.debug,20:userLogger.info,30:userLogger.warning,40:userLogger.debug,50:userLogger.critical}
		logFunction = logFunctions.get(level, None)
		if logFunction != None: 
			logFunction(message)

	

