
import logging
import datetime

from config import Configer

def get_logger(name):
    today_str = datetime.date.today().strftime('%Y-%m-%d')
    fileHandler = logging.FileHandler(filename='log_{}.txt'.format(today_str))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    logger = logging.getLogger(name)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    logger.setLevel(Configer.get('logger','level'))
    return logger
