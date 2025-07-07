import sys
import json
from scripts.group_data import GroupData

def err(inputFileName):
    print(inputFileName, 'の記法が正しくありません', file=sys.stderr)
    exit(0)

def loadData(inputFileName):
    with open(inputFileName, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            groupData = GroupData()
            groupData.order = int(data['order'])
            assert 0 < groupData.order
            num = int(data['numOfGenerators'])
            groupData.numOfGenerators = num
            assert 1 <= num and num <= 26
            
            mul = 1
            groupData.ords = [0 for _ in range(num)]
            for i in range(num):
                s = chr(ord('a') + i)
                groupData.ords[i] = int(data['relations'][s])
                assert 1 < groupData.ords[i]
                mul *= groupData.ords[i]
            assert mul == groupData.order

            groupData.indexMap = dict()
            now = [0 for _ in range(num)]
            def dfs(i):
                if i == num:
                    groupData.indexMap[tuple(now)] = len(groupData.indexMap)
                    groupData.indexMapInv.append(tuple(now))
                    return
                
                for j in range(groupData.ords[i]):
                    now[i] = j
                    dfs(i + 1)
            dfs(0)

            groupData.product_table = [[0 for _ in range(groupData.order)] for _ in range(groupData.order)]
            groupData.op = [[0 for _ in range(num)] for _ in range(num)]
            for i in range(num):
                for j in range(num):
                    if i < j:
                        now = [0 for _ in range(num)]
                        now[i] = 1
                        now[j] = 1
                        groupData.op[i][j] = groupData.indexMap[tuple(now)]
                    elif i == j:
                        now = [0 for _ in range(num)]
                        now[i] = 2 % groupData.ords[i]
                        groupData.op[i][j] = groupData.indexMap[tuple(now)]
                    else:
                        s = chr(ord('a') + i) + chr(ord('a') + j)
                        now = data['relations'][s]
                        groupData.op[i][j] = groupData.indexMap[tuple(now)]
            
            return groupData
        except Exception:
            err(inputFileName)
