import sys
import time


def year():
    return time.localtime()[0]


def month():
    return time.localtime()[1]


def day():
    return time.localtime()[2]


def hour():
    return time.localtime()[3]


def minute():
    return time.localtime()[4]


def second():
    return time.localtime()[5]


def millis():
    return int(time.time() * 1000)
