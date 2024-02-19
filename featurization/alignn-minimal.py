# *****************   ALIGNN    **********************
print('Importing MPDD-ALIGNN...', flush=True)
from alignn import pretrained
print('ALIGNN Running...', flush=True)
pretrained.download_default_models(verbose=True, parallel=False)
print('ALIGNN Models Downloaded!', flush=True)
alignnResult = pretrained.run_models_from_directory('structures', mode='serial')
print('ALIGNN Done!', flush=True)

# Order keys in order "name", "SIPFENN_*", "ALIGNN_*"
finalResult = [{**{'name': e['name']}, **{k: e[k] for k in e if k.startswith('ALIGNN')}} for e in finalResult]
print(finalResult, flush=True)
outString = f'| {" | ".join(finalResult[0].keys())} |\n'
outString += f'| {" | ".join(["---" for _ in finalResult[0].keys()])} |\n'
for e in finalResult:
    outString += f'| {e["name"]} '
    outString += f'| {" | ".join([str(round(v,4)) for k, v in e.items() if k != "name"])} |\n'
print(outString)
with open('response_ALIGNN.md', 'w') as f:
    f.write(outString)

print('\n\n\nAll Done!')

