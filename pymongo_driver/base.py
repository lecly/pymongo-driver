#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from pymongo import MongoClient
from bson.objectid import ObjectId
from config.database import mongorc


class Connection(object):

    def __init__(self, host=None, port=None):
        self.__connection = None
        self.__host = host
        self.__port = port

    def connect(self, db=None):
        client = MongoClient(host=self.__host, port=self.__port)
        if client and db:
            self.__connection = client[db]
            return self.__connection
            # print('status: {0}'.format('connection established'))
            # print('id: {0}'.format(id(self.__connection)))
        return None


class Base(object):

    db = None

    def __init__(self):
        if Base.db is None:
            _host, _port, _db = mongorc['host'], mongorc['port'], mongorc['db']
            Base.db = Connection(_host, _port).connect(_db)


# 必填字段的 default 为 RequireField
class RequireField(object):
    pass


# 必填字段未填时, 抛出的异常为 RequireFieldError
class RequireFieldError(Exception):
    pass


# vim:ts=4:sw=4
