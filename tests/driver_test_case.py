#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import json
import unittest
from pymongo_driver import *
from util.common import load_model
from data import *


complex_collection_model = load_model('complex_collection_model', ['model'])


class DriverTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 正常数据的测试
    def test_purifier(self):
        self.maxDiff = None
        data = for_purifier.data_input()
        data = complex_collection_model().purifier(data)
        result = for_purifier.data_output()
        self.assertDictEqual(data, result)

    # 最小化数据的测试
    def test_purifier_min(self):
        self.maxDiff = None
        data = for_purifier_min.data_input()
        data = complex_collection_model().purifier(data)
        result = for_purifier_min.data_output()
        self.assertDictEqual(data, result)

    # 最小化数据的测试
    def test_purifier_min_2(self):
        self.maxDiff = None
        data = for_purifier_min.data_input(unnecessary=True)
        data = complex_collection_model().purifier(data)
        result = for_purifier_min.data_output()
        self.assertDictEqual(data, result)

    # 空数据的测试, 抛出异常 ValueError
    def test_purifier_ValueError(self):
        self.maxDiff = None
        data = {}
        self.assertRaises(ValueError, complex_collection_model().purifier, data)

    # 空数据的错误类型测试, 抛出异常 ValueError
    def test_purifier_ValueError_2(self):
        self.maxDiff = None
        data = []
        self.assertRaises(ValueError, complex_collection_model().purifier, data)

    # 必填字段的测试, 必填字段未填时, 抛出异常 RequireFieldError
    def test_purifier_RequireFieldError(self):
        self.maxDiff = None
        data = {'x': 0}
        self.assertRaises(RequireFieldError, complex_collection_model().purifier, data)

    # 错误类型测试, 抛出异常 TypeError
    def test_purifier_TypeError(self):
        self.maxDiff = None
        data = [1, 2, 3]
        self.assertRaises(TypeError, complex_collection_model().purifier, data)

    # 只做数据净化, 不做必填项补全的测试, 提供必填项
    def test_purifier_without_complement_1(self):
        self.maxDiff = None
        data = {'str_field': 789, 'int_field': '123', 'int_field_default_none': None}
        data = complex_collection_model().purifier(data, complement=False)
        result = {'str_field': '789', 'int_field': 123, 'int_field_default_none': None}
        # print('\ndata:\n{0}\n\nresult:\n{1}\n'.format(data, result))
        self.assertDictEqual(data, result)

    # 只做数据净化, 不做必填项补全的测试, 不提供必填项
    def test_purifier_without_complement_2(self):
        self.maxDiff = None
        data = {'float_field': '123.789'}
        data = complex_collection_model().purifier(data, complement=False)
        result = {'float_field': 123.789}
        # print('\ndata:\n{0}\n\nresult:\n{1}\n'.format(data, result))
        self.assertDictEqual(data, result)

    # 只做数据净化, 不做必填项补全的测试, 嵌套的 dist
    def test_purifier_without_complement_3(self):
        self.maxDiff = None
        data = {'dict_field': {'int_field': '123', 'float_field': '123.789'}}
        data = complex_collection_model().purifier(data, complement=False)
        result = {'dict_field': {'int_field': 123, 'float_field': 123.789}}
        # print('\ndata:\n{0}\n\nresult:\n{1}\n'.format(data, result))
        self.assertDictEqual(data, result)

    # 只做数据净化, 不做必填项补全的测试, 嵌套的 复杂的 dist
    def test_purifier_without_complement_4(self):
        self.maxDiff = None
        data = {
            'dict_field_nesting': {
                'tuple_int_field': ('123', '456'),
                'dict_field': {
                    'bool_field': 'abc'
                }
            }
        }
        data = complex_collection_model().purifier(data, complement=False)
        result = {
            'dict_field_nesting': {
                'tuple_int_field': [123, 456],
                'dict_field': {
                    'bool_field': True
                }
            }
        }
        # print('\ndata:\n{0}\n\nresult:\n{1}\n'.format(data, result))
        self.assertDictEqual(data, result)

    # 只做数据净化, 不做必填项补全的测试, 嵌套的 复杂的 空的 dist
    def test_purifier_without_complement_5(self):
        self.maxDiff = None
        data = {
            'dict_field': [],
            'list_str_field': [],
            'dict_field_nesting': {
                'dict_field': {},
                'list_str_field': []
            }
        }
        data = complex_collection_model().purifier(data, complement=False)
        result = {
            'dict_field': {},
            'list_str_field': [],
            'dict_field_nesting': {
                'dict_field': {},
                'list_str_field': []
            }
        }
        # print('\ndata:\n{0}\n\nresult:\n{1}\n'.format(data, result))
        self.assertDictEqual(data, result)

    # 正常数据的测试
    def test_reformulate(self):
        self.maxDiff = None
        data = for_reformulate.data_input()
        data = complex_collection_model().reformulate(data)
        result = for_reformulate.data_output()
        self.assertDictEqual(data, result)


def _test_case():
    unittest.main()


if __name__ == '__main__':
    unittest.main()


# vim:ts=4:sw=4
