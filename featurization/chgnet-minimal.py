# ****************  CHGNet  **********************
print('Importing CHGNet...', flush=True)
import sys
from pymatgen.core import Structure
from tqdm import tqdm
import natsort
import time
from chgnet.model import CHGNet
from chgnet.model import StructOptimizer
try:
    print('CHGNet Ready...', flush=True)
    # Read all files from structures directory
    import os
    structures, names = [], []
    files = os.listdir('structures')
    files = natsort.natsorted(files)
    print(files)
    for file in files:
        structures.append(Structure.from_file(f'structures/{file}'))
        names.append(file)
    print(f'Found {len(structures)} structures.\nRunning energy predictions...', flush=True)

    # Init CHGNet Model and run energy predictions on initial structures
    t0 = time.time()
    chgnet = CHGNet.load()
    predictions = chgnet.predict_structure(
        structures,
        task='e',
        return_site_energies = False,
        return_atom_feas = False,
        return_crystal_feas = False,
        batch_size = 6
        )

    energies = [p['e'].item() for p in predictions]
    print(f'Energies obtained at {(time.time()-t0)/len(structures):.2f} s/structure', flush=True)
    print([round(e, 4) for e in energies], flush=True)

    print('Relaxing structures...', flush=True)
    # Relax structures
    t1 = time.time()
    relaxer = StructOptimizer()
    relaxed_structures = []
    for s in tqdm(structures):
        result = relaxer.relax(
            s, 
            fmax = 0.2,
            steps = 50,
            relax_cell = True,
            ase_filter = "FrechetCellFilter",
            save_path = None,
            loginterval = 1,
            crystal_feas_save_path = None,
            verbose=True
            )
        relaxed_structures.append(result['final_structure'])
    print(f'Relaxation done at {(time.time()-t1)/len(structures):.2f} s/structure', flush=True)
    for struct, name in zip(relaxed_structures, names):
        struct.to(f'structures_relaxed/{name}')

    print('Running energy predictions on relaxed structures...', flush=True)
    # Run energy predictions on relaxed structures
    t2 = time.time()
    relaxed_predictions = chgnet.predict_structure(
        relaxed_structures,
        task='e',
        return_site_energies = False,
        return_atom_feas = False,
        return_crystal_feas = False,
        batch_size = 6
        )
    relaxed_energies = [p['e'].item() for p in relaxed_predictions]
    print(f'Energies obtained at {(time.time()-t2)/len(structures):.2f} s/structure', flush=True)
    print([round(e, 4) for e in relaxed_energies], flush=True)

    # Markdown output
    outString = '\nPlease note that these are *energies*, not *formation energies*.\n'
    outString += f'| Name | CHGNet_0.3.0-MP Energy [eV/atom] | CHGNet_0.3.0-MP Relaxed Energy [eV/atom] |\n'
    outString += f'| --- | --- | --- |\n'
    for n, e, re in zip(names, energies, relaxed_energies):
        outString += f'| {n} | {round(e, 4)} | {round(re, 4)} |\n'
    with open('response_CHGNet.md', 'w') as f:
        f.write(outString)

    print('CHGNet Done!', flush=True)
except Exception as e:
    print(f"An error occurred: {str(e)}", file=sys.stderr)
    sys.exit(1)