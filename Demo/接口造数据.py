# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/6}

import requests
from time import sleep
import random

i = 19163
# 获取token值
for m in range(0, 100):
    userEmailNum = ['ceshi888000', 'ceshi888001', 'ceshi888002', 'ceshi888003', 'ceshi888004', 'ceshi888005',
                    'ceshi888006', 'ceshi888007', 'ceshi888008', 'ceshi888009', 'ceshi888010', 'ceshi888011',
                    'ceshi888012', 'ceshi888013', 'ceshi888014', 'ceshi888015', 'ceshi888016', 'ceshi888017',
                    'ceshi888018', 'ceshi888019', 'ceshi888020', 'ceshi888021', 'ceshi888022', 'ceshi888023',
                    'ceshi888024', 'ceshi888025', 'ceshi888026', 'ceshi888027', 'ceshi888028', 'ceshi888029',
                    'ceshi888030', 'ceshi888031', 'ceshi888032', 'ceshi888033', 'ceshi888034', 'ceshi888035',
                    'ceshi888036', 'ceshi888037', 'ceshi888038', 'ceshi888039', 'ceshi888040', 'ceshi888041',
                    'ceshi888042', 'ceshi888043', 'ceshi888044', 'ceshi888045', 'ceshi888046', 'ceshi888047',
                    'ceshi888048', 'ceshi888049']
    # userEmailNum = ['ceshi999000', ]
    for j in range(len(userEmailNum)):
        url = 'http://10.2.22.130:9998';
        header = {"Content-Type": "application/json;charset=UTF-8"}
        payload1 = {"userEmailNum": userEmailNum[j], "password": "913c47b5b7410471ab65f6be9026bbb2",
                    "companyCode": "400"}
        loginresponse = requests.post(url + '/detect/api/auth/tokens', headers=header, json=payload1)
        print(loginresponse.text)
        # print(loginresponse.status_code)
        # print(loginresponse.elapsed.total_seconds())
        token = loginresponse.json()['data']
        # print(token)

        # 添加订单
        header1 = {"Content-Type": "application/json;charset=UTF-8", "Authorization": "Bearer " + token}
        for k in range(0, 6):
            print(i)
            payload2 = {
                "materialIdAndCodeDTO": {
                    "innerMaterialCode": "13002239",
                    "id": "0027816a973b4a21a477da7f74dd74e0"
                },
                "customerMaterialCode": "50114164",
                "innerMaterialCode": "",
                "materialName": "压缩机组件QXT-B121(高性能)",
                "materialTypeName": "包装纸托",
                "materialTypeCode": "500029",
                "customerName": "珠海格力电器股份有限公司",
                "customerCode": "400",
                "customerId": 22,
                "customerOrderNum": "",
                "innerOrderNum": "nbDD" + str(i).zfill(6),
                "preproductionDate": "2021-05-28 00:00:00",
                "orderQuantity": random.randint(4, 500),
                "productLineId": 78,
                "productLineName": "K5",
                "imageNumber": "(50539L)N4.BX000003",
                "productModel": None,
                "materialId": "0027816a973b4a21a477da7f74dd74e0"
            }
            r1 = requests.post(url + '/detect/basicmaintenance/order/add', headers=header1, json=payload2)
            print(r1.text)
            i = i + 1
