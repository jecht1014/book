import pandas as pd

class CorrelationTable:
    """
    相関表
    """
    def __init__(self, raw_data: list[int|float], class_interval: list[int|float], num_of_class: list[int|float], min_class_mark: list[int|float]):
        """
        Parameters
        ----------
        row_data : list[int|float]
            粗データ
        class_interval : list[int|float]
            階級幅
        num_of_class : list[int|float]
            階級数
        min_class_mark : list[int|float]
            最小の階級値
        """

        # リストの長さチェック
        if not(len(class_interval) == len(class_interval) == len(num_of_class) == len(num_of_class) == len(min_class_mark) == 2):
            raise ValueError('リストの長さは2である必要があります')

        self.raw_data = raw_data
        self.class_interval = class_interval
        self.num_of_class = num_of_class
        self.length = len(raw_data)

        xs = [min_class_mark[0] + class_interval[0]*i for i in range(num_of_class[0])]
        ys = [min_class_mark[1] + class_interval[1]*i for i in range(num_of_class[1])]

        self.correlation_table = pd.DataFrame(0, index=ys, columns=xs)
        
        for raw in raw_data:
            for y in ys:
                for x in xs:
                    if x-class_interval[0]/2 < raw[0] <= x+class_interval[0]/2 and y-class_interval[1]/2 < raw[1] <= y+class_interval[1]/2:
                        self.correlation_table.loc[y, x] += 1
                        break
        
    def covariance(self) -> float:
        """
        共分散の計算を行う関数

        Returns
        -------
        float
            共分散
        """
        x_frequency = self.correlation_table.sum()
        x_mean = x_frequency.dot(pd.Series(self.correlation_table.columns.values, index=x_frequency.index.values)) / self.length

        y_frequency = self.correlation_table.sum(axis=1)
        y_mean = y_frequency.dot(pd.Series(self.correlation_table.index.values, index=y_frequency.index.values)) / self.length

        covariance = 0
        for column_name, item in self.correlation_table.items():
            for row_name, value in item.items():
                covariance += (column_name - x_mean) * (row_name - y_mean) * value

        covariance /= self.length
        return covariance
    
    def correlation_coefficient(self) -> float:
        """
        相関係数の計算を行う関数

        Returns
        -------
        float
            相関係数
        """
        
        # xの標準偏差を求める
        x_frequency = self.correlation_table.sum()
        x_mean = x_frequency.dot(pd.Series(self.correlation_table.columns.values, index=x_frequency.index.values)) / self.length
        standard_deviation_x = 0
        for item, value in x_frequency.items():
            standard_deviation_x += (item - x_mean)**2 * value
        standard_deviation_x = (standard_deviation_x / (self.length))**0.5

        # yの標準偏差を求める
        y_frequency = self.correlation_table.sum(axis=1)
        y_mean = y_frequency.dot(pd.Series(self.correlation_table.index.values, index=y_frequency.index.values)) / self.length
        standard_deviation_y = 0
        for item, value in y_frequency.items():
            standard_deviation_y += (item - y_mean)**2 * value
        standard_deviation_y = (standard_deviation_y / self.length)**0.5

        print(standard_deviation_x, standard_deviation_y)
        return self.covariance()/(standard_deviation_x*standard_deviation_y)