import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 30000)

path = '/Users/fengliang/Desktop/综合查询test.xlsx'

cust_list = pd.read_excel(path, header=0, index_col='客户编号')
print(cust_list.dtypes)
# 修改类型
cust_list['客户名称'] = cust_list['客户名称'].astype(str)
cust_list = cust_list.map(lambda x: x.strip() if isinstance(x, str) else x)
cust_list.sort_values(by=['贷款金额(元)', '风险状态'], inplace=True, ascending=[False, True])
cust_list['客户名称'] = cust_list['客户名称'].str.strip()
cust_list.to_excel('/Users/fengliang/Desktop/综合查询Test.xlsx')


print(cust_list.dtypes)
print(cust_list.head(15))
