# import execjs
# import requests
import pandas as pd
import pendulum

# headers = {
#     'Host': "app.poizon.com",
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
#                   " Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI "
#                   "MiniProgramEnv/Windows WindowsWechat",
#     'appid': "wxapp",
#     'appversion': "4.4.0",
#     'content-type': "application/x-www-form-urlencoded",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept': "*/*",
# }


# def get_recensales_list_url(lastId, productId):
#     # 最近购买接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         sign = ctx.call('getSign',
#                         'lastId{}limit20productId{}sourceAppapp19bc545a393a25177083d4a748807cc0'.format(lastId,
#                                                                                                         productId))
#         recensales_list_url = 'https://app.poizon.com/api/v1/h5/product/fire/recentSoldList?' \
#                               'productId={}&lastId={}&limit=20&sourceApp=app&sign={}'.format(productId, lastId, sign)
#         return recensales_list_url


# def get_search_by_keywords_url(page, sortMode, sortType):
#     # 关键词搜索商品接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         # 53489
#         sign = ctx.call('getSign',
#                         'limit20page{}sortMode{}sortType{}titleajunionId19bc545a393a25177083d4a748807cc0'.format(page,
#                                                                                                                  sortMode,
#                                                                                                                  sortType))
#         search_by_keywords_url = 'https://app.poizon.com/api/v1/h5/product/fire/search/list?title=aj&page={}&sortType={}&sortMode={}&' \
#                                  'limit=20&unionId=&sign={}'.format(page, sortType, sortMode, sign)
#         return search_by_keywords_url


# def get_brand_list_url(lastId, tabId):
#     # 商品品类列表接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         sign = ctx.call('getSign',
#                         'lastId{}limit20tabId{}19bc545a393a25177083d4a748807cc0'.format(lastId, tabId))
#         brand_list_url = 'https://app.poizon.com/api/v1/h5/index/fire/shoppingTab?' \
#                          'tabId={}&limit=20&lastId={}&sign={}'.format(tabId, lastId, sign)
#         return brand_list_url


# def get_product_detail_url(productId):
#     # 商品详情接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         sign = ctx.call('getSign',
#                         'productId{}productSourceNamewx19bc545a393a25177083d4a748807cc0'.format(productId))
#         product_detail_url = 'https://app.poizon.com/api/v1/h5/index/fire/flow/product/detail?' \
#                              'productId={}&productSourceName=wx&sign={}'.format(productId, sign)
#         return product_detail_url


# recensales_list_url = get_recensales_list_url(0, 40755)
# search_by_keywords_url = get_search_by_keywords_url(0, 1, 0)
# brand_list_url = get_brand_list_url(1, 4)
# product_detail_url = get_product_detail_url(53489)
# recensales_list_response = requests.get(url=recensales_list_url, headers=headers)
# search_by_keywords_response = requests.get(url=search_by_keywords_url, headers=headers)
# brand_list_response = requests.get(url=brand_list_url, headers=headers)
# product_detail_response = requests.get(url=product_detail_url, headers=headers)
# print(recensales_list_response.text)
# print(search_by_keywords_response.text)
# print(brand_list_response.text)
# print(product_detail_response.text)
# import execjs
import requests
import hashlib
from urllib.parse import quote
import json

# headers = {
#     'Host': "app.poizon.com",
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
#                   " Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI "
#                   "MiniProgramEnv/Windows WindowsWechat",
#     'appid': "wxapp",
#     'appversion': "4.4.0",
#     'content-type': "application/x-www-form-urlencoded",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept': "*/*",
# }
#
#
# def get_recensales_list_url(lastId, productId):
#     # 最近购买接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         sign = ctx.call('getSign',
#                         'lastId{}limit20productId{}sourceAppapp19bc545a393a25177083d4a748807cc0'.format(lastId,
#                                                                                                         productId))
#         recensales_list_url = 'https://app.poizon.com/api/v1/h5/product/fire/recentSoldList?' \
#                               'productId={}&lastId={}&limit=20&sourceApp=app&sign={}'.format(productId, lastId, sign)
#         return recensales_list_url
#
#
# def get_search_by_keywords_url(page, sortMode, sortType):
#     # 关键词搜索商品接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         # 53489
#         sign = ctx.call('getSign',
#                         'limit20page{}sortMode{}sortType{}titleajunionId19bc545a393a25177083d4a748807cc0'.format(page,
#                                                                                                                  sortMode,
#                                                                                                                  sortType))
#         search_by_keywords_url = 'https://app.poizon.com/api/v1/h5/product/fire/search/list?title=aj&page={}&sortType={}&sortMode={}&' \
#                                  'limit=20&unionId=&sign={}'.format(page, sortType, sortMode, sign)
#         return search_by_keywords_url
#
#
# def get_brand_list_url(lastId, tabId):
#     # 商品品类列表接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         sign = ctx.call('getSign',
#                         'lastId{}limit20tabId{}19bc545a393a25177083d4a748807cc0'.format(lastId, tabId))
#         brand_list_url = 'https://app.poizon.com/api/v1/h5/index/fire/shoppingTab?' \
#                          'tabId={}&limit=20&lastId={}&sign={}'.format(tabId, lastId, sign)
#         return brand_list_url
#
#
# def get_product_detail_url(productId):
#     # 商品详情接口
#     with open('sign.js', 'r', encoding='utf-8')as f:
#         all_ = f.read()
#         ctx = execjs.compile(all_)
#         sign = ctx.call('getSign',
#                         'productId{}productSourceNamewx19bc545a393a25177083d4a748807cc0'.format(productId))
#         product_detail_url = 'https://app.poizon.com/api/v1/h5/index/fire/flow/product/detail?' \
#                              'productId={}&productSourceName=wx&sign={}'.format(productId, sign)
#         return product_detail_url
#
#
# recensales_list_url = get_recensales_list_url(0, 40755)
# search_by_keywords_url = get_search_by_keywords_url(0, 1, 0)
# brand_list_url = get_brand_list_url(1, 4)
# product_detail_url = get_product_detail_url(53489)
# recensales_list_response = requests.get(url=recensales_list_url, headers=headers)
# search_by_keywords_response = requests.get(url=search_by_keywords_url, headers=headers)
# brand_list_response = requests.get(url=brand_list_url, headers=headers)
# product_detail_response = requests.get(url=product_detail_url, headers=headers)
# print(recensales_list_response.text)
# print(search_by_keywords_response.text)
# print(brand_list_response.text)
# print(product_detail_response.text)
headers = {
    'Host': "app.poizon.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI "
                  "MiniProgramEnv/Windows WindowsWechat",
    'appid': "wxapp",
    'appversion': "4.4.0",
    'content-type': "application/json",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept': "*/*",
}

