# 采用正则表达式regex
import re
import pandas as pd
import numpy as np

with open('movies.txt') as f:
    content = f.read()
#  整理成字符串Str格式
content01 = content.replace('::', '|')
#  替换分隔符
print(content01)

content_first_list = re.findall(r'[\w() :,.|\'!?=#$%+_;"\\&/@\-]+', content01)
#  按回车分离出每行
print(content_first_list)

content_2nd_list = [re.findall(r'[\w() :,.\'!?=%+_$#;"\\&/@\-]+', x) for x in content_first_list]
#  按｜分隔成list
print(content_2nd_list)

content_pd = pd.DataFrame(content_2nd_list)
#转成DataFrame
print(content_pd)

movies_type = pd.Series(content_pd.iloc[:,2].unique()).dropna()
#  提取出电影type分类
movies_type

for i in movies_type:
    content_pd['gen_' + i] = pd.Series(1, index=content_pd[(content_pd == i).any(axis=1)].index)
# 用for循环，在原文件movies中添加gen_项目作为列，项目名称从movies_type获取
# 对应的index：例如--->Animation名称出现的行都标记出来，在Animation列中对应赋值1
print(content_pd)
print(content_pd.iloc[0].dropna())