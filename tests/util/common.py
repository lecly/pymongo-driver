#!/usr/bin/env python
# vim: set fileencoding=utf-8 :


import sys
import imp


def load_model(name, path=['model', ]):
    # 尝试从缓存中返回
    try:
        return sys.modules[name]
    except KeyError:
        pass

    fp, pathname, description = imp.find_module(name, path)

    try:
        model = imp.load_module(name, fp, pathname, description)
        class_name = underline_to_camel(name)
        return getattr(model, class_name)
    finally:
        if fp:
            fp.close()


def camel_to_underline(camel_format):
    '''
    驼峰命名格式 -> 下划线命名格式
    '''
    underline_format = ''
    if isinstance(camel_format, str):
        for s in camel_format:
            underline_format += s if s.islower() else '_' + s.lower()
    return underline_format


def underline_to_camel(underline_format):
    '''''
    下划线命名格式 -> 驼峰命名格式
    '''
    camel_format = ''
    if isinstance(underline_format, str):
        for s in underline_format.split('_'):
            camel_format += s.capitalize()
    return camel_format


# vim:ts=4:sw=4
