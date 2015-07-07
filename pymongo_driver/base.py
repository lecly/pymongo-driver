#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from pymongo import MongoClient
from bson.objectid import ObjectId
from config.database import mongorc


class Connection(object):

    def __init__(self, host=None, port=None, connect=True, db=None):
        self.connection = None
        self.host = host
        self.port = port
        self._connect(connect, db)

    def connect(self, db=None):
        self._connect(True, db)

    def _connect(self, connect=True, db=None):
        if connect:
            client = MongoClient(host=self.host, port=self.port, connect=True)
            if client and db:
                self.connection = client[db]
                # print('\nstatus: {0}'.format('connection established'))
                # print('\nid: {0}'.format(id(self.connection)))


class Base(object):

    db = None

    def __init__(self):
        if Base.db is None:
            host, port, db = mongorc['host'], mongorc['port'], mongorc['db']
            Base.db = Connection(host, port, True, db)


# 必填字段的 default 为 RequireField
class RequireField(object):
    pass


# 必填字段未填时, 抛出的异常为 RequireFieldError
class RequireFieldError(Exception):
    pass


# vim:ts=4:sw=4
