import pandas as pd
import matplotlib.pyplot as plt


# 用来正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei', 'Songti SC', 'STFangsong']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 优化格式
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)
path = '/Users/fengliang/Desktop/综合查询test.xlsx'
cust_list = pd.read_excel(path, header=0, index_col=0)

cust_list = cust_list.loc[cust_list['贷款金额(元)'].apply(lambda a: a <= 2000)]

print(cust_list)
# pandas绘图方法
# cust_list.plot.bar(x='客户名称', y='贷款金额(元)', color='green',title="客户贷款金额对比")

# matplotlib绘图方法
plt.bar(cust_list['客户名称'], cust_list['贷款金额(元)'], color='#3AA3B1')
# x轴旋转
plt.xticks(cust_list['客户名称'], rotation=45)
plt.xlabel('客户名称')
plt.ylabel('贷款金额(元)')
plt.title('客户贷款金额排序', fontsize=14)
# 紧凑型布局
plt.tight_layout()


plt.show()
