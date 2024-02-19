print('Importing pySIPFENN...', flush=True)
import pysipfenn
import numpy as np
# ****************  pySIPFENN  **********************
# Init
print('\n\n\nStarting pySIPFENN Run', flush=True)
c = pysipfenn.Calculator()
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

# *****************   ALIGNN    **********************
print('Importing MPDD-ALIGNN...', flush=True)
from alignn import pretrained
print('ALIGNN Running...', flush=True)
pretrained.download_default_models()
print('ALIGNN Models Downloaded!', flush=True)
alignnResult = pretrained.run_models_from_directory('structures', mode='serial')
print('ALIGNN Done!', flush=True)

# *********   Merge and write to file    **************
# Match results based on the `name` field
finalResult = []
for sr in sipfennResult:
    for ar in alignnResult:
        if sr['name'] == ar['name']:
            finalResult.append({**sr, **ar})
            break

# Order keys in order "name", "SIPFENN_*", "ALIGNN_*"
finalResult = [{**{'name': e['name']}, **{k: e[k] for k in e if k.startswith('SIPFENN')} , **{k: e[k] for k in e if k.startswith('ALIGNN')}} for e in finalResult]
print(finalResult, flush=True)
outString = f'| {" | ".join(finalResult[0].keys())} |\n'
outString += f'| {" | ".join(["---" for _ in finalResult[0].keys()])} |\n'
for e in finalResult:
    outString += f'| {e["name"]} '
    outString += f'| {" | ".join([str(round(v,4)) for k, v in e.items() if k != "name"])} |\n'
print(outString)
with open('response.md', 'w') as f:
    f.write(outString)

print('\n\n\nAll Done!')

