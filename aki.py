import pandas as pd

def choose():
    tmp = input("y/n:")
    if tmp == "y":
        return True
    else:
        return False

df = pd.read_csv("tmp.csv")
#print(df.head())

for column in df.columns[1:-1]:
    print(column + "を使用していますか？")
    if choose():
        df['ポイント'] = df.apply(lambda row: row['ポイント']+row[column]*1 if row[column] else row['ポイント'], axis=1)
print(df.loc[df['ポイント'].idxmax(),df.columns[0]])
print(df)