index_load_more_url = 'https://app.poizon.com/api/v1/h5/index/fire/index'
# {"sign":"5e22051c5156608a85b12d501d615c61","tabId":"","limit":20,"lastId":1}
recensales_load_more_url = 'https://app.poizon.com/api/v1/h5/commodity/fire/last-sold-list'
# {"sign":"f44e26eb08becbd16b7ed268d83b3b8c","spuId":"73803","limit":20,"lastId":"","sourceApp":"app"}
product_detail_url = 'https://app.poizon.com/api/v1/h5/index/fire/flow/product/detail'
# {"sign":"5721d19afd7a7891b627abb9ac385ab0","spuId":"49413","productSourceName":"","propertyValueId":"0"}
category = {"code": 200, "msg": "success", "data": {
    "list": [{"catId": 0, "catName": "品牌"}, {"catId": 1, "catName": "系列"}, {"catId": 3, "catName": "球鞋"},
             {"catId": 6, "catName": "潮搭"}, {"catId": 8, "catName": "手表"}, {"catId": 1000119, "catName": "配件"},
             {"catId": 7, "catName": "潮玩"}, {"catId": 9, "catName": "数码"}, {"catId": 1000008, "catName": "家电"},
             {"catId": 726, "catName": "箱包"}, {"catId": 587, "catName": "美妆"}, {"catId": 945, "catName": "家居"}]},
            "status": 200}
