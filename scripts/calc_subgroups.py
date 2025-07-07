import sys
sys.setrecursionlimit(10**9)

def calcSubgroups(groupData):
    order = groupData.order
    now = [0 for _ in range(order)]
    subgroups = []
    isNormal = []

    def isSubgroup():
        if now[0] == 0:
            return False

        for i in range(order):
            if now[i] == 0:
                continue
            for j in range(order):
                if now[j] == 0:
                    continue
                if now[groupData.productTable[i][j]] == 0:
                    return False

        for i in range(order):
            if now[i] == 0:
                continue
            if now[groupData.invs[i]] == 0:
                return False

        return True

    def isNormalSubgroup():
        for i in range(order):
            if now[i] == 0:
                continue
            for j in range(order):
                g = groupData.productTable[j][i]
                g = groupData.productTable[g][groupData.invs[j]]
                if now[g] == 0:
                    return False
        return True

    def toArrays():
        l = []
        for i in range(order):
            if now[i] == 1:
                l.append(i)
        return l

    def dfs(i):
        if i == order:
            if isSubgroup():
                subgroups.append(toArrays())
                if isNormalSubgroup():
                    isNormal.append(True)
                else:
                    isNormal.append(False)
            return

        now[i] = 0
        dfs(i + 1)
        now[i] = 1
        dfs(i + 1)

    dfs(0)
    
    return (subgroups, isNormal)
