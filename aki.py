import pandas as pd

class Jinn:
    def __init__(self, path):
        """
        filepath: データのCSVファイルへのパス
        """
        self.default_df = pd.read_csv(path) # デフォルトのデータフレーム（今後は使用しない）
        self.df = self.default_df # このデータフレームを書き換えながら推測していく
        self.target = "" # 質問の要素
        self.last_target = "" #前回の質問の要素

    def update_target(self):
        # もっとも使用されている要素を返す
        self.target = self.df.iloc[:, 1:-1].apply(lambda line: sum(line.values)).idxmax()

        if len(self.df) == 1:
            print(self.df)
            self.last_target = self.df.iloc[0,0]
            return (self.df.iloc[0,0], 1) # 食品がほぼ確定した場合
        elif len(self.df) == 0:
            if self.last_target == "":
                return ("データが不足しています", 2) # 推論対象の食品が全て無くなった場合
            return ("あなたが食べたいのは"+self.last_target+"です", 2) # 推論対象の食品が全て無くなった場合
        else:
            return (self.target, 0) # 食品が確定していない場合

    def update_remining_df(self, choosed):
        if choosed:
            # そのターゲットが使用されている食品のDataFrameを返す
            _df = self.df.query(f"{self.target} != 0")
            self.df = _df[list(filter(lambda x: x != self.target, _df.columns))]
        else:
            # そのターゲットが使用されていない食品のDataFrameを返す
            _df = self.df.query(f"{self.target} == 0")
            self.df = _df[list(filter(lambda x: x != self.target, _df.columns))]

        return self.df


if __name__ == "__main__":
    jinn = Jinn(path="tmp.csv")

    while True:
        print(jinn.df)

        target = jinn.update_target() # 質問するtargetを返す

        print(f"{target}を使用していますか？")
        is_choose = input("y/n:") == "y"
        df = jinn.update_remining_df(is_choose) # データフレームの更新

        if len(df) == 1:
            print(df.iloc[0, 0])
            break
