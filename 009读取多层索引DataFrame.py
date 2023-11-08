import pandas as pd

# 文件路径
path = '/Users/fengliang/Documents/workspace/Pandas&Matplotlib/excel/2023年社保卡、代发工资任务进度表(10月31日).xlsx'
# 读取Excel文件，并指定多层索引的列名，指定sheet
df_excel = pd.read_excel(path, sheet_name='支行进度表', header=0, index_col=0)

print(df_excel)