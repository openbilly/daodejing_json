# -- coding: utf-8 --
# list其实可以理解为一种特殊的字典

import json
import os
import time
file = open("daodejing.json", 'r', encoding='utf-8')
data = file.read()
books = json.loads(data)
print("数据类型：")
print(type(data))
print(type(books))
# print(books[0])
print(type(books[0]))

"""
for book in books:
    print(book['name'])
    print(type(book['paragraphs']))
    i = 1
    for paragraph in book['paragraphs']:
        print (str(i) + "、" + paragraph)
        i += 1
"""

"""
book3 = books[3]
# print(book3)
print(book3.get("dynasty"))
"""

for book in books:
    x = 1 #要输了第x章
    select_book = "道德經學錄"
    if book.get('name') == select_book :
        print(book.get('name'))
        print(book.get("dynasty",'未知年代'))
        print(type(book['paragraphs']))
        print(book['paragraphs'][x-1])
#    paragraphs = book.get('paragraphs')
#    print(paragraphs[1])
