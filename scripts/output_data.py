import json
import json
import re
from io import StringIO

class GroupEncoder(json.JSONEncoder):
    def encode(self, obj):
        buffer = StringIO()
        self._encode_obj(obj, buffer, parent_key=None)
        return buffer.getvalue()

    def _encode_obj(self, obj, buffer, parent_key):
        if isinstance(obj, dict):
            buffer.write("{")
            for i, (k, v) in enumerate(obj.items()):
                if i > 0:
                    buffer.write(", ")
                buffer.write(json.dumps(k))
                buffer.write(": ")
                self._encode_obj(v, buffer, parent_key=k)
            buffer.write("}")
        elif isinstance(obj, list):
            # キーが "orderX" の場合 → 中のリスト（部分群）を1行で出力
            if parent_key and re.match(r"order\d+", parent_key):
                buffer.write("[\n")
                for i, subgroup in enumerate(obj):
                    if i > 0:
                        buffer.write(",\n")
                    inline = "[{}]".format(", ".join(json.dumps(pair) for pair in subgroup))
                    buffer.write("  " + inline)
                buffer.write("\n]")
            else:
                buffer.write("[\n")
                for i, item in enumerate(obj):
                    if i > 0:
                        buffer.write(",\n")
                    buffer.write("  ")
                    self._encode_obj(item, buffer, parent_key=None)
                buffer.write("\n]")
        else:
            buffer.write(json.dumps(obj))
def outputData(groupData, subgroups, isNormal):
    order = groupData.order
    num = groupData.numOfGenerators

    data = dict()

    group = dict()
    group['order'] = order
    group['numOfGenerators'] = num

    relations = dict()
    for i in range(num):
        relations[chr(ord('a') + i)] = groupData.ords[i]
    
    for i in range(num):
        for j in range(i + 1, num):
            relations[chr(ord('a') + j) + chr(ord('a') + i)] = str(list(groupData.indexMapInv[groupData.op[j][i]]))
    
    group['relations'] = relations
    data['group'] = group

    data['subgroup'] = dict()
    data['normal-subgroup'] = dict()
    def toArray(now):
        l = []
        for i in range(len(now)):
            l.append(list(groupData.indexMapInv[now[i]]))
        return str(l)
    
    for i in range(len(subgroups)):
        g = len(subgroups[i])
        s = 'order' + str(g)
        if not s in data['subgroup']:
            data['subgroup'][s] = []
        data['subgroup'][s].append(toArray(subgroups[i]))

        if isNormal[i]:
            if not s in data['normal-subgroup']:
                data['normal-subgroup'][s] = []
            data['normal-subgroup'][s].append(toArray(subgroups[i]))

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, cls=GroupEncoder, ensure_ascii=False, indent=4)
