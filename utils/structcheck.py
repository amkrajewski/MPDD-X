print('Importing pymatgen...', flush=True)
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import natsort
import os
import sys
print('\n\n\nImporting Structures...', flush=True)

structures, names = [], []
files = os.listdir('structures')
files = natsort.natsorted(files)
for file in files:
    try:
        s = Structure.from_file(f'structures/{file}')
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)
    if s.is_valid(tol=0.1) and s.is_ordered and s.composition.valid:
        print(f"The structure was not valid, not ordered, or not occupied by a valid compositon.")
        structures.append(s)
        names.append(file)
    else:
        sys.exit(1)
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