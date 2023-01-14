# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 03:02:15 2023

@author: Yuin

判斷是否發生詐騙:參與者 1 是否同時擔任車禍事故 1 和車禍事故 2 中的駕駛者或搭乘者, 以
及保險代理人是否同時為車禍事故 1 和車禍事故 2 中參與者做保險代理，或是車禍事故 2 中車
輛 3 的搭乘者參與者 2 ，同時也是車禍事故 1 中車輛 2 的搭乘者，如果發生則可能發生詐騙,
由查詢圖形資料庫中的關係來判斷,其符合上述情形的後兩者情況，因此有可能為詐欺事件。
"""

from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

# 建立車禍節點
graph.run("CREATE (a:車禍 {name: '車禍 1'})")
graph.run("CREATE (a:車禍 {name: '車禍 2'})")

# 建立車輛節點
graph.run("CREATE (v:車禍事故參與車輛 {name: '車 1'})")
graph.run("CREATE (v:車禍事故參與車輛 {name: '車 2'})")
graph.run("CREATE (v:車禍事故參與車輛 {name: '車 3'})")
graph.run("CREATE (v:車禍事故參與車輛 {name: '車 4'})")

# 建立參與者節點
graph.run("CREATE (p:車禍參與者 {name: '參與者 1'})")
graph.run("CREATE (p:車禍參與者 {name: '參與者 2'})")
graph.run("CREATE (p:車禍參與者 {name: '參與者 3'})")

# 建立保險代理人節點
graph.run("CREATE (i:保險代理人 {name: '保險代理人'})")

# 建立醫生節點
graph.run("CREATE (d:醫生 {name: '醫生'})")

# 建立律師節點
graph.run("CREATE (l:律師 {name: '律師'})")
# 建立車 1 捲入車禍 1 的關係
graph.run("MATCH (a:車禍 {name: '車禍 1'}), (v:車禍事故參與車輛 {name: '車 1'}) CREATE (v)-[:捲入]->(a)")
# 建立車 2 捲入車禍 1 的關係
graph.run("MATCH (a:車禍 {name: '車禍 1'}), (v:車禍事故參與車輛 {name: '車 2'}) CREATE (v)-[:捲入]->(a)")

# 建立車 3 捲入車禍 2 的關係
graph.run("MATCH (a:車禍 {name: '車禍 2'}), (v:車禍事故參與車輛 {name: '車 3'}) CREATE (v)-[:捲入]->(a)")

# 建立車 4 捲入車禍 2 的關係
graph.run("MATCH (a:車禍 {name: '車禍 2'}), (v:車禍事故參與車輛 {name: '車 4'}) CREATE (v)-[:捲入]->(a)")

# 建立參與者 1 駕駛車 1 的關係
graph.run("MATCH (p:車禍參與者 {name: '參與者 1'}), (v:車禍事故參與車輛 {name: '車 1'}) CREATE (p)-[:駕駛]->(v)")

# 建立參與者 1 目擊車 3 發生車禍 的關係
graph.run("MATCH (p:車禍參與者 {name: '參與者 1'}), (v:車禍事故參與車輛 {name: '車 3'}) CREATE (p)-[:目擊證人]->(v)")

# 建立參與者 2 駕駛車 2 的關係
graph.run("MATCH (p:車禍參與者 {name: '參與者 2'}), (v:車禍事故參與車輛 {name: '車 2'}) CREATE (p)-[:駕駛]->(v)")

# 建立參與者 2 搭乘車 3 的關係
graph.run("MATCH (p:車禍參與者 {name: '參與者 2'}), (v:車禍事故參與車輛 {name: '車 3'}) CREATE (p)-[:搭乘]->(v)")

# 建立參與者 3 駕駛車 4 的關係
graph.run("MATCH (p:車禍參與者 {name: '參與者 3'}), (v:車禍事故參與車輛 {name: '車 4'}) CREATE (p)-[:駕駛]->(v)")

# 建立律師評定車 4 的關係
graph.run("MATCH (l:律師 {name: '律師'}), (v:車禍事故參與車輛 {name: '車 4'}) CREATE (l)-[:評定]->(v)")

# 建立保險代理人幫參與者 1 做保險代理 的關係
graph.run("MATCH (i:保險代理人 {name: '保險代理人'}), (p:車禍參與者 {name: '參與者 1'}) CREATE (i)-[:保險代理]->(p)")

# 建立保險代理人幫參與者 3 做保險代理 的關係
graph.run("MATCH (i:保險代理人 {name: '保險代理人'}), (p:車禍參與者 {name: '參與者 3'}) CREATE (i)-[:保險代理]->(p)")

# 建立醫生幫參與者 3 做治療 的關係
graph.run("MATCH (d:醫生 {name: '醫生'}), (p:車禍參與者 {name: '參與者 3'}) CREATE (d)-[:治療]->(p)")


          