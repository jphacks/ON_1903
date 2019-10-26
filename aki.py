import pandas as pd

def choose():
    tmp = input("y/n:")
    if tmp == "y":
        return True
    else:
        return False

def get_target(df):
    # dfのなかで重みの総和が最小の食材を返す
    return df.iloc[:, 1:-1].apply(lambda line: sum(line.values)).idxmax()

if __name__ == "__main__":
    df = pd.read_csv("tmp.csv")

    while True:
        target = get_target(df)
        print(f"{target}を使用していますか？")
        if choose():
            df = df.query(f"{target} != 0") # そのターゲットが使用されている食品のDataFrameを返す
            if len(df) == 1:
                print(df.iloc[0, 0])
                break
        else:
            # df = df.query(f"{target} == 0")[list(filter(lambda column: column != target, df.columns))] # そのターゲットが使用されていない食品のDataFrameを返す
            df = df[list(map(lambda x: x[0], filter(lambda x: x[1]>0, df.query(f"{target} == 0").sum()[1:].items())))]

# for column in df.columns[1:-1]:
#     print(column + "を使用していますか？")
#     if choose():
#         df['ポイント'] = df.apply(lambda row: row['ポイント']+row[column]*1 if row[column] else row['ポイント'], axis=1)
# print(df.loc[df['ポイント'].idxmax(),df.columns[0]])
# print(df)
