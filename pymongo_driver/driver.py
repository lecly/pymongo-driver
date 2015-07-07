#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from .base import *
from .purify import Purify


class Driver(Base):

    def __init__(self):
        # Base.__init__(self)
        super(Driver, self).__init__()

    def _structure(self):
        '''
        子类必须实现本方法
        '''
        raise NotImplementedError

    def _collection(self):
        '''
        子类必须实现本方法
        '''
        raise NotImplementedError

    def purifier(self, data, complement=True):
        # complement 的含义, 参考 Purify.behavior()
        return Purify(self._structure()).behavior(complement=complement).purifier(data)

    def reformulate(self, data):
        return Purify(self._structure()).reformulate(data)

    def collection(self):
        return self.db[self._collection()]

    def find_by_id(self, _id):
        return self.collection().find_one({'_id': ObjectId(_id)})

    '''
    defined by pymongo.collection:
        find(self, *args, **kwargs)
    '''
    def find(self, *args, **kwargs):
        return self.collection().find(*args, **kwargs)

    '''
    defined by pymongo.collection:
        find_one(self, filter=None, *args, **kwargs)
    '''
    def find_one(self, criteria, *args, **kwargs):
        criteria = self.reformulate(criteria)
        return self.collection().find_one(criteria, *args, **kwargs)

    '''
    defined by pymongo.collection:
        ** DEPRECATED **
        insert(self, doc_or_docs, manipulate=True, check_keys=True, continue_on_error=False, **kwargs):
    '''
    def insert(self, data):
        data = self.purifier(data)
        return self.collection().insert(data)

    '''
    defined by pymongo.collection:
        ** DEPRECATED **
        update(self, spec, document, upsert=False, manipulate=False, multi=False, check_keys=True, **kwargs):
    '''
    def update(self, data, condition=None):
        '''
        update() 只需更新指定字段, 无需取出整个文档
        the criterion is {'_id': ObjectId(_id)}
        '''
        # 尝试通过以下两个步骤找到数据原位
        # 1. 尝试从 data 中直接取出 '_id'
        _id = data.get('_id') if '_id' in data else None
        # 2. 尝试通过 condition 间接找出一条文档的 '_id'
        if not _id and condition:
            _doc = self.find_one(condition)
            _id = _doc.get('_id') if _doc else None
        if not _id:
            return False
        # update() 操作时, 不应对数据源做"自动补全未填字段的默认值"
        # 因为此时的数据源, 可能只涉及到需要修改的字段
        # 未提供的字段, 是不需要修改的, 保留它们在数据库中的值即可, 千万不能"自动补全默认值"
        _only_field_value = True
        for modifier in ('$inc', '$mul', '$rename', '$setOnInsert', '$set', '$unset', '$min', '$max', '$currentDate'):
            if modifier in data:
                data[modifier] = self.purifier(data.get(modifier), complement=False)
                _only_field_value = False
        if _only_field_value:
            data = self.purifier(data, complement=False)
        # print('\nupdate data:\n{0}\n'.format(data))
        return self.collection().update({'_id': _id}, data)

    '''
    defined by pymongo.collection:
        ** DEPRECATED **
        save(self, to_save, manipulate=True, check_keys=True, **kwargs):
    '''
    def save(self, data, condition=None):
        '''
        save() 需要取出整个文档, 然后将新数据应用到文档, 再保存
        save() means: insert() if not exist else update()
        the criterion is {'_id': ObjectId(_id)}
        '''
        # 尝试通过以下两个步骤找到数据原位
        # 1. 尝试从 data 中直接取出 '_id', 并找到原文档
        _id = data.get('_id') if '_id' in data else None
        if _id:
            _doc = self.find_one({'_id': _id})
        # 2. 尝试通过 condition 间接找到原文档
        elif condition:
            _doc = self.find_one(condition)
        _doc = {} if _doc is None else _doc
        # save() 操作时, 不应对数据源做"自动补全未填字段的默认值"
        # 因为此时的数据源, 可能只涉及到需要修改的字段
        # 未提供的字段, 是不需要修改的, 保留它们在数据库中的值即可, 千万不能"自动补全默认值"
        data = self.purifier(data, complement=False)
        # 将新数据应用到原文档
        _doc.update(data)
        # save 原文档
        return self.collection().save(_doc)

    def ensure_exist(self, data, unique_keys=['_id']):
        '''
        ensure_exist() means: insert() if not exist else do nothing
        the criterion is {'unique_keys': unique_keys}
        '''
        _unique_keys = []
        if type(unique_keys) is str:
            _unique_keys.append(unique_keys)
        elif type(unique_keys) is list:
            _unique_keys.extend(unique_keys)
        else:
            raise TypeError('unique_keys must be a str or list instance')
        condition = {}
        for _uk in _unique_keys:
            if _uk not in data:
                raise KeyError("the unique_key '{0}' not in data".format(_uk))
            condition.update({_uk: data.get(_uk)})
        if condition == {}:
            raise KeyError('data or unique_keys error')
        x = self.find_one(condition)
        if not x:
            inserted_id = self.insert(data)
            if not inserted_id:
                return False
            x = self.find_one({'_id': ObjectId(inserted_id)})
        else:
            self.update(data, condition)
            x = self.find_one(condition)
        return x


# vim:ts=4:sw=4
