import logging

logging.basicConfig(filename='charming.log', level=logging.DEBUG)


def log(msg):
    logging.debug(msg)
