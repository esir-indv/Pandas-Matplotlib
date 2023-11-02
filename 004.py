import pandas as pd
from datetime import date, timedelta

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 7000)
# 读取的时候最好指定Index列，避免自动生成
cust_list = pd.read_excel('/Users/fengliang/Desktop/综合查询20200331.xlsx', header=0, index_col=None,
                          dtype={'日期': str, '客户名称': str, '风险状态': str})
cust_list = cust_list.map(lambda x: x.strip() if isinstance(x, str) else x)
# 初始日期
start = date(2023, 10, 2)
# 循环填充日期
for i in cust_list.index:
    cust_list['日期'].at[i] = start

print(cust_list.head(15))

cust_list.set_index('客户编号', inplace=True)
cust_list.to_excel('/Users/fengliang/Desktop/综合查询Test.xlsx')
