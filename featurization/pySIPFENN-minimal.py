import pysipfenn
import numpy as np
c = pysipfenn.Calculator()
c.downloadModels('SIPFENN_Krajewski2022_NN30')
c.runFromDirectory('structures', 'KS2022', 'parallel')
resultArray = np.array(c.descriptorData)
np.save('descriptorData.npy', resultArray)
outString = f'| {" | ".join(c.get_resultDictsWithNames()[0].keys())} |\n'
outString += f'| {" | ".join(["---" for _ in c.get_resultDictsWithNames()[0].keys()])} |\n'
for e in c.get_resultDictsWithNames():
    outString += f'| {e["name"]} '
    outString += f'| {" | ".join([str(round(v,4)) for k, v in e.items() if k != "name"])} |\n'
print(outString)
with open('response.md', 'w') as f:
    f.write(outString)"
