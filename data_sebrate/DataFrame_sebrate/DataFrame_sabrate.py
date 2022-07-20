import numpy as np
import pandas as pd
import csv

movies = pd.read_table('movies.txt', sep='::',
                       header=None, names=['movie_id', 'title', 'genres'])
# 读取原文件
print(movies.head(6))  # 检查原文件格式

genres = movies['genres'].copy()
genres.to_csv('genres.csv', index=False, header=False)
# 提取genres作为Series，输出到csv文件中

f = open('genres.csv')
genres_read = csv.reader(f, delimiter='|')
# 利用csv.reader(f,delimiter='|')命令，将genres中的项目单独分开，此时为csv.reader格式
genres_lines = list(genres_read)  # list化，为转成DataFrame作准备

genres_pd = pd.DataFrame(genres_lines, columns=list('abcdef'))
# 将genres中项目转为DataFrame，赋值临时列标题abcdef

genres_unique = genres_pd.loc[:, 'a'].unique()
# 在第'a'列中用.unique()取出不重复的genres名称

for i in genres_unique:
    movies['genr_' + i] = pd.Series(1, index=genres_pd[(genres_pd == i).any(axis=1)].index)
# 用for循环，在原文件movies中添加genres项目作为列，项目名称从genres_unique获取
# 对应的index：例如--->Animation名称出现的行都标记出来，在Animation列中对应赋值1
print(movies)
print(movies.iloc[0].dropna())
