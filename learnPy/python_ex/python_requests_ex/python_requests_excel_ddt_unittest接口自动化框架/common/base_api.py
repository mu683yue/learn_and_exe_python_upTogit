#!usr/bin/python3
#-*- coding:utf-8 -*-

"""
1、把excel读取处理的数据作为请求参数，封装requests请求方法，传入请求参数，并返回结果
2、为了不污染测试数据，出报告的时候先将测试的excel赋值到新的excel
3、把测试返回的结果，写入信贷excel文件
"""

import sys
sys.path.append(r"S:\Develop\python_workplace\python_requests_excel_ddt_unittest接口自动化框架")

import json
import requests
from common.readexcel import ExcelUtil
from common.writeexcel import copy_excel,Write_excel


def send_requests(s,testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    #url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    #请求头部headers
    try:
        headers = eval(testdata["headers"])
    except:
        headers = None
    #post请求body类型
    type = testdata["type"]

    test_nub = testdata['id']
    print(f"*******正在执行测试用例:----{test_nub}----*******")
    print(f"请求方式{method}，请求url：{url}")
    print(f"请求params：{params}")

    #post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = { }

    #判断传data数据还是json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post":
        print(f"post请求body类型为：{type},body内容为：{body}")

    verify = False
    res = {} #接受返回数据

    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                    )
        print(f"页面返回信息：{r.content.decode('utf-8')}")
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res['statuscode'] = str(r.status_code)   #状态码转成str
        res['text'] = r.content.decode('utf-8')
        res['times'] = str(r.elapsed.total_seconds()) #接口请求时间转成str
        if res['statuscode'] != '200':
            res['error'] = res['text']
        else:
            res['error'] = ''
        res['msg'] = ''
        if testdata['checkpoint'] in res['text']:
            res['result'] = "pass"
        else:
            res["result"] = "fail"
        return res
    except Exception as e:
        res['msg'] = str(msg)
        return res

def write_result(result,filename="result.xlsx"):
    #返回结果的行数row_nub
    row_nub = result['rowNum']
    #写入statuscode
    wt = Write_excel(filename)
    wt.write(row_nub,8,result['statuscode'])  #写入返回状态
    wt.write(row_nub,9,result['times'])   #耗时
    wt.write(row_nub,10,result['error'])  #状态码非200时的返回信息
    wt.write(row_nub,12,result['result'])  #测试结果pass还是fail
    wt.write(row_nub,13,result['msg'])   #抛异常

if __name__=="__main__":
    data = ExcelUtil("debug_api.xlsx").dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s,data[0])
    copy_excel("debug_api.xlsx","result.xlsx")
    write_result(res,filename="result.xlsx")
        



















    
    
            
