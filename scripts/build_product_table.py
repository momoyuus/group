def buildProductTable(groupData):
    order = groupData.order
    num = groupData.numOfGenerators

    def toArrays(e):
        now = []
        for i in range(num):
            if e[i] == 0:
                continue
            now.append([i, e[i]])
        return now

    for i in range(order):
        for j in range(order):
            now = []
            now.extend(toArrays(groupData.indexMapInv[i]))
            now.extend(toArrays(groupData.indexMapInv[j]))
            while True:
                l = len(now)
                p = False
                for k in range(0, l):
                    if now[k][1] == 0:
                        now.pop(k)
                        p = True
                        break
                if p:
                    continue
                for k in range(l - 1, -1, -1):
                    ni = now[k][0]
                    if groupData.ords[ni] <= now[k][1]:
                        now[k][1] %= groupData.ords[ni]
                        p = True
                        break
                    if k == 0:
                        continue
                    nj = now[k - 1][0]
                    if nj < ni:
                        continue
                    if ni == nj:
                        now[k][1] += now[k - 1][1]
                        now.pop(k - 1)
                        p = True
                        break
                    if nj > ni:
                        now[k][1] -= 1
                        now[k - 1][1] -= 1
                        now = now[:k] + toArrays(groupData.indexMapInv[groupData.op[nj][ni]]) + now[k:]
                        p = True
                        break
                if not p:
                    break
            t = [0 for _ in range(num)]
            for k in range(len(now)):
                t[now[k][0]] = now[k][1]
            groupData.productTable[i][j] = groupData.indexMap[tuple(t)]
