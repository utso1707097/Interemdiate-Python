import logging
import logging.config

#for using dict/file config method
logging.config.fileConfig('logging.conf')
'''
or
from logging import *
'''
#Logging is useful to track the error or exception or information.It also helps in debugging
#admin login info logout info
#If error occoured then shows the message

#most important method : basicConfig(**kwargs)
'''
this method is used to config logging system.
#filename
#filemode
#level
#format
#datefmt
#stream
#handler
'''
'''
#levels
NOTSET 0
DEBUG 10
INFO 20
WARNING 30
ERROR 40
CRITICAL 50
'''

'''
#Methods
getLogger()
info(msg)
warning(msg)
error(msg)
exception(msg)
'''

'''
#Format
foramt can take a string LogRecord attributes in any arrangement you like
asctime ex:%(asctime)s
created ex:%(created)f
fileanme ex:%(filename)f
levelname ex:%(levelno)s
message ex:%(message)s
'''
#this method used to config the logging system

#five different log level
#You can see warning info critical
'''
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',datefmt='%m/%d/%Y %H:%M:%S')
logging.warning("This is my warning")
logging.error("This is an error")
logging.critical("This is a critical")
logging.debug("This is a debug message")
logging.info("This is an info")
#By default our logger is call root logger
#log in different module in testlog.py
import testlog
'''
#Define and use log handler

'''
logger=logging.getLogger(__name__)
stream_h= logging.StreamHandler()
file_h=logging.FileHandler('file.log')

#Level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')

'''

logger=logging.getLogger('simpleExample')
logger.debug('this is a debug message')