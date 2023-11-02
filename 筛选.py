import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)
path = '/Users/fengliang/Desktop/综合查询test.xlsx'
cust_list = pd.read_excel(path, header=0, index_col=0)


def money_0_to_1000(a):
    return 0 <= a <= 1000


def money_10000000(a):
    return a >= 100000


def danger(b):
    return '可疑' == b


print(cust_list.dtypes)
# apply:应用该函数，将该series中的数据放进去筛选，循环a
cust_list = cust_list.loc[cust_list['风险状态'].apply(lambda a: a == '可疑')]

cust_lists2 = cust_list.loc[cust_list['贷款金额(元)'].apply(lambda a: a >= 10000)]

print(cust_list.head(5))
print(cust_lists2.head(3))
