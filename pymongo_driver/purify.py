#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from .base import ObjectId, RequireField, RequireFieldError


class Purify:

    '''
    变量中会频繁出现 structure 和 struct
    structure, 用于表示 collection 的结构定义, 是一个整体
    struct, 用于表示 structure 以及其在遍历过程中的递归子元素
    '''
    def __init__(self, structure):
        if not structure:
            raise ValueError('structure is not defined')
        if not isinstance(structure, dict):
            raise TypeError("'structure' must be a dict instance")
        self.structure = structure
        self.behavior()

    def behavior(self, complement=True):
        '''
        complement: 类型为 bool
        当 structure 定义了某个 field 而数据源 data 未提供时, 不论是否 RequireField, 此时有两种处理方式:
            1. insert 时, 应该补全默认值, 对应于 complement == True
            2. update 时, 不要补全默认值, 对应于 complement == False
        '''
        self.complement = complement
        return self

    def purifier(self, data):
        '''
        data: 类型为 dist, 数据源
        '''
        if not data:
            raise ValueError('data is not defined')
        if not isinstance(data, dict):
            raise TypeError("'data' must be a dict instance")
        return self._filter(data, self.structure)

    def reformulate(self, condition={}):
        if not isinstance(condition, dict):
            raise TypeError("'condition' must be a dict instance")
        for field, value in list(condition.items()):
            field_list = field.split('.')
            _struct = self.structure
            # print('condition: {0}\nstructure: {1}'.format(condition, self.structure))
            while field_list:
                # 取出并移除第一个元素
                _field = field_list.pop(0)
                # 针对 tuple, list, dict 取出子节点的结构数据
                if 'items' in _struct:
                    _struct = _struct.get('items')
                # 针对 tuple, list 取出第一个元素的结构数据
                if isinstance(_struct, (tuple, list)):
                    _struct = _struct[0]
                # 脱去一层衣服
                _struct = _struct.get(_field)
                # print('_field: {0}\n_struct: {1}\n'.format(_field, _struct))
                # 衣服已经脱完
                if not field_list:
                    if _field == '_id' and _struct is None:
                        condition[field] = ObjectId(value)
                    else:
                        _type = _struct.get('item_type') if 'item_type' in _struct else _struct.get('type')
                        if _type in (int, str, float, bool, tuple, list, dict, ObjectId):
                            condition[field] = self.conversion(value, _type)
                        else:
                            raise TypeError('"{0}" structure error'.format(field))
        return condition

    def _filter(self, data, struct):
        if data is None:
            return None
        document = {}
        # print('\norig data:\n{0}\nstruct:\n{1}\n'.format(data, struct))
        for _field, _struct in list(struct.items()):
            # print('\ndata: {0}\n_field: {1}\n_struct: {2}'.format(data, _field, _struct))
            # 数据源未提供field
            if _field not in data:
                # self.complement 为 True, 表示需要补全默认值
                if self.complement:
                    document[_field] = self._filter_not_given(_field, _struct)
            # 数据源已提供field
            else:
                document[_field] = self._filter_given(data, _field, _struct)
        return document

    def _filter_not_given(self, field, struct):
        struct_type = struct.get('type')
        struct_default = struct.get('default')
        struct_item_type = struct.get('item_type', None)
        # 必填项, 抛出异常
        if struct_default is RequireField:
            raise RequireFieldError('"{0}" is required'.format(field))
        # 非必填项, 取默认值
        else:
            # tuple, list 都需要以 list 来表示
            if struct_type in (tuple, list):
                if struct_item_type in (int, str, float, bool, dict):
                    return [self.conversion(i, struct_item_type) for i in struct_default]
            else:
                return struct_default

    def _filter_given(self, data, field, struct):
        struct_type = struct.get('type')
        struct_default = struct.get('default')
        struct_item_type = struct.get('item_type', None)
        value = data.get(field, struct_default)
        if struct_type is dict:
            # 如果数据源非空, 或者是必填项, 递归进入子节点
            if data.get(field) != {} or struct_default is RequireField:
                # struct.get('items'), 子元素的struct
                return self._filter(value, struct.get('items'))
            # 否则取默认值
            else:
                return struct_default
        elif struct_type in (int, str, float, bool, ObjectId):
            return self.conversion(value, struct_type)
        elif struct_type in (tuple, list):
            # tuple, list 都需要以 list 来表示
            # 子元素为 dict, 依次取出子节点元素, 递归处理
            if struct_item_type is dict:
                _temp = []
                for _value in value:
                    # struct.get('items')[0], 子元素的struct
                    _temp.append(self._filter(_value, struct.get('items')[0]))
                return _temp
            else:
                if value is None:
                    return None
                if not isinstance(value, (tuple, list)):
                    raise TypeError("'{0}' must be a tuple or list instance".format(field))
                if struct_item_type in (int, str, float, bool):
                    return [self.conversion(i, struct_item_type) for i in value]

    def conversion(self, variable, dst_type):
        # avoid unnecessary conversions
        if variable is None or isinstance(variable, dst_type):
            return variable
        return dst_type(variable)


# vim:ts=4:sw=4
