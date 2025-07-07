import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=False, help='入力ファイルのパス')
args = parser.parse_args()

inputFileName = args.input
if inputFileName is None:
    inputFileName = 'group.json'

if not os.path.exists(inputFileName):
    print(inputFileName, 'が見つかりません', file=sys.stderr)
    exit(0)
