#!/usr/bin/python
about = """
ABOUT:
This script  reads GROMACS .tpr file and produces .psf and .prm files readable by  CP2K[ http://cp2k.berlios.de/] and probably some other MM software.
This script uses modified version of GROMACS library python wrapper, written by Martin Hofling  [http://oldwww.gromacs.org/pipermail/gmx-developers/2009-March/003183.html].

NB: This script IS NOT capable of exact conversion between tpr and psf/prm topology/force field representation. Respective energies calculated by GROMACS and CP2K/FIST match in case of bonds, angles and sometimes dihedrals. Nonbonded interactions (Coulomb and VdW, both long range and 1-4) are different for most of tested systems. Gradients calculated by both codes for some large system correlate with covariance coefficient 0.4.

REQUIREMENTS:
* GROMACS dynamic libraries (libgmx*.so)
* Modified version of GromPy wrapper (distributed  with this script)

USAGE: tpr2psf.py system.tpr
Will produce system.psf and system.prm

AUTHOR: piton_at_erg.biophys.msu.ru
"""

import sys
import os.path
sys.path.append(os.path.dirname(sys.argv[0]))
import os
from grompy import types, tpxio
import ctypes

class STUFF:
  def __init__(self):
    pass

class TPR:

  fmt_psf_title = "PSF\n\n%8d !NTITLE\n%s"
  fmt_atoms_title = "%8d !NATOM: atoms"
  fmt_atom = "%8d %-4s %-4s %-4s %-4s %-4s %10.6f     %9.4f  %10d"
  fmt_bonds_title = "%8d !NBOND: bonds"
  fmt_bonds = " %7d %7d"
  fmt_angles_title = "%8d !NTHETA: angles"
  fmt_angles = " %7d %7d %7d"
  fmt_dih_title = "%8d !NPHI: dihedrals"
  fmt_idih_title = "%8d !NIMPHI: impropers"
  fmt_dih = " %7d %7d %7d %7d"

  def __init__(self, tpr_name):
    self.tpr = tpxio.tpxfile(tpr_name)
    # TOPOLOGY
    # Atoms
    self.atoms = []
    for i in range(self.tpr.top.atoms.nr):
      at = self.tpr.top.atoms.atom[i]
      self.atoms.append(STUFF())
      self.atoms[i].resi = at.resind+1
      self.atoms[i].chain = self.tpr.top.atoms.resinfo[at.resind].chainid
      self.atoms[i].resn = ctypes.string_at(self.tpr.top.atoms.resinfo[at.resind].name[0])
      self.atoms[i].nm = ctypes.string_at(self.tpr.top.atoms.atomname[i][0])
      self.atoms[i].ityp = at.type
      self.atoms[i].typ = ctypes.string_at(self.tpr.top.atoms.atomtype[i][0])
      self.atoms[i].q = at.q
      self.atoms[i].m = at.m
    
    # Bonds
    F_BONDS = types.F_BONDS
    bonds = self.tpr.top.idef.il[F_BONDS]
    self.bonds = []
    for i in range(bonds.nr/3):
      self.bonds.append(STUFF())
      self.bonds[i].typ = bonds.iatoms[3*i]
      self.bonds[i].atoms = (bonds.iatoms[3*i+1], bonds.iatoms[3*i+2])

    # Angles
    F_ANGLES = types.F_ANGLES
    angles = self.tpr.top.idef.il[F_ANGLES]
    self.angles = []
    for i in range(angles.nr/4):
      self.angles.append(STUFF())
      self.angles[i].typ = angles.iatoms[4*i]
      self.angles[i].atoms = (angles.iatoms[4*i+1], angles.iatoms[4*i+2], angles.iatoms[4*i+3])
    
    # Proper Dihedrals
    F_PDIHS = types.F_PDIHS
    pdihs = self.tpr.top.idef.il[F_PDIHS]
    self.pdihs = []
    for i in range(pdihs.nr/5):
      self.pdihs.append(STUFF())
      self.pdihs[i].typ = pdihs.iatoms[5*i]
      self.pdihs[i].atoms = (pdihs.iatoms[5*i+1], pdihs.iatoms[5*i+2], pdihs.iatoms[5*i+3], pdihs.iatoms[5*i+4])

    # RB Dihedrals
    F_RBDIHS = types.F_RBDIHS
    rbdihs = self.tpr.top.idef.il[F_RBDIHS]
    self.rbdihs = []
    for i in range(rbdihs.nr/5):
      self.rbdihs.append(STUFF())
      self.rbdihs[i].typ = rbdihs.iatoms[5*i]
      self.rbdihs[i].atoms = (rbdihs.iatoms[5*i+1], rbdihs.iatoms[5*i+2], rbdihs.iatoms[5*i+3], rbdihs.iatoms[5*i+4])

    # Improper dihedrals
    F_IDIHS = types.F_IDIHS
    idihs = self.tpr.top.idef.il[F_IDIHS]
    self.idihs = []
    for i in range(idihs.nr/5):
      self.idihs.append(STUFF())
      self.idihs[i].typ = idihs.iatoms[5*i]
      self.idihs[i].atoms = (idihs.iatoms[5*i+1], idihs.iatoms[5*i+2], idihs.iatoms[5*i+3], idihs.iatoms[5*i+4])

    # LJ 1-4
    F_LJ14 = types.F_LJ14
    nb14 = self.tpr.top.idef.il[F_LJ14]
    self.nb14 = []
    for i in range(nb14.nr/3):
      self.nb14.append(STUFF())
      self.nb14[i].typ = nb14.iatoms[3*i]
      self.nb14[i].atoms = (nb14.iatoms[3*i+1], nb14.iatoms[3*i+2])

    #FORCEFILED
    # Bonds
    self.par_bonds = {}
    for bond in self.bonds:
      if not bond.typ in self.par_bonds.keys():
        self.par_bonds[bond.typ] = STUFF()
        self.par_bonds[bond.typ].ftyp = self.tpr.top.idef.functype[bond.typ]
        if self.par_bonds[bond.typ].ftyp != types.F_BONDS:
          raise NameError, "Unsupported bond ftype"
        self.par_bonds[bond.typ].r = self.tpr.top.idef.iparams[bond.typ].harmonic.rA
        self.par_bonds[bond.typ].k = self.tpr.top.idef.iparams[bond.typ].harmonic.krA
        self.par_bonds[bond.typ].types = []
      atypes = (self.atoms[bond.atoms[0]].typ, self.atoms[bond.atoms[1]].typ)
      if not atypes in self.par_bonds[bond.typ].types:
        self.par_bonds[bond.typ].types.append( atypes )

    # Angles
    self.par_angles = {}
    for angle in self.angles:
      if not angle.typ in self.par_angles.keys():
        self.par_angles[angle.typ] = STUFF()
        self.par_angles[angle.typ].ftyp = self.tpr.top.idef.functype[angle.typ] 
        if self.par_angles[angle.typ].ftyp != types.F_ANGLES:
          raise NameError, "Unsupported angle ftype"
        self.par_angles[angle.typ].r = self.tpr.top.idef.iparams[angle.typ].harmonic.rA
        self.par_angles[angle.typ].k = self.tpr.top.idef.iparams[angle.typ].harmonic.krA
        self.par_angles[angle.typ].types = []
      atypes = self.atoms[angle.atoms[0]].typ, self.atoms[angle.atoms[1]].typ, self.atoms[angle.atoms[2]].typ
      if not atypes in self.par_angles[angle.typ].types:
        self.par_angles[angle.typ].types.append( atypes )

    # Proper Dihedrals
    self.par_pdihs = {}
    for pdih in self.pdihs:
      if not pdih.typ in self.par_pdihs.keys():
        self.par_pdihs[pdih.typ] = STUFF()
        self.par_pdihs[pdih.typ].ftyp = self.tpr.top.idef.functype[pdih.typ] 
        if self.par_pdihs[pdih.typ].ftyp != types.F_PDIHS:
          raise NameError, "Unsupported pdih ftype"
        self.par_pdihs[pdih.typ].phi = self.tpr.top.idef.iparams[pdih.typ].pdihs.phiA
        self.par_pdihs[pdih.typ].C = self.tpr.top.idef.iparams[pdih.typ].pdihs.cpA
        self.par_pdihs[pdih.typ].m = self.tpr.top.idef.iparams[pdih.typ].pdihs.mult
        self.par_pdihs[pdih.typ].types = []
      atypes = self.atoms[pdih.atoms[0]].typ, self.atoms[pdih.atoms[1]].typ, self.atoms[pdih.atoms[2]].typ, self.atoms[pdih.atoms[3]].typ
      if not atypes in self.par_pdihs[pdih.typ].types:
        self.par_pdihs[pdih.typ].types.append( atypes )

    # RB Dihedrals
    self.par_rbdihs = {}
    for rbdih in self.rbdihs:
      if not rbdih.typ in self.par_rbdihs.keys():
        self.par_rbdihs[rbdih.typ] = STUFF()
        self.par_rbdihs[rbdih.typ].ftyp = self.tpr.top.idef.functype[rbdih.typ] 
        if self.par_rbdihs[rbdih.typ].ftyp != types.F_RBDIHS:
          raise NameError, "Unsupported rbdih ftype"
        self.par_rbdihs[rbdih.typ].C = []
        for i in range(types.NR_RBDIHS):
          self.par_rbdihs[rbdih.typ].C.append(self.tpr.top.idef.iparams[rbdih.typ].rbdihs.rbcA[i])
        self.par_rbdihs[rbdih.typ].types = []
      atypes = self.atoms[rbdih.atoms[0]].typ, self.atoms[rbdih.atoms[1]].typ, self.atoms[rbdih.atoms[2]].typ, self.atoms[rbdih.atoms[3]].typ
      if not atypes in self.par_rbdihs[rbdih.typ].types:
        self.par_rbdihs[rbdih.typ].types.append( atypes )

    # IMPROPERS
    self.par_idihs = {}
    for idih in self.idihs:
      if not idih.typ in self.par_idihs.keys():
        self.par_idihs[idih.typ] = STUFF()
        self.par_idihs[idih.typ].ftyp = self.tpr.top.idef.functype[idih.typ] 
        if self.par_idihs[idih.typ].ftyp != types.F_IDIHS:
          raise NameError, "Unsupported idih ftype"
        self.par_idihs[idih.typ].phi = self.tpr.top.idef.iparams[idih.typ].harmonic.rA
        self.par_idihs[idih.typ].k = self.tpr.top.idef.iparams[idih.typ].harmonic.krA
        self.par_idihs[idih.typ].types = []
      atypes = self.atoms[idih.atoms[0]].typ, self.atoms[idih.atoms[1]].typ, self.atoms[idih.atoms[2]].typ, self.atoms[idih.atoms[3]].typ
      if not atypes in self.par_idihs[idih.typ].types:
        self.par_idihs[idih.typ].types.append( atypes )
    
    # NB LJ
    self.par_nb = {}
    for at in self.atoms:
      if not at.ityp in self.par_nb.keys():
        self.par_nb[at.ityp] = STUFF()
        self.par_nb[at.ityp].c6 = self.tpr.top.idef.iparams[at.ityp].lj.c6
        self.par_nb[at.ityp].c12 = self.tpr.top.idef.iparams[at.ityp].lj.c12
        self.par_nb[at.ityp].typ = []
      if not at.typ in self.par_nb[at.ityp].typ: self.par_nb[at.ityp].typ.append(at.typ)

    # NB LJ14
    self.par_nb14 = {}
    for nb14 in self.nb14:
      if not nb14.typ in self.par_nb14.keys():
        self.par_nb14[nb14.typ] = STUFF()
        self.par_nb14[nb14.typ].ftyp = self.tpr.top.idef.functype[nb14.typ]
        if self.par_nb14[nb14.typ].ftyp != types.F_LJ14:
          raise NameError, "Unsupported nb14 ftype %d" % nb14.typ
        self.par_nb14[nb14.typ].c6 = self.tpr.top.idef.iparams[nb14.typ].lj.c6
        self.par_nb14[nb14.typ].c12 = self.tpr.top.idef.iparams[nb14.typ].lj.c12
        self.par_nb14[nb14.typ].types = []
      atypes = (self.atoms[nb14.atoms[0]], self.atoms[nb14.atoms[1]])
      if not atypes in self.par_nb14[nb14.typ].types:
        self.par_nb14[nb14.typ].types.append( atypes )
        

  def print_psf(self, f=sys.stdout):
    # header
    print >>f, self.fmt_psf_title % (2, "Generated by tpr2psf\n"+self.tpr.title)
    print >>f, ""

    # Atoms
    print >>f, self.fmt_atoms_title % len(self.atoms)
    for i in range(len(self.atoms)):
      at = self.atoms[i]
      print >>f, self.fmt_atom % (i+1, at.chain, at.resi, at.resn, at.nm, at.typ, at.q, at.m, 0)
    print >>f, ""

    # Bonds
    print >>f, self.fmt_bonds_title % len(self.bonds),
    i=0
    for bond in self.bonds:
      if not i % 4: print >>f, ""
      print >>f, self.fmt_bonds % (bond.atoms[0]+1, bond.atoms[1]+1),
      i += 1
    print >>f, "\n"

    # Angles
    print >>f, self.fmt_angles_title % len(self.angles),
    i=0
    for angle in self.angles:
      if not i % 3: print >>f, ""
      print >>f, self.fmt_angles % (angle.atoms[0]+1, angle.atoms[1]+1, angle.atoms[2]+1),
      i += 1
    print >>f, "\n"

    # Dihedrals
    print >>f, self.fmt_dih_title % (len(self.rbdihs)+len(self.pdihs)),
    i=0
    for dih in self.rbdihs + self.pdihs:
      if not i % 2: print >>f, ""
      print >>f, self.fmt_dih % (dih.atoms[0]+1, dih.atoms[1]+1, dih.atoms[2]+1, dih.atoms[3]+1),
      i += 1
    print >>f, "\n"

    # Improper Dihedrals
    if (len(self.idihs)):
      print >>f, self.fmt_idih_title % len(self.idihs),
      i=0
      for idih in self.idihs:
        if not i % 2: print >>f, ""
        print >>f, self.fmt_dih % (idih.atoms[0]+1, idih.atoms[1]+1, idih.atoms[2]+1, idih.atoms[3]+1),
        i += 1
      print >>f, "\n"

  def print_ff(self, f=sys.stdout):
    j2cal = 1./4.1840
    nm2a = 10.
    print >>sys.stderr, "\nFF parameters"
    
    # Bonds
    print >>sys.stderr, "\tBonds: %d"  % len(self.par_bonds)
    print >>f, """
BONDS
!V(bond) = Kb(b - b0)**2
!Kb: kcal/mole/A**2
!b0: A
!atom type Kb          b0
    """
    for k in self.par_bonds:
      for atypes in self.par_bonds[k].types:
        print >>f, "%s %s  " % atypes,
        print >>f, "%.5f %.5f" % (self.par_bonds[k].k * 0.5 * j2cal / nm2a**2, self.par_bonds[k].r * nm2a)
    
    # Angles
    print >>sys.stderr, "\tAngles: %d"  % len(self.par_angles)
    print >>f, """
ANGLES
!V(angle) = Ktheta(Theta - Theta0)**2
!Ktheta: kcal/mole/rad**2
!Theta0: degrees
!atom types     Ktheta    Theta0
    """
    for k in self.par_angles:
      for atypes in self.par_angles[k].types:
        print >>f, "%s %s %s  " % atypes,
        print >>f, "%.5f %.4f" % (self.par_angles[k].k * 0.5 * j2cal, self.par_angles[k].r)

    # Dihedrals
    print >>f, """
DIHEDRALS
! V(dihedral) = Kchi(1 + cos(n(chi) - delta))
!Kchi: kcal/mole
!n: multiplicity
!delta: degrees
!atom types             Kchi    n   delta
    """
    # Propers
    print >>sys.stderr, "\tProper dihedrals: %d"  % len(self.par_pdihs)
    for typ,dih in self.par_pdihs.items():
      for atypes in dih.types:
        print >>f, "%s %s %s %s  " % atypes,
        print >>f, "%.5f %d %.4f" % (dih.C*j2cal, dih.m, dih.phi)

    # RB's
    print >>sys.stderr, "\tRyckaert-Belleman dihedrals: %d"  % len(self.par_rbdihs)
    for k in self.par_rbdihs:
      for atypes in self.par_rbdihs[k].types:
        C =  self.par_rbdihs[k].C
        F = [0., 0., 0., 0., 0.]
        F[0], F[1], F[2], F[3], F[4] = -(C[1]+3*C[3]/4+5*C[5]/8), -(C[2]/2+C[4]/2), -(C[3]/4+5*C[5]/16), -C[4]/8, -C[5]/16
        for i in range(len(F)): 
          if abs(F[i]) >= 1e-4:
            print >>f, "%s %s %s %s  " % atypes,
            print >>f, "%.5f %d %.4f" % (F[i]*j2cal, i+1, 180*(i%2))
        print >>f, ""

    # Improper Dihedrals
    print >>sys.stderr, "\tImproper dihedrals: %d"  % len(self.par_idihs)
    print >>f, """
IMPROPER
!V(improper) = Kpsi(psi - psi0)**2
!Kpsi: kcal/mole/rad**2
!psi0: degrees
!note that the second column of numbers (0) is ignored
!atom types           Kpsi         0         psi0
    """
    for k, imp in self.par_idihs.items():
      for atypes in imp.types:
        print >>f, "%s %s %s %s  " % atypes,
        print >>f, "%.5f 0 %.4f" % (imp.k*j2cal/2, imp.phi)

    # Nonbonded
    print >>sys.stderr, "\tNonbonded parameters: %d"  % len(self.par_nb)
    print >>f, """
NONBONDED
!V(Lennard-Jones) = Eps,i,j[(Rmin,i,j/ri,j)**12 - 2(Rmin,i,j/ri,j)**6]
!epsilon: kcal/mole, Eps,i,j = sqrt(eps,i * eps,j)
!Rmin/2: A, Rmin,i,j = Rmin/2,i + Rmin/2,j
!atom  ignored    epsilon      Rmin/2   ignored   eps,1-4       Rmin/2,1-4
    """
    for k,par_nb in self.par_nb.items():
      if self.par_nb[k].c6 != 0. and self.par_nb[k].c12 != 0.:
        par_nb.eps = par_nb.c6**2 / par_nb.c12 / 4
        par_nb.sig = (par_nb.c6/2/par_nb.eps)**(1./6.)
        par_nb.eps *= j2cal
        par_nb.sig *= nm2a
      else:
        par_nb.eps = 0.
        par_nb.sig = 0.
      for typ in par_nb.typ:
#        print >>f, k,
        print >>f, "%s  0.0  %.5f %.5f" % (typ, -par_nb.eps, par_nb.sig/2)
#        print >>f, "%s  0.0  %.5f %.5f" % (typ, -0, 0)

#        print >>f, "; %.5e %.5e" % (par_nb.c6, par_nb.c12)
#        print >>f, typ, 0, eps, sig/2

    print >>f, "\n\nEND"
#    print >>f, """
#NONBONDED14
#! atoms  epsilon, $kcal mole^{-1}$  sigma, $\AA$
#"""
"""
    for k,par_nb14 in self.par_nb14.items():
      if par_nb14.c6 != 0. and par_nb14.c12 != 0.:
        eps = par_nb14.c6**2 / par_nb14.c12 / 4
        sig = (par_nb14.c6/2/eps)**(1./6.)
        eps *= j2cal
        sig *= nm2a
      else:
        eps = 0.
        sig = 0.
      for atypes in self.par_nb14[k].types:
        print >>f, k,
        print >>f, "%s %s " % (atypes[0].typ, atypes[1].typ),
        print >>f, "%.5f %.5f  %.5f %.5f" % (eps, sig,  (self.par_nb[atypes[0].ityp].eps * self.par_nb[atypes[1].ityp].eps)**0.5, (self.par_nb[atypes[0].ityp].sig + self.par_nb[atypes[1].ityp].sig)/2),
        print >>f, "; %.5e %.5e" % (par_nb14.c6, par_nb14.c12)
"""

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print about
    sys.exit(1)
  tpr = TPR(sys.argv[1])
  psf = open(os.path.splitext(sys.argv[1])[0]+".psf", 'w')
  prm = open(os.path.splitext(sys.argv[1])[0]+".prm", 'w')
  tpr.print_psf(psf)
  tpr.print_ff(prm)
  psf.close()
  prm.close()
  sys.exit(0)


