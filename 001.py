import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3], 'name': ['Tim', 'Victor', 'Nick']})
# 设置索引
df = df.set_index('ID')
df.to_excel('/Users/fengliang/Documents/workspace/output.xlsx')
print(df)
