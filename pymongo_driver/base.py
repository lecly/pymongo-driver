#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from pymongo import MongoClient
from bson.objectid import ObjectId
try:
    from config.database import mongorc
except:
    mongorc = {}


class Connection(object):

    def __init__(self, host=None, port=None):
        self.__connection = None
        self.__host = host
        self.__port = port

    def connect(self, db=None):
        client = MongoClient(host=self.__host, port=self.__port)
        if client and db:
            self.__connection = client[db]
            # print('status: {0}'.format('connection established'))
            # print('id: {0}'.format(id(self.__connection)))
            return self.__connection
        return None


class Base(object):

    db = None

    def __init__(self):
        if Base.db is None and mongorc:
            _host, _port, _db = mongorc.get('host'), mongorc.get('port'), mongorc.get('db')
            self.__connect(_host, _port, _db)

    def init(self, host, port, db):
        if Base.db is None:
            self.__connect(host, port, db)
        return True

    def __connect(self, host, port, db):
        Base.db = Connection(host, port).connect(db)


# 必填字段的 default 为 RequireField
class RequireField(object):
    pass


# 必填字段未填时, 抛出的异常为 RequireFieldError
class RequireFieldError(Exception):
    pass


# vim:ts=4:sw=4
