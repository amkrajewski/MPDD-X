# MPDD-contribute (experimental!)

***This repository is a one stop solution for getting material properties with ML models while contributing to a community database.***

It is as simple as [**opening an issue**](https://github.com/amkrajewski/MPDD-contribute/issues/new?assignees=&labels=contrib&projects=&template=contribution-template.md&title=%5BIN%5D) and uploading a ZIP file with atomic structures in `POSCAR` or `CIF` format! One you do it, your atomic structures will be processed through several tools, described below, and returned a neat Markdown report.
- [`pySIPFENN`](https://github.com/PhasesResearchLab/pySIPFENN) framework, returning (1) array of descriptors (feature vectors) in Numpy `.npy` and `CSV` formats you can use for your ML modelling, alongside formation energy predictions.
- [`ALIGNN`](https://github.com/usnistgov/alignn) framework, returing (1) results from 7 ALIGNN models [specified here](https://github.com/amkrajewski/mpdd-alignn/blob/main/alignn/config.yaml) and (2) compressed graph representation files.
- [`CHGNet`](https://github.com/CederGroupHub/chgnet) model, returing (1) energy prediction for your input, (2) CHGNet-relaxed structures in the same format (`POSCAR`/`CIF`)as your input, and (3) energy prediction for the relaxed structures.

Notes:
- There is no hardcoded limit for the number of atomic structures you can submit, but (a) please consider avoiding running unnecessary calculations and (b) there can be a time limit for your submission processing, which you will likely hit if you submit more than 2000 typical structures or 500 large structres at once. You can monitor progress under Actions tab.
