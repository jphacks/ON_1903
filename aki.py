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
        print(df)
        target = get_target(df)
        print(f"{target}を使用していますか？")
        if choose():
            # そのターゲットが使用されている食品のDataFrameを返す
            df = df.query(f"{target} != 0")
            df = df[list(filter(lambda x: x != target, df.columns))]
        else:
            # そのターゲットが使用されていない食品のDataFrameを返す
            df = df.query(f"{target} == 0")
            df = df[list(filter(lambda x: x != target, df.columns))]
        
        if len(df) == 1:
            print(df.iloc[0, 0])
            break
