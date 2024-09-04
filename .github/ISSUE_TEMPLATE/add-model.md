---
name: Request Addition of ML Model to the MPDD Ecosystem (Expert)
about: Template for requesting to add a new model into the MPDD ecosystem.
title: "[ENH]"
labels: enhancement
assignees: ''

---

We are happy to quickly add any structure-informed model which is a plug-and-play addition to our infrastructure, which will generally mean it either:
- Utilizes already implemented representation, feature set, or its subset. Please check below as appropriate:
    - [ ] My model uses [`KS2022`](https://pysipfenn.readthedocs.io/en/v0.15.0/source/pysipfenn.descriptorDefinitions.html) or its subset.
    - [ ] My model uses [`ALIGNN`](https://github.com/usnistgov/alignn/blob/main/alignn/models/alignn.py#L190) graph representation.
    - [ ] My model is a refitting or a variation of [`CHGNet`](https://github.com/CederGroupHub/chgnet/blob/main/chgnet/model/model.py#L33)
    - [ ] My model is available from a public citable source like Zenodo (preferred) or figshare.
    - [ ] My model can be fetched within 30s, corresponding to ~2GB on Zenodo or 250MB on figshare.
    - [ ] My model can run single-threaded in under 500ms / structure
    - [ ] My model can run single-threaded in under 5s / structure

- Is a lightweight tool, which can be quickly installed and run. Please check below as appropriate:
    - [ ] My model is well maintained and has been used in past research.
    - [ ] My model is actively tested at least weekly and has been well-maintained for at least 6 months.
    - [ ] My model is available from a public citable source like Zenodo (preferred) or figshare.
    - [ ] My model can be fetched within 30s, corresponding to ~2GB on Zenodo or 250MB on figshare.
    - [ ] My model can run single-threaded in under 500ms / structure
    - [ ] My model can run single-threaded in under 5s / structure
 
If it does not fall into the above categories, please dont get discouraged and still let us know! It will be much more work on our side, but we will probably be happy to work with you. To get started on that, please explain it in a few sentences.
