#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

_bool_field = 'x'
_float_field = '123.45'
_int_field = '123'
_str_field = 789


def data_input():
    source = {
        'bool_field': _bool_field,
        'float_field': _float_field,
        'int_field': _int_field,
        'str_field': _str_field,
    }
    return _data_build(source)


def data_output():
    source = {
        'bool_field': bool(_bool_field),
        'float_field': float(_float_field),
        'int_field': int(_int_field),
        'str_field': str(_str_field),
    }
    return _data_build(source)


def _data_build(source):
    bool_field = source.get('bool_field')
    float_field = source.get('float_field')
    int_field = source.get('int_field')
    str_field = source.get('str_field')

    return {
        'float_field': float_field,
        'tuple_int_field': int_field,
        'list_dict_field.str_field': str_field,
        'list_dict_field_nesting.dict_field.int_field': int_field,
        'list_dict_field_nesting.dict_field.bool_field': bool_field,
        'list_dict_field_nesting.dict_field.list_str_field': str_field,
    }


# vim:ts=4:sw=4
