import pandas as pd

d = {'x': 100, 'y': 200, 'z': 300}
print(d.keys())
s1 = pd.Series(d)
print(s1)
d1 = pd.Series([1, 2, 3], index=[1, 2, 3], name="A")
d2 = pd.Series([10, 20, 30], index=[1, 2, 3], name="B")
d3 = pd.Series([100, 200, 300], index=[1, 2, 4], name="C")
# 以列形式添加
print("===以列形式添加===")
df = pd.DataFrame({d1.name: d1, d2.name: d2, d3.name: d3})
print(df)
print("===以行形式添加===")
# 以行形式添加
df2 = pd.DataFrame([d1, d2, d3])
print(df2)
