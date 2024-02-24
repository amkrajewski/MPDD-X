print('Importing pymatgen...', flush=True)
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import natsort
import os
print('\n\n\nImporting Structures...', flush=True)

structures, names = [], []
files = os.listdir('structures')
files = natsort.natsorted(files)
for file in files:
    structures.append(Structure.from_file(f'structures/{file}'))
    names.append(file)
print(f'Found {len(structures)} structures.\nPerforming a quick analysis.', flush=True)
outString = "Structure Record:\n"
outString += f'| Name | Formula | Crytal Family | Space Group | Volume per Atom |\n'
outString += f'| --- | --- | --- | --- | --- |\n'

for s, n in zip(structures, names):
    sgA = SpacegroupAnalyzer(s)
    outString += f'| {n} | {s.formula} | {sgA.get_crystal_system()} | {sgA.get_space_group_symbol()} | {s.volume / s.num_sites:.3f} |\n'
print(outString)
with open('structureList.md', 'w') as f:
    f.write(outString)

print('\n\n\nAll Done!')