doCategoryDetail = {"code": 200, "msg": "success", "data": {"list": [{"brand": {"goodsBrandId": 144,
                                                                                "brandName": "Nike", "type": 0,
                                                                                "logoUrl": "https://du.hupucdn.com/news_byte3724byte_94276b9b2c7361e9fa70da69894d2e91_w150h150.png"},
                                                                      "seriesList": []}, {"brand": {"goodsBrandId": 13,
                                                                                                    "brandName": "Jordan",
                                                                                                    "type": 0,
                                                                                                    "logoUrl": "https://du.hupucdn.com/news_byte3173byte_5c87bdf672c1b1858d994e281ce5f154_w150h150.png"},
                                                                                          "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 3,
                                                                                   "brandName": "adidas", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24108byte_fc70f4c88211e100fe6c29a6f4a46a96_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 494,
                                                                                   "brandName": "adidas originals",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24706byte_9802f5a4f25e6cd1b284a5b754cec4f0_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 439,
                                                                                   "brandName": "Supreme", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte6426byte_c7ab640bf99963bfc2aff21ca4ff8322_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 79,
                                                                                   "brandName": "GUCCI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25670byte_c9ca8b5347750651bebbf84dd7d12d01_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10359,
                                                                                   "brandName": "Fear of God",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte17196byte_d5f7a627b65e90f6b850b613c14b54a2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10176,
                                                                                   "brandName": "LOUIS VUITTON",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte33190byte_d14f21356f020e12a534b967be2bed77_w382h322.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1245,
                                                                                   "brandName": "OFF-WHITE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte2408byte_4d329f274512ddb136989432292cdd3f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 45,
                                                                                   "brandName": "THE NORTH FACE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte31268byte_e05935a55a37e7901640f7d09548499d_w151h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10082,
                                                                                   "brandName": "FOG", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23329byte_3e247b5d598f7da36a1af24d08cb9ad8_w350h350.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10215,
                                                                                   "brandName": "STONE ISLAND",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24302byte_570d51bb8c62233c3b52a9ffb05e5d74_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10223,
                                                                                   "brandName": "HERMES", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30429byte_658ec36fbe99d2b3ae1e5a685ee1b20c_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10370,
                                                                                   "brandName": "Jimmy Choo", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte18060byte_e664bd98b2a590c464e0e154b5f9ce53_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1310,
                                                                                   "brandName": "Champion", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21403byte_6995f22e76a1a203f4f4dfd3ff43c21b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 176,
                                                                                   "brandName": "Converse", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte8272byte_078b04a261c1bb1c868f1522c7ddcefc_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 2,
                                                                                   "brandName": "Puma", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26564byte_a768870ae48f1a216dd756c2206c34b1_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 4,
                                                                                   "brandName": "New Balance",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte6189byte_1cb7717a44b335651ad4656610142591_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 7,
                                                                                   "brandName": "Under Armour",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21646byte_0bd049d8c27c8509f3166d68a388dfe9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 9,
                                                                                   "brandName": "Vans", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte9507byte_49aaeb534cecab574949cf34b43da3a5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 33,
                                                                                   "brandName": "李宁", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte7350byte_d60fa387aac42cb8c9b79700d720397d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 4981,
                                                                                   "brandName": "JRs", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte5113byte_7a651984f882e48df46c67758d6934d2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10027,
                                                                                   "brandName": "Dickies", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte37984byte_e8d6f32f6b17f736a422fac90c99d7e5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10113,
                                                                                   "brandName": "ANTI SOCIAL SOCIAL CLUB",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28476byte_863a194b02da977009144bd9f10dde1f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 843,
                                                                                   "brandName": "CASIO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte4156byte_4d3d1a6e2beca7f700e1ac92ea6b2fdf_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10141,
                                                                                   "brandName": "UNDEFEATED", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte16826byte_6d7166e0081d6b42619e54ca06900406_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10250,
                                                                                   "brandName": "NINTENDO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte29039byte_b5b91acfeaf88ec0c76df08b08e6e5cd_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10001,
                                                                                   "brandName": "Thrasher", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30750byte_446d35e36b912ad366d8f72a6a9cc5e4_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10021,
                                                                                   "brandName": "Cav Empt", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte61774byte_7a5969f3694fc71f727c63e8bc3d95d5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10032,
                                                                                   "brandName": "Burberry", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27771byte_9031f22329273c84170de8aa0f7d7c67_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10037,
                                                                                   "brandName": "C2H4", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte42973byte_8681e3b6092a4dbf6938621cb28e75f4_w284h284.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10043,
                                                                                   "brandName": "Mitchell & Ness",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte35794byte_37e1d65f0c9df1c61c217bded6435b9d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10046,
                                                                                   "brandName": "Moncler", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27878byte_9066687c9718c1168f8846653018a935_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1860,
                                                                                   "brandName": "THOM BROWNE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte7866byte_fc0d1f01af88a3425bb106fe21f720a9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10062,
                                                                                   "brandName": "VLONE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte38175byte_da7a862bd765220eb9bb00efbf5cfab3_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10072,
                                                                                   "brandName": "HUAWEI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte53433byte_8949768c520c73adfd0798c7416ff642_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10073,
                                                                                   "brandName": "Canada Goose",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte40959byte_26901c3ba55661a1ea668d49c599e86b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1131,
                                                                                   "brandName": "隐蔽者", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28746byte_5a165d2728e81983d7bbd59739e56b97_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10095,
                                                                                   "brandName": "FMACM", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21768byte_8480a963cd231f2ea4ec032753238cd9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10098,
                                                                                   "brandName": "Onitsuka Tiger",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27415byte_63662423bde0d02cb8576ff47afb270d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10103,
                                                                                   "brandName": "Guuka", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte29973byte_ef6eeef0535a0c9b2ade4fb6efc0aa06_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 634,
                                                                                   "brandName": "A BATHING APE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte8375byte_cedf2c6ad46d2ac60f0c2f86cbccffcd_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10115,
                                                                                   "brandName": "Mishkanyc", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte34270byte_f4816f6a78ea1e528144fadcaf671db6_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10119,
                                                                                   "brandName": "AMBUSH", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22861byte_44dadd412d9c0b3c57f0d382f5554f5c_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10120,
                                                                                   "brandName": "CDG Play", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30859byte_4b1af0b2a9bc9007a3f0c5385fea1f8d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10164,
                                                                                   "brandName": "GOTNOFEARS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22932byte_c11b6cb93dc1f26ee98d44db6017c522_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10172,
                                                                                   "brandName": "THE NORTH FACE PURPLE LABEL",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22025byte_ce1dc9be1690240e01f1365eedac1362_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10186,
                                                                                   "brandName": "Subcrew", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23252byte_48b6f7f61cad6c18fb7adafe9696ef1f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10243,
                                                                                   "brandName": "Aftermaths", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20974byte_9b01f95cba8e542a258ccc7f1ccf9647_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10248,
                                                                                   "brandName": "Aape", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte34614byte_beb0b973078c0e17171edea6cd0c715d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10263,
                                                                                   "brandName": "apm monaco", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28592byte_384295707fe8076c1cc738402f3b928b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 6,
                                                                                   "brandName": "Reebok", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte8192byte_cda902674ee7d4d4c51d32b834a76e7b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10264,
                                                                                   "brandName": "DUEPLAY", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20052byte_41e361c6d2df6895d3b38dfdd9c2efa9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 577,
                                                                                   "brandName": "PALACE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte8691byte_5577b630f2fd4fcb8d6f7f45071acc40_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10000,
                                                                                   "brandName": "ROARINGWILD",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21733byte_bf73cc451933ed2392d31620c08f76d6_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1222,
                                                                                   "brandName": "NOAH", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte33752byte_11638ecd79b8d3c7fd29b92dfb9f5f5b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10030,
                                                                                   "brandName": "Carhartt WIP",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte9975byte_222768bbe7d7daffed18c85090de6153_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10298,
                                                                                   "brandName": "BANU", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24263byte_c480365559a6a9808a69547bc8084579_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10357,
                                                                                   "brandName": "EQUALIZER", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte18391byte_b300fb77b24a776296bc7a92873d1839_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10075,
                                                                                   "brandName": "RIPNDIP", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte35669byte_5e1b7e4e57ee4568bfb9bf657c8146c5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10087,
                                                                                   "brandName": "Stussy", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30589byte_c37b4863d6248dd92a588696c9e1dfe5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10092,
                                                                                   "brandName": "NPC", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte5399byte_249e0a587b457f46e7e6bad9fd7234bc_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10118,
                                                                                   "brandName": "Red Charcoal",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte19757byte_91817a270103c441138260ad9812f1d8_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10106,
                                                                                   "brandName": "Dior", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21672byte_cfe86702e27c9870189b6ad6a7f795b8_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 65,
                                                                                   "brandName": "Apple", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte1253byte_c8fcc08b731e30d4d1453c77bb4417d7_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10039,
                                                                                   "brandName": "Randomevent",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22681byte_d422ea97ad63fe2718dc0a3208602adb_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10260,
                                                                                   "brandName": "Swarovski", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte29555byte_630db5e96d66e6f5287c293cd78caf27_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10010,
                                                                                   "brandName": "PRADA", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21018byte_f70b725f896e7d48d7cf5de27efb693a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10107,
                                                                                   "brandName": "UNIQLO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22384byte_3363df740785c4f46ff7e9e60732d44c_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10173,
                                                                                   "brandName": "HIPANDA", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30445byte_c66a18c65a8fed91a6790c51b4742f5a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10219,
                                                                                   "brandName": "HUMAN MADE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte37800byte_decdf76555f22cb831ac23e08ab2018b_w150h150.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10348,
                                                                                   "brandName": "PINKO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21540byte_a15095f6f394d948ae5ab220d8d1a122_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10349,
                                                                                   "brandName": "ISSEY MIYAKE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21345byte_f151d2b6a79e5f9189d3edeb5febd68d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10094,
                                                                                   "brandName": "HERON PRESTON",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21445byte_263c6af2c24fe8eb020f2fad8956aae6_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10217,
                                                                                   "brandName": "HARSH AND CRUEL",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27648byte_68693ca8aa0d93a7bc4efacf7131a1d0_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10229,
                                                                                   "brandName": "COACH", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22573byte_2d963bacc8403d3bff0f44edd04dab64_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10230,
                                                                                   "brandName": "MICHAEL KORS",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21530byte_ae96688098a3d529824fa5cb71bf3765_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10273,
                                                                                   "brandName": "XLARGE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte38276byte_061c84c498eadd44eb11704a5420f785_w688h628.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10012,
                                                                                   "brandName": "Balenciaga", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25051byte_c9098ab23afe7e5b2ebbe5bbe02cf20b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10097,
                                                                                   "brandName": "New Era", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte12037byte_2650d81fe891a08f41ba8ef58f92e4c8_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10236,
                                                                                   "brandName": "UNDER GARDEN",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21683byte_ebeac156f070e9f48e74e13567a908ad_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10216,
                                                                                   "brandName": "Suamoment", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26349byte_999d4032e637fbccca3aaf6db95ef2ea_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 8,
                                                                                   "brandName": "Asics", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte3352byte_31e3a9553fef833c3004a84c4c016093_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10261,
                                                                                   "brandName": "TIFFANY & CO.",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21293byte_6af55972221b24da968a1b9957080c1e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10045,
                                                                                   "brandName": "CHANEL", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte32784byte_b947def32e782d20594230896ad2b342_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10302,
                                                                                   "brandName": "alexander wang",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20702byte_4635ead9077fefadaf9875638452a339_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10347,
                                                                                   "brandName": "MLB", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21412byte_ba8096a44748f1e896828a6d1196f571_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10191,
                                                                                   "brandName": "BEASTER", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23781byte_319f230d9345cd5154b908631d2bb868_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10245,
                                                                                   "brandName": "izzue", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21393byte_cf5140071b8824d433f4b32a51d49220_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10257,
                                                                                   "brandName": "FIVE CM", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22092byte_3cd80b1e49ad6bd28e5e371327424532_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10262,
                                                                                   "brandName": "Acne Studios",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26766byte_8e0cc00c1fccd1958d56b008370107cc_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 4984,
                                                                                   "brandName": "得物", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte1528byte_5fd1d0d6bd3ff23d2b6c0d2933da1b8e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10235,
                                                                                   "brandName": ":CHOCOOLATE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21808byte_2418d1805f60850c961c31ea40982ed2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10096,
                                                                                   "brandName": "PALM ANGELS",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22102byte_3d85af8f2d0566d7a1620404f9432be5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1302,
                                                                                   "brandName": "WTAPS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte5814byte_ce947464a6105c6aef7d7fb981aaa61e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 4983,
                                                                                   "brandName": "NEIGHBORHOOD",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte3804byte_316eb37426516d3cf8252fcbab6aa0cf_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10024,
                                                                                   "brandName": "BANDAI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte41491byte_d575b1bce5ab5754ea2444c0bb415782_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 2389,
                                                                                   "brandName": "LEGO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte33157byte_7e92ea9e2640626b9d52ce2a9fd2a75c_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10224,
                                                                                   "brandName": "DANGEROUSPEOPLE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27331byte_fd65dfa6630e179a1bed93573a9b32cb_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10241,
                                                                                   "brandName": "Acupuncture",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26897byte_26ec3a3b2f532353a635cff0752eb743_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10255,
                                                                                   "brandName": "MITARBEITER（IN）",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21741byte_058a1342e063fbb9fd341a1f3aca48a6_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1318,
                                                                                   "brandName": "FILA", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24479byte_79cb074cf3d73a420d75a435aee91fe2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10315,
                                                                                   "brandName": "SANKUANZ", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23445byte_3e251bad0695be109b037d80b9908e2a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10221,
                                                                                   "brandName": "*EVAE+MOB", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22561byte_e52e3571b938f7027d4ea5ce1c406cb8_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10226,
                                                                                   "brandName": "BABAMA", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23766byte_8a0dcd76a4e7032a66209f40d0b6ec85_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10228,
                                                                                   "brandName": "OMTO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23242byte_06cc9e12bd4efdf4d1885c401c224e10_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10237,
                                                                                   "brandName": "OMT", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24518byte_6be637e798e477e8c2e9e7d502e59b25_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10244,
                                                                                   "brandName": "VERAF CA", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22401byte_7c150e55199eb32e12bb29f01ed6c801_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 34,
                                                                                   "brandName": "安踏", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte925102byte_5d9ca8cebc2286d70ef66f4f4a8f2983_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10210,
                                                                                   "brandName": "CDG", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20964byte_54ad49c012c262b02805451b9462f481_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10369,
                                                                                   "brandName": "× × DESIGN", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21649byte_f3502bde5ec295493f6b1ffff54fdad9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10017,
                                                                                   "brandName": "PLACES+FACES",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22034byte_87c416321487ad3071b2e886690b6c83_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10020,
                                                                                   "brandName": "VERSACE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte17169byte_7a363914e3e65ddcab341f2088451861_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10022,
                                                                                   "brandName": "LONGINES", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte3779byte_b43ce49900670dcd8855801cd4ecbc3e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10029,
                                                                                   "brandName": "McQ", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20529byte_0a3c77e055b5ea67e5dd976e0ae15ef9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10031,
                                                                                   "brandName": "Alpha Industries",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte10726byte_a964cf670ceeb6e83dd7dc74670d2d0e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10033,
                                                                                   "brandName": "Hasbro", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte33084byte_6ee0b3af2fe9007bd43d7e43b2d9cbcd_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10048,
                                                                                   "brandName": "Boy London", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte12032byte_dc8badd06954530bab52bee2dcd2281e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10053,
                                                                                   "brandName": "MOSCHINO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte3922byte_e6fed7cc9d76aaed983119b1f6ea4da2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10099,
                                                                                   "brandName": "VEJA", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27380byte_01358f743e3668ee4f860cc03c6cee71_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10105,
                                                                                   "brandName": "GAON", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24582byte_5dc995e735d926f10686a3b2e4f99ffe_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10110,
                                                                                   "brandName": "EDCO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25568byte_4c07bb13aeb5e88d127f5f30b0582ed2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10111,
                                                                                   "brandName": "FYP", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24609byte_694a64457745672bd4e7b657b6753993_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10125,
                                                                                   "brandName": "OPPO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25629byte_7fb979a04f572beaa96b0583f4204748_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10130,
                                                                                   "brandName": "Corade", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte5181byte_7a202830db26f4d93c565e2cc1e0af4d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10132,
                                                                                   "brandName": "MostwantedLab",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21748byte_4c88547590072659de8e0731fef96a4f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10135,
                                                                                   "brandName": "PRBLMS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22576byte_910768509dbfed23275fa7989753dffd_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10138,
                                                                                   "brandName": "zippo", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28711byte_8d40191080a1a21111d66ce2ee000e90_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10142,
                                                                                   "brandName": "UNVESNO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte2826byte_fdb1b1046cae382cfb60cac11f9b281d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10150,
                                                                                   "brandName": "vivo", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26242byte_b829524880093cc2099d470299889c89_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10246,
                                                                                   "brandName": "HOKA ONE ONE",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26308byte_1e82701c70c29b871b630adb45dbebd3_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10247,
                                                                                   "brandName": "KEEN", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30591byte_670bf1d37ce8479f3fa09a55d28dcb93_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10002,
                                                                                   "brandName": "Y-3", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte29394byte_2f32b853acb651e2831f8797fe29fbfa_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10267,
                                                                                   "brandName": "LOCCITANE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25047byte_c8480c6f2b9a32fc3a54524146bd1165_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10013,
                                                                                   "brandName": "Neil Barrett",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte3026byte_cdeab7bf75187f17fa8c069c9a3a051a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10269,
                                                                                   "brandName": "Charlotte Tilbury ",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23124byte_0113ad2025780a77a7f5131571ecee54_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10014,
                                                                                   "brandName": "KENZO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte7359byte_c71c56a9aea36427f7bb106f18151548_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10270,
                                                                                   "brandName": "BVLGARI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22644byte_9dfd426ffa4b796999f49447b6a67f13_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10271,
                                                                                   "brandName": "Jo Malone London",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22269byte_51fd61cb797b6c2bbf0c0b84981c0948_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10016,
                                                                                   "brandName": "Vetements", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24790byte_b66758a5ea903a5a005798f7d84d1498_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10274,
                                                                                   "brandName": "GIORGIO ARMANI",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21786byte_2857737687e9338787e5121b81e2fe27_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10019,
                                                                                   "brandName": "Givenchy", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23368byte_51dcde3cd1f5ef90c5734249bcd17af0_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10275,
                                                                                   "brandName": "GUERLAIN", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21952byte_b06c9655af8bbd85bbacd7905c856d99_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10276,
                                                                                   "brandName": "Fresh", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte29422byte_c362cefc52c99839bbf299bef133e165_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10277,
                                                                                   "brandName": "Clé de Peau Beauté",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24675byte_c3c1c3b08d7926e82fd1681f920a955f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10278,
                                                                                   "brandName": "LANCOME", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22324byte_41fe4c8042bfd4761df3cbde50eb1ab0_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10023,
                                                                                   "brandName": "FENDI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte3735byte_363b11ad1f4b34f6b165818fe14ded88_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10279,
                                                                                   "brandName": "Kiehls", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22486byte_39f44b549295514934db3bea8696551a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10280,
                                                                                   "brandName": "MAC", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20822byte_0d14fc90e743b48c0d198505ac7acbbd_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10026,
                                                                                   "brandName": "Yves Saint Laurent",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte29430byte_88593ab0095ed38806e07d4afd4889cf_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10282,
                                                                                   "brandName": "LA MER", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21643byte_c2302d6ae27f2fa9569a224a49da3097_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10284,
                                                                                   "brandName": "CLARINS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23308byte_a69c3dfc25e7a7c6400ffe44d8242a30_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10285,
                                                                                   "brandName": "NARS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25821byte_311c624a310303b590d5d4c062f056ea_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10286,
                                                                                   "brandName": "benefit", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25499byte_f2dadfa1b21c81b9e659300bf07e8d37_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10287,
                                                                                   "brandName": "GLAMGLOW", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22830byte_eb7b37c9e623fc1b2ee13c291e1a29aa_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10288,
                                                                                   "brandName": "Too Faced", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22156byte_47dd9a1fe0969e1648e912ee16cbb844_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10289,
                                                                                   "brandName": "URBAN DECAY",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21218byte_dc1d505013e356a3479ad5295b6f1e75_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10290,
                                                                                   "brandName": "FOREO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20670byte_924d6ad6b63fda5c7dae0c77b6e55a3f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10035,
                                                                                   "brandName": "Dyson", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28101byte_18fa7633c4e27f221c840813d784080f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10291,
                                                                                   "brandName": "Christian Louboutin",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24594byte_d45524f35597ed91bbd7544f9e652172_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10293,
                                                                                   "brandName": "xVESSEL", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23132byte_cc28fa998fb6243eb71054f6c2135db9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10044,
                                                                                   "brandName": "TISSOT", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte31626byte_d4191837d926ec7bbd1e29c5fe46e595_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10300,
                                                                                   "brandName": "PRIME 1 STUDIO",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21836byte_44d1b5dc422073743a3c11647a8409a3_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10047,
                                                                                   "brandName": "MCM", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte50051byte_3ed4a130ff4dc02151428c3e50978942_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10310,
                                                                                   "brandName": "acme de la vie",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22262byte_a8a932aaedbab86b34249828b7ed32f8_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10311,
                                                                                   "brandName": "BE@RBRICK", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23466byte_2e8da4a1f054a8e4682594a45612814e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10065,
                                                                                   "brandName": "Timberland", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25895byte_88b2058d896df08f73cd94a47d2310f2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1000018,
                                                                                   "brandName": "RAF SIMONS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/FkYorY5yQT4Q4E66tjPrzETZ7R-p"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10068,
                                                                                   "brandName": "PANERAI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte32912byte_36220760228f319bb75f52330c7e4b3e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1000020,
                                                                                   "brandName": "正负零", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/FsrWiDmNZYaV1MjkRu0KMGU065zO"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10069,
                                                                                   "brandName": "MIDO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26922byte_be1c2be794cb6d454620f4692647e268_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10070,
                                                                                   "brandName": "Dupont", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28213byte_3d762e61d0d0ab8dec7d7dd92fe1dc99_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10071,
                                                                                   "brandName": "kindle", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27862byte_be5d55c9c358e569b89fbf8e12fc20a4_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10331,
                                                                                   "brandName": "WHY PLAY", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte28380byte_363531321a5e823c56cc2f933f3be497_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10078,
                                                                                   "brandName": "Logitech", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21472byte_ce700f9b3ca84b7a4a5f308f82bae04e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10341,
                                                                                   "brandName": "anello", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25573byte_8080b45548c4b17bc976f8797ff158d5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1000045,
                                                                                   "brandName": "DMCkal", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/FtcBWuRAZXH8rxoRoJSQDhQID6sT"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10350,
                                                                                   "brandName": "A-COLD-WALL*",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte17623byte_ebcbe70f089dabe23e93588dc6ac66a3_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10354,
                                                                                   "brandName": "CONKLAB", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21404byte_7fb50713eb0f986354735b304d5be896_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10101,
                                                                                   "brandName": "GENANX/闪电", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte33425byte_c27fb3124848c48aee19c85441352048_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10358,
                                                                                   "brandName": "FOOT INDUSTRY",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20338byte_4e3b752398bf7ff9e16d9fe37e4ecee9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10360,
                                                                                   "brandName": "BONELESS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte17690byte_8c346bdce381e0cf63c76f187a4fe042_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10361,
                                                                                   "brandName": "umamiism", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22545byte_34df2f448a017f7fdb3e570606c241b9_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10362,
                                                                                   "brandName": "华人青年", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22601byte_f52dc5ab9f4452f97babc47821d24021_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10363,
                                                                                   "brandName": "FUNKMASTERS",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21027byte_1576a0f677e9cacd8762be6db99d4c78_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1000061,
                                                                                   "brandName": "GUESS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/Fi6tDRWTi5rnQiW-ZB5BB-FbPoZN"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 1000062,
                                                                                   "brandName": "Needles", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/FiwdfFP76yqpag1r50r1qVG-TXad"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10368,
                                                                                   "brandName": "Subtle", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21987byte_4b242f882bf5df63b2da5eae632fa29c_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10116,
                                                                                   "brandName": "EMPORIO ARMANI",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22342byte_7060a8a9b7c6b335143673f5417a1944_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10124,
                                                                                   "brandName": "AMONSTER", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/FjZYBGDKtsc_9n8ftq28XsMRxZxB"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10381,
                                                                                   "brandName": "PCMY", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21692byte_205236932bf037dab9965dd2be87085e_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10127,
                                                                                   "brandName": "Rothco", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24098byte_12c50dcd1c1044fa4a6335bedd98e7d4_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10131,
                                                                                   "brandName": "THE WIZ", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte6823byte_6a92589a3c42dcb6a1f3e849966daf53_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10388,
                                                                                   "brandName": "TSMLXLT", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20983byte_d18f9145f160a5dd3b5d0ca45acec510_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10390,
                                                                                   "brandName": "TRICKCOO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25337byte_823a55d69768b65e728f896971a0185d_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10391,
                                                                                   "brandName": "NOCAO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22420byte_91b1ed0e11d4948a817f5ae35a0bfd99_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10136,
                                                                                   "brandName": "PROS BY CH", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte6186byte_323eba7633b20d61d566dbc0bdb83f13_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10137,
                                                                                   "brandName": "OXY", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24524byte_535ab7db658c3f1c8e00a821e5587585_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10394,
                                                                                   "brandName": "FLOAT", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25774byte_07be4b895302ee06cbd9ad53aa017ed5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10143,
                                                                                   "brandName": "Suicoke", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22613byte_16cd0ea92dde2aea19b76b46491814bb_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10146,
                                                                                   "brandName": "GARMIN", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20845byte_5af278c31aad1b5e0982544840c2df96_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10151,
                                                                                   "brandName": "BANPRESTO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte56132byte_ee71a1bac952dac4cd3f59b4c6673203_w800h800.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10153,
                                                                                   "brandName": "Harman/Kardon",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte17446byte_134385ee63bf9d12cd7f98e27344310e_w150h150.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10413,
                                                                                   "brandName": "OSCill", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23787byte_88a0a8c1b72cd8693957af2a53b89bd5_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10414,
                                                                                   "brandName": "LIFEGOESON", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/FgHxeSwXg9SKBtRNrNNKjn-O8yxf"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10161,
                                                                                   "brandName": "PSO Brand", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte47498byte_0bb2a47154dfa0fc914e98cfeae6c407_w1000h1000.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10167,
                                                                                   "brandName": "EVISU", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte8745byte_0ba5f52e059d3e91803a05843c2b22e2_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10423,
                                                                                   "brandName": "Maison Margiela",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22857byte_d8df7145e944cd7b203d3f5520b06c43_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10168,
                                                                                   "brandName": "INXX", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte20442byte_4c50ce6dca7408dec92df78b72106e46_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10169,
                                                                                   "brandName": "B&O", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte36636byte_b32fd6036ba60c4f868b197ada8b8c6f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10425,
                                                                                   "brandName": "Charlie Luciano",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21051byte_28faf07c5d5a078a6fc18357413ce7c3_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10170,
                                                                                   "brandName": "CITIZEN", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21252byte_1158debba23c31ccfed657aa8ce762bd_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10171,
                                                                                   "brandName": "LOFREE", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22408byte_1af23b04a9bc352bfff21edb63514d39_w150h150.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10429,
                                                                                   "brandName": "Arcteryx", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24934byte_5ebce6f644ee8ebdbc89f04a068fc1af_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10174,
                                                                                   "brandName": "DAMTOYS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte31687byte_84591020e1a16ce89318585a5d84e9fc_w150h150.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10175,
                                                                                   "brandName": "POP MART", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24981byte_909c5a578874dac97c6d3796be69cdf3_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10179,
                                                                                   "brandName": "野兽王国", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte36849byte_5af274d0628f77ca06994e30ed50d5c4_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10183,
                                                                                   "brandName": "ALIENWARE/外星人",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25149byte_458a868f82f2ac201e5d2f56fc087d60_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10184,
                                                                                   "brandName": "Herschel", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte34213byte_403f7a96cd33f1cfdb12769a7e870f65_w824h752.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10187,
                                                                                   "brandName": "科大讯飞", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte25000byte_8351390b01275c1fcaa8f20a040b6dfe_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10443,
                                                                                   "brandName": "chinism", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21910byte_d24daabd4b84bba6c37e22a42dd18602_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10188,
                                                                                   "brandName": "韶音", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte6089byte_b5d736ec8a0c1269eceb94dcfa520c37_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10190,
                                                                                   "brandName": "SAINT LAURENT",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21416byte_6836702d9d6f487e44b8922d8eaeb86b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10193,
                                                                                   "brandName": "SPALDING", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte27011byte_12f13f15a9a198939f3d9b847dbdb214_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10195,
                                                                                   "brandName": "Levis", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23207byte_ad584d3079f341b83325f4974b99e342_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10196,
                                                                                   "brandName": "SENNHEISER", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21466byte_f597724d3c9eb3294441c608cb59e1fe_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10197,
                                                                                   "brandName": "CASETIFY", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23539byte_3a85a808033ed920a29cac5fad902b6f_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10199,
                                                                                   "brandName": "JMGO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26989byte_cdd8e059931aa405f55c5d2426862a6b_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10200,
                                                                                   "brandName": "PHILIPS", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24239byte_5655ed4f287863630934c96aa823346a_w150h150.jpg"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10201,
                                                                                   "brandName": "SEIKO", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22717byte_6bfa41469825cfd6c70f5e3080d5de6a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10202,
                                                                                   "brandName": "GENANX", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte9514byte_77dee80e931dfd8b528f609c400951e4_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10204,
                                                                                   "brandName": "TIANC", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21593byte_aa160ed7e50ca090d629490010346a9a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10205,
                                                                                   "brandName": "Drew House", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30015byte_31ba151ba30e01ae6132ce9584b4e49a_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10206,
                                                                                   "brandName": "小米/MI", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte23786byte_d04434a4af3b56e20758cbeaed4f4531_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10207,
                                                                                   "brandName": "CALVIN KLEIN",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte24775byte_736593d1ee0995be050b1fbcec77bf46_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 2016,
                                                                                   "brandName": "DanielWellington",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21711byte_f48145a65169f913b0139ff2e1811e78_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10211,
                                                                                   "brandName": "飞智", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte26616byte_8001c14855f8528d7bccc31183bfaf75_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10213,
                                                                                   "brandName": "TOM FORD", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte21248byte_2994883ac1627497e75e9b99ba327c48_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10485,
                                                                                   "brandName": "RickyisClown",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte22583byte_98f823c8acb1459e6c72f5bdaf8a88b0_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10233,
                                                                                   "brandName": "Dr.Martens", "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte31892byte_8d31e2f10cc7fffe8d99545d757dfff6_w150h150.png"},
                                                                         "seriesList": []}, {
                                                                         "brand": {"goodsBrandId": 10238,
                                                                                   "brandName": "APPortfolio",
                                                                                   "type": 0,
                                                                                   "logoUrl": "https://du.hupucdn.com/news_byte30968byte_19dd10185fc4b82037621b3708a613e4_w150h150.png"},
                                                                         "seriesList": []}]}, "status": 200}


