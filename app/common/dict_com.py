# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 21:34:12
# @Author  : lileilei
def comp_dict(dict1,dict2):
    for k,v in dict1.items():
        for k2,v2 in dict2.items():
            if k==k2 and v==v2:
                return True
            else:
                return False
def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(fanhuijson[key])) for key in result.keys()])
        value2=([(str(value)) for value in result.values()])
        if value1==value2:
            return  'pass'
        else:
            return 'fail'
    else:
        raise ('请填写期望值')