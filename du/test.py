# -*- coding:utf8 -*-

'''
    @Author :  pjx
    @File   :  test
    @Time   :  2020/6/19 23:27
'''

import warnings

warnings.filterwarnings("ignore")


data = {"data":{"total":2,"page":0,"productList":[{"requestId":"14ecbd337f3f8e88","page":0,"dataType":0,"productId":67304,"spuId":67304,"propertyValueId":0,"propertyValue":"","logoUrl":"https://china-product.poizon.com/Fuo9pnvKeeFJDtPpYAhnjkzL7chtnew.png","images":["https://china-product.poizon.com/Fuo9pnvKeeFJDtPpYAhnjkzL7chtnew.png"],"title":"Air Jordan 1 Zoom Racer Blue 白蓝 \"小Dior\" 篮球鞋","subTitle":"","spuMinSalePrice":197900,"minSalePrice":197900,"soldNum":25590,"sourceName":"search","price":197900,"broUrl":"https://du.hupucdn.com/news_byte3173byte_5c87bdf672c1b1858d994e281ce5f154_w150h150.png","articleNumber":"CK6637-104","priceType":1,"goodsType":0},{"requestId":"14ecbd337f3f8e88","page":0,"dataType":0,"productId":1001549,"spuId":1001549,"propertyValueId":0,"propertyValue":"","logoUrl":"https://cdn.poizon.com/node-common/7da3a00a248b8504b5b49a4537eee2f0.jpg","images":["https://cdn.poizon.com/node-common/7da3a00a248b8504b5b49a4537eee2f0.jpg"],"title":"Air Jordan 1 High Zoom Air “Zen Green” 黑绿","subTle":"","spuMinSalePrice":136900,"minSalePrice":136900,"soldNum":2236,"sourceName":"search","price":136900,"brandLogoUrl":"https://du.hupucdn.com/news_byte3173byte_5c87bdf672c1b1858d994e281ce5f154_w150h150.png","articleNumber":"CK6637-002","priceType":1,"goodsType":0}],"showHotProduct":0,"screen":{},"isShowGeneral":1,"requestId":"14ecbd337f3f8e88"},"code":200,"status":200,"msg":"ok","error":False}
4

import json
print(data['data']['productList'])

da = input()
print(da)
if da == '':
    print("shuai")
print(type(int(da)))
da_list = str.split(da, ",")
print(da_list)