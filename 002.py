import pandas as pd

pd.set_option("display.max_columns", None)

cust = pd.read_excel('/Users/fengliang/Desktop/综合查询20200331.xlsx', header=0)
cust =cust.set_index("客户编号")


print(cust.shape)

print(cust.columns)
print("===")

print(cust.head(3))

cust.to_excel('/Users/fengliang/Desktop/综合查询20231031.xlsx')