import sys
import argparse
import os
from scripts.load_data import loadData
from scripts.build_product_table import buildProductTable

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=False, help='入力ファイルのパス')
args = parser.parse_args()

inputFileName = args.input
if inputFileName is None:
    inputFileName = 'group.json'

if not os.path.exists(inputFileName):
    print(inputFileName, 'が見つかりません', file=sys.stderr)
    exit(0)

groupData = loadData(inputFileName)
buildProductTable(groupData)
print(groupData)
