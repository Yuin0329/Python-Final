# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 00:14:36 2023

@author: Yuin
"""

from pymongo import MongoClient

# 連接到 MongoDB
client = MongoClient()

# 建立疫苗資料庫
db = client['vaccines']

# 建立疫苗資料表
vaccines_col = db['vaccines']

# 插入疫苗資料
vaccines_col.insert_many([
    {
        "疫苗名稱": "輝瑞",
        "研發國家": "美國和德國",
        "保護率": "95%",
        "副作用": "頭痛",
        "每劑價格(新台幣)": 530
    },
    {
        "疫苗名稱": "莫德納",
        "研發國家": "美國",
        "保護率": "90%",
        "副作用": "頭痛",
        "每劑價格(新台幣)": 620
    },
    {
        "疫苗名稱": "AZ",
        "研發國家": "英國和瑞典",
        "保護率": "80%",
        "副作用": "接種處痠痛",
        "每劑價格(新台幣)": 310
    },
    {
        "疫苗名稱": "高端",
        "研發國家": "台灣",
        "保護率": "85%",
        "副作用": "接種處痠痛",
        "每劑價格(新台幣)": 750}
])
print('-----------------------3.1----------------------')
for vaccine in vaccines_col.find():
    print(vaccine)
print('-----------------------3.2----------------------')
query = {"研發國家": "美國"}
query2 = {"研發國家": "美國和德國"}
for vaccine in vaccines_col.find(query):
    print(vaccine)
for vaccine in vaccines_col.find(query2):
    print(vaccine)
print('-----------------------3.3----------------------')
# 查詢每劑價格大於 500 的疫苗
query = {"每劑價格(新台幣)": {"$gt": 500}}
for vaccine in vaccines_col.find(query):
    print(vaccine)
print('----------------------3.4-----------------------')
# 新增一筆疫苗資料
vaccines_col.insert_one({
        "疫苗名稱": "聯亞",
        "研發國家": "台灣",
        "保護率": "80%",
        "副作用": "嗜睡",
        "每劑價格(新台幣)": 550
    })

# 顯示疫苗資料庫中所有疫苗
for vaccine in vaccines_col.find():
    print(vaccine)
print('------------------------3.5---------------------')
# 更新輝瑞和莫德納疫苗中副作用欄位
query = {"疫苗名稱": {"$in": ["輝瑞", "莫德納"]}}
new_values = {"$set": {"副作用": "頭痛和嗜睡"}}
vaccines_col.update_many(query, new_values)

# 顯示更新後的疫苗資料
for vaccine in vaccines_col.find():
    print(vaccine)
print('------------------------3.6---------------------')
# 依照每劑價格，由小到大排序
for vaccine in vaccines_col.find().sort("每劑價格(新台幣)", 1):
    print(vaccine)
print('------------------------3.7---------------------')
# 刪除疫苗庫中的所有資料
result = vaccines_col.delete_many({})

# 顯示刪除結果
print("刪除數量: ", result.deleted_count)