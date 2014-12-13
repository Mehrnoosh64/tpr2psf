This script reads GROMACS .tpr file and produces .psf and .prm files readable by  
[CP2K](http://cp2k.org/) and probably some other MM software. This script uses 
modified version of [grompy](https://github.com/GromPy/GromPy) GROMACS library 
python wrapper, written by Martin Hofling.

**NB.0:** The script works with GROMACS 4.5.5. For use with other versions you 
have to manually genenerate grompy/types.py using 
[ctypesgen](http://code.google.com/p/ctypesgen/)

**NB.1:** The script IS NOT capable of exact conversion between tpr and psf/prm 
topology/force field representation. Respective energies calculated by GROMACS 
and CP2K/FIST match in case of bonds, angles and sometimes dihedrals.  Nonbonded 
interactions (Coulomb and VdW, both long range and 1-4) are different for most 
of tested systems. Gradients calculated by both codes for some large system 
correlate with covariance coefficient 0.4.

**REQUIREMENTS:**
* GROMACS dynamic libraries (libgmx*.so)
* Modified version of GromPy wrapper (distributed  with this script)

**USAGE:** tpr2psf.py system.tpr

Will produce system.psf and system.prm