def return_sign(raw_sign_code_str):
    # md5原始sign的字符串
    m = hashlib.md5()
    m.update(raw_sign_code_str.encode("utf8"))
    sign = m.hexdigest()
    return sign


def index_load_data(lastId):
    # 首页数据流
    post_data = dict()
    post_data['tabId'] = ''
    post_data['limit'] = 20
    post_data['lastId'] = lastId
    post_data['sign'] = return_sign('lastId{}limit20tabId19bc545a393a25177083d4a748807cc0'.format(lastId))
    post_data = str(post_data).encode('utf-8')
    res_data = requests.post(index_load_more_url, headers=headers, data=post_data).text
    print(res_data)


def recensales_load_more_data(spuId, lastId, size=20):
    # 最近购买接口
    post_data = dict()
    post_data['limit'] = size
    post_data['spuId'] = spuId
    post_data['lastId'] = lastId
    post_data['sourceApp'] = 'app'
    post_data['sign'] = return_sign(
        'lastId{}limit{}sourceAppappspuId{}19bc545a393a25177083d4a748807cc0'.format(lastId, size, spuId))
    post_data = str(post_data).encode('utf-8')
    res_data = requests.post(recensales_load_more_url, headers=headers, data=post_data).text
    print(res_data)
    return json.loads(res_data)


def search_by_keywords_load_more_data(keywords, page, sortMode, sortType):
    # 关键词搜索商品接口
    sign = return_sign(
        'limit20page{}showHot-1sortMode{}sortType{}title{}unionId19bc545a393a25177083d4a748807cc0'.format(page,
                                                                                                          sortMode,
                                                                                                          sortType,
                                                                                                          keywords))
    print(sign)
    url = 'https://app.poizon.com/api/v1/h5/search/fire/search/list?' \
          'sign={}&title={}&page={}&sortType={}' \
          '&sortMode={}&limit=20&showHot=-1&unionId='.format(sign, quote(keywords), page, sortType, sortMode)
    res_data = requests.get(url, headers=headers).text
    return json.loads(res_data)



def brand_list_load_more_data(page, sortType, sortMode, catId, unionId, title=''):
    # 品牌列表页商品接口
    sign = return_sign(
        'catId{}limit20page{}showHot-1sortMode{}sortType{}title{}unionId{}19bc545a393a25177083d4a748807cc0'.format(
            catId, page, sortMode, sortType, title, unionId
        ))
    print(sign)
    url = 'https://app.poizon.com/api/v1/h5/search/fire/search/list?' \
          'sign={}&title={}&page={}&sortType={}' \
          '&sortMode={}&limit=20&showHot=-1&catId={}&unionId={}'.format(sign, title, page, sortType, sortMode, catId,
                                                                        unionId)
    res_data = requests.get(url, headers=headers).text
    print(res_data)


