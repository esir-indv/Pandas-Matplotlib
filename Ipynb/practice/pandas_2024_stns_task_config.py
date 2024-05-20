import pandas as pd
data_file = "/Users/fengliang/Desktop/一起合并输出.xlsx"
data_info = pd.read_excel(data_file)
data_info.fillna(method='ffill', inplace=True)
data_info.to_excel('file.xlsx')