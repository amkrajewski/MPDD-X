print('Importing pySIPFENN...', flush=True)
from pysipfenn import Calculator
import numpy as np
# ****************  pySIPFENN  **********************
# Init
print('\n\n\nStarting pySIPFENN Run', flush=True)
c = Calculator()
# Get model and run from directory
c.downloadModels('SIPFENN_Krajewski2022_NN30')
c.loadModels('SIPFENN_Krajewski2022_NN30')
c.runFromDirectory('structures', 'KS2022', 'serial')
# Persist results
resultArray = np.array(c.descriptorData)
np.save('descriptorData.npy', resultArray)
c.writeDescriptorsToCSV('KS2022', 'descriptorData.csv')
sipfennResult = c.get_resultDictsWithNames()
c.writeResultsToCSV('results.csv')
del c
print('pySIPFENN Done!\n\n\n', flush=True)


# Order keys in order "name", "SIPFENN_*", "ALIGNN_*"
finalResult = [{**{'name': e['name']}, **{k: e[k] for k in e if k.startswith('SIPFENN')}} for e in sipfennResult]
print(finalResult, flush=True)
outString = f'| {" | ".join(finalResult[0].keys())} |\n'
outString += f'| {" | ".join(["---" for _ in finalResult[0].keys()])} |\n'
for e in finalResult:
    outString += f'| {e["name"]} '
    outString += f'| {" | ".join([str(round(v,4)) for k, v in e.items() if k != "name"])} |\n'
print(outString)
with open('response_pySIPFENN.md', 'w') as f:
    f.write(outString)

print('\n\n\nAll Done!')