def product_detail_data(spuId, propertyValueId, productSourceName=''):
    # 商品详情页接口
    post_data = dict()
    post_data['spuId'] = spuId
    post_data['productSourceName'] = productSourceName
    post_data['propertyValueId'] = propertyValueId
    post_data['sign'] = return_sign(
        'productSourceName{}propertyValueId{}spuId{}19bc545a393a25177083d4a748807cc0'.format(productSourceName,
                                                                                             propertyValueId, spuId))
    post_data = str(post_data).encode('utf-8')
    res_data = requests.post(product_detail_url, headers=headers, data=post_data).text
    return json.loads(res_data)


def is_number(param):
    try:
        return int(param)
    except Exception:
        print("输入的数值不是数字")
        exit()

import time, re

if __name__ == '__main__':
    # index_load_data(1)
    # recensales_load_more_data(73803, '')
    # search_by_keywords_load_more_data('詹17', 0, 1, 1)  # 2020年入了一双😍
    print("请输入你需要查找的商品")
    keywords = input()
    keywords_list = str.split(keywords, ",")
    print("请输入你需要查询是数据量,(回车默认100)")
    num_size = input()
    if num_size == '':
        num_size = 100
    else:
        num_size = is_number(num_size)
    sold_data = []
    for keyword in keywords_list:
        datas = search_by_keywords_load_more_data(keyword, 0, 1, 1)  # 2020年入了一双😍
        for idx, prod in enumerate(datas['data']['productList']):
            print("选项:{} title: {}, 销售数量: {}, 销售金额: {}".format(idx, prod['title'], prod['soldNum'], prod['price']/100))
        print("请输入数字,默认0")
        id = input()
        if id == '':
            id = 0
        else:
            id = is_number(id)
        if id > len(datas['data']['productList']) and id > 0:
            print("输入的数字超过产品的上限")
            exit()
        last_id = ''
        for query_idx in range(0, int(num_size/100)):
            details = recensales_load_more_data(datas['data']['productList'][id]['spuId'], last_id, 100)
            last_id = details['data']['lastId']
            # details = product_detail_data(spuId=datas['data']['productList'][id]['spuId'], propertyValueId=0)
            for sold in details['data']['list']:
                now_date = pendulum.now('Asia/Shanghai')
                if sold['formatTime'].find('刚刚') >= 0:
                    now_date = now_date
                elif '分' in sold['formatTime']:
                    print(now_date)
                    now_date = now_date.add(0,0,0,0,0,-int(re.findall(r'\d+', sold['formatTime'])[0])).to_datetime_string()
                    print(now_date)
                elif '小时前' in sold['formatTime']:
                    now_date = now_date.add(0,0,0,0,-int(re.findall(r'\d+', sold['formatTime'])[0]),0).to_datetime_string()
                elif '天前' in sold['formatTime']:
                    now_date = now_date.add(0,0,0,-int(re.findall(r'\d+', sold['formatTime'])[0]),0,0).to_datetime_string()
                elif '月前' in sold['formatTime']:
                    now_date = now_date.add(0,0,-int(re.findall(r'\d+', sold['formatTime'])[0]),0,0,0).to_datetime_string()
                else:
                    now_date = "2020年{}".format(sold['formatTime'])
                sold_data.append([sold['avatar'], sold['userName'], now_date, sold['price']/100, sold['propertiesValues']])
            time.sleep(0.1)
    sold_df = pd.DataFrame(sold_data, columns=['avatar', '用户名', '时间', "价格", "码号"])
    # brand_list_load_more_data(page=0, sortType=1, sortMode=1, catId=0, unionId=144)  # nike系列
    # product_detail_data(spuId=49413, propertyValueId=0)
    sold_df.to_excel("{}_du.xls".format(pendulum.now('Asia/Shanghai').to_date_string()), index=False)

