# vsids
Experimental code and results for the paper titled "Understanding VSIDS Branching Heuristic in CDCL SAT Solvers"

Remaining code available in https://bitbucket.org/ezulkosk/sat_scripts

## Community

To print out a the community structure of a dimacs file:

```bash
pip install --user NetworkX
pip install --user python-louvain
python louvain.py myinstance.cnf > myinstance.cnf.cmty
```

This will print out a mapping (indexed from 0) to a community number (indexed from 0). Two variables map to the same community number if and only if the two variables belong to the same community computed by the Louvain method.

## Run AdaptVSIDS

```bash
make -C adaptvsids/
adaptvsids/core/adaptvsids myinstance.cnf
```

## Run mVSIDS

```bash
make -C mvsids
mvsids/core/mvsids myinstance.cnf
```

## Run cVSIDS

```bash
make -C cvsids
cvsids/core/cvsids myinstance.cnf
```

## Run TGC Experiment

Compute the TDC and TEC of the clause database on regular intervals.

```bash
make -C tkc
tkc/core/tkc -cmty-file=myinstance.cnf.cmty myinstance.cnf
```

## Run Bridge Experiment

Compute the number of picked, bumped, and learnt variables that are also bridge variables. The relevant statistics will be printed upon termination.

```bash
make -C countbridgemvsids/
countbridgemvsids/core/countbridgemvsids -cmty-file=myinstance.cnf.cmty myinstance.cnf
```
