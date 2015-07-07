#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

_str_field = 789
_int_field = '123'
_float_field = '0.0'
_bool_field = 'x'
_int_field_default_none = None
_tuple_int_field = ('12', '23')
_list_str_field = ['ab', 'bc']


def data_input(unnecessary=False):
    source = {
        'str_field': _str_field,
        'int_field': _int_field,
        'int_field_default_none': _int_field_default_none,
    }
    if unnecessary:
        source['dict_field'] = {}
    return source


def data_output():
    str_field = str(_str_field)
    int_field = int(_int_field)
    float_field = float(_float_field)
    bool_field = bool(_bool_field)
    int_field_default_none = None if _int_field_default_none is None else int(_int_field_default_none)
    tuple_int_field = list(int(i) for i in _tuple_int_field)
    list_str_field = list(str(s) for s in _list_str_field)

    return {
        'str_field': str_field,
        'int_field': int_field,
        'float_field': float_field,
        'bool_field': bool_field,
        'int_field_default_none': int_field_default_none,
        'tuple_int_field': tuple_int_field,
        'list_str_field': list_str_field,
        'dict_field': {},
        'dict_field_nesting': {},
        'list_dict_field': [],
        'list_dict_field_nesting': []
    }


# vim:ts=4:sw=4
