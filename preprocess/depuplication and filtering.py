import pandas as pd
import numpy as np
from pandas import Series,DataFrame
path='D:\\BIT\\Course\\数据挖掘\\大作业\\1.csv'
f=open(path,encoding='UTF-8')
df=pd.read_csv(f)
print(df.shape[0])
print(df.dtypes)
df.drop_duplicates(subset=['j_name','c_name'],keep='first',inplace=True)
print(df.shape[0])
df.to_csv('2.csv',encoding='utf=8')
df=df[~ df['j_name'].str.contains('软件测试|化工|扫描仪|实施|信息|测试|合伙人|售前|运维|电销|销售|律师|专员|机械|土木|商务|链家|运营|新媒体|岗位|教学|教务|整形|美容|微信|web|前端|行政|司机|助理|设计|策划|文案|架构')]
print(df.shape[0])
df=df[~df['j_name'].isin(['软件工程师','高级软件工程师'])]
print(df.shape[0])
df=df[~ df['w_field'].str.contains('测试|售前|运维|合伙人|电销|销售|律师|专员|机械|土木|商务|链家|运营|新媒体|岗位|教学|教务|整形|美容|微信|web|前端|行政|司机|助理|设计|策划|文案|架构',na=False)]
print(df.shape[0])
df=df[df['j_name'].str.len()>4]
print(df.shape[0])
df.to_csv('3.csv',encoding='utf-8')
