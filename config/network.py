# -*- coding:utf-8 –*-
__author__ = 'gzs2477'

from business.basic import BasicDispatcher
from business.common import CommonService

SID_COMMON = 5200

def configDispatcher():
    dispatcher = BasicDispatcher()

    dispatcher.registerService(SID_COMMON, CommonService())

    return dispatcher