#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


from pymongo_driver import *


class ComplexCollectionModel(driver.Driver):

    def _structure(self):
        return {
            'str_field': {'type': str, 'default': RequireField},
            'int_field': {'type': int, 'default': RequireField},
            'float_field': {'type': float, 'default': 0.0},
            'bool_field': {'type': bool, 'default': True},
            'int_field_default_none': {'type': int, 'default': None},
            'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
            'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']},
            'dict_field': {'type': dict, 'default': {}, 'items': {
                'str_field': {'type': str, 'default': 'abc'},
                'int_field': {'type': int, 'default': 123},
                'float_field': {'type': float, 'default': 0.0},
                'bool_field': {'type': bool, 'default': True},
                'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
                'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']}
            }},
            'dict_field_nesting': {'type': dict, 'default': {}, 'items': {
                'str_field': {'type': str, 'default': 'abc'},
                'int_field': {'type': int, 'default': 123},
                'float_field': {'type': float, 'default': 0.0},
                'bool_field': {'type': bool, 'default': True},
                'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
                'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']},
                'dict_field': {'type': dict, 'default': {}, 'items': {
                    'str_field': {'type': str, 'default': 'abc'},
                    'int_field': {'type': int, 'default': 123},
                    'float_field': {'type': float, 'default': 0.0},
                    'bool_field': {'type': bool, 'default': True},
                    'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
                    'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']}
                }}
            }},
            'list_dict_field': {'type': list, 'item_type': dict, 'default': [], 'items': [{
                'str_field': {'type': str, 'default': 'abc'},
                'int_field': {'type': int, 'default': 123},
                'float_field': {'type': float, 'default': 0.0},
                'bool_field': {'type': bool, 'default': True},
                'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
                'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']}
            }, ]},
            'list_dict_field_nesting': {'type': list, 'item_type': dict, 'default': [], 'items': [{
                'str_field': {'type': str, 'default': 'abc'},
                'int_field': {'type': int, 'default': 123},
                'float_field': {'type': float, 'default': 0.0},
                'bool_field': {'type': bool, 'default': True},
                'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
                'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']},
                'dict_field': {'type': dict, 'default': {}, 'items': {
                    'str_field': {'type': str, 'default': 'abc'},
                    'int_field': {'type': int, 'default': 123},
                    'float_field': {'type': float, 'default': 0.0},
                    'bool_field': {'type': bool, 'default': True},
                    'tuple_int_field': {'type': tuple, 'item_type': int, 'default': (12, 23)},
                    'list_str_field': {'type': list, 'item_type': str, 'default': ['ab', 'bc']}
                }}
            }, ]}
        }

    def _collection(self):
        return 'test_driven'


# vim:ts=4:sw=4
