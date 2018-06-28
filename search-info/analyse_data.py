# Code based on Python 3.x
# _*_ coding: utf-8 _*_

import pandas as pd

df = pd.read_csv('zhilian_DA.csv', header=None)


df.columns = ['职位名称', '反馈率', '公司名称', '月薪', '工作地点',
           '发布日期', '招聘简介', '网页链接']

# 将调整后的dataframe文件输出到新的csv文件
df.to_csv('zhilian_DA_update.csv', index=False)