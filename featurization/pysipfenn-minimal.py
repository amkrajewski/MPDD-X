# ****************  pySIPFENN  **********************
print('Importing pySIPFENN...', flush=True)
import sys
from pysipfenn import Calculator
import numpy as np
from natsort import natsorted
try:
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
    print('pySIPFENN Done!\n\n\n', flush=True)

    # Rename key 'SIPFENN_Krajewski2022_NN30' to 'SIPFENN_NN30-OQMD [eV/atom]' and then order keys
    finalResult = []
    for e in sipfennResult:
        finalResult.append({
            'name': e['name'], 
            'SIPFENN_NN30-OQMD [eV/atom]': e['SIPFENN_Krajewski2022_NN30']})
    finalResult = natsorted(finalResult, key=lambda e: e['name'])

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
except Exception as e:
    print(f"An error occurred: {str(e)}", file=sys.stderr)
    sys.exit(1)
finally:
    if 'c' in locals():
        del c