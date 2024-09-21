import unittest
import csv
from pathlib import Path

import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

import correlation_table

class TestCorrelationTable(unittest.TestCase):
    """
    correlation_table.pyのテスト
    """

    def setUp(self) -> None:
        """
        テスト用のcsvファイルを事前に読み込む
        """
        parent = Path(__file__).resolve().parent
        row_data = []

        with open(parent.joinpath('../sample_data/StatData02_1.csv')) as f:
            reader = csv.reader(f)
            row_data = [row for row in reader][1:]
            row_data = [[float(row[1]), float(row[2])] for row in row_data]

        self.correlation_table = correlation_table.CorrelationTable(row_data, [1, 200], [9, 10], [45, 2400])
    
    def test_covariance(self):
        """
        共分散のテスト
        """
        self.assertAlmostEqual(self.correlation_table.covariance(), 442.00, places=2)

unittest.main()