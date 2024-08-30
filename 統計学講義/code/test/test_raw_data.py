import unittest
import csv
from pathlib import Path

import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import raw_data

class TestRawData(unittest.TestCase):
    """
    frequency_table.pyのテスト
    """

    def setUp(self) -> None:
        """
        テスト用のcsvファイルを事前に読み込む
        """
        parent = Path(__file__).resolve().parent
        row_data = []

        # テスト用のcsvファイルの読み込み
        with open(parent.joinpath('../sample_data/StatData01_1.csv')) as f:
            reader = csv.reader(f)
            data = [row[0] for row in reader][1:]
            data = [int(row) for row in data]

        self.raw_data = raw_data.RawData(data)

    def test_mean(self):
        """
        平均のテスト
        """
        self.assertEqual(self.raw_data.mean(), 3160.2)
    
    def test_median(self):
        """
        中央値のテスト
        """
        # 偶数個の場合
        self.assertEqual(self.raw_data.median(), 3160)

        # 奇数個の場合
        odd_raw_data = raw_data.RawData([1, 2, 3, 4, 5])
        self.assertEqual(odd_raw_data.median(), 3)

unittest.main()