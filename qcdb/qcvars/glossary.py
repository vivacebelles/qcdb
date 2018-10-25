qcvardefs = {}
#.. include:: autodoc_abbr_options_c.rst
#
#.. _`apdx:psivariables_alpha`:
#
#PSI Variables by Alpha
#======================
#
#.. note:: Lowercase letters in PSI variable names represent portions of
#   the variable name that vary by root number, calculation order, etc.
#   See text for fuller description.


_dip_components = ['X', 'Y', 'Z']
_quad_components = ['XX', 'XY', 'XZ', 'YY', 'YZ', 'ZZ']

qcvardefs['(T) CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The coupled-cluster perturbative triples correction.

.. psivar:: (T) CORRECTION ENERGY
"""}

qcvardefs['[T] CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The coupled-cluster bracket perturbative triples correction.

.. psivar:: [T] CORRECTION ENERGY
"""}

#.. psivar:: A-(T) CORRECTION ENERGY
#
#   The coupled-cluster asymmetric perturbative triples correction [H].
#
#.. psivar:: MP4(T) CORRECTION ENERGY
#
#   The MP4 triples component [H]. Quantity is second right-hand term in
#   Eq. :eq:`MP4terms`.
#
#.. psivar:: AAA (T) CORRECTION ENERGY
#   AAB (T) CORRECTION ENERGY
#   ABB (T) CORRECTION ENERGY
#   BBB (T) CORRECTION ENERGY
#
#   Spin components of the UHF-based coupled-cluster perturbative triples correction [H].

#.. psivar:: ACPF DIPOLE X
#   ACPF DIPOLE Y
#   ACPF DIPOLE Z
#
#   The three components of the dipole [Debye] for the 
#   averaged coupled-pair functional level of theory.
#
#.. psivar:: ACPF QUADRUPOLE XX
#   ACPF QUADRUPOLE XY
#   ACPF QUADRUPOLE XZ
#   ACPF QUADRUPOLE YY
#   ACPF QUADRUPOLE YZ
#   ACPF QUADRUPOLE ZZ
#
#   The six components of the quadrupole [Debye Ang] for the 
#   averaged coupled-pair functional level of theory.
#
#.. psivar:: ACPF TOTAL ENERGY
#   ACPF CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the averaged coupled-pair functional level of theory.
#
#.. psivar:: AQCC DIPOLE X
#   AQCC DIPOLE Y
#   AQCC DIPOLE Z
#
#   The three components of the dipole [Debye] for the 
#   averaged quadratic coupled-cluster level of theory.
#
#.. psivar:: AQCC QUADRUPOLE XX
#   AQCC QUADRUPOLE XY
#   AQCC QUADRUPOLE XZ
#   AQCC QUADRUPOLE YY
#   AQCC QUADRUPOLE YZ
#   AQCC QUADRUPOLE ZZ

#   The six components of the quadrupole [Debye Ang] for the 
#   averaged quadratic coupled-cluster level of theory.
#
#.. psivar:: AQCC TOTAL ENERGY
#   AQCC CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the averaged quadratic coupled-cluster level of theory.
#.. psivar:: BRUECKNER CONVERGED
#
#   Value 1 (0) when the Brueckner orbitals have (have not) converged.
#
#.. psivar:: CBS TOTAL ENERGY
#   CBS CORRELATION ENERGY
#   CBS REFERENCE ENERGY
#
#   The total electronic energy [H] and its breakdown into reference total
#   energy [H] and correlation correction components [H] for the compound
#   method requested through cbs().
#
#.. psivar:: CC ROOT n DIPOLE X
#   CC ROOT n DIPOLE Y 
#   CC ROOT n DIPOLE Z
#
#   The three components of the dipole [Debye] for the requested
#   coupled cluster level of theory and root *n* (number starts at GS = 0).
#
#.. psivar:: CC ROOT n QUADRUPOLE XX
#   CC ROOT n QUADRUPOLE XY
#   CC ROOT n QUADRUPOLE XZ
#   CC ROOT n QUADRUPOLE YY
#   CC ROOT n QUADRUPOLE YZ
#   CC ROOT n QUADRUPOLE ZZ
#
#   The six components of the quadrupole [Debye Ang] for the requested
#   coupled cluster level of theory and root *n* (numbering starts at GS = 0).
#
#.. psivar:: CC ROOT n TOTAL ENERGY
#   CC ROOT n CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the requested coupled cluster level of theory and root 
#   *n* (numbering starts at GS = 0).
#
#.. psivar:: CC TOTAL ENERGY
#   CC CORRELATION ENERGY
#
#.. psivar:: CC T1 DIAGNOSTIC
#   CC D1 DIAGNOSTIC
#   CC NEW D1 DIAGNOSTIC
#   CC D2 DIAGNOSTIC
#
#   Diagnostic of multireference character.
#
#.. psivar:: CC2 TOTAL ENERGY
#   CC2 CORRELATION ENERGY
#   CC3 TOTAL ENERGY
#   CC3 CORRELATION ENERGY
#   CC4 TOTAL ENERGY
#   CC4 CORRELATION ENERGY
#   CCnn TOTAL ENERGY
#   CCnn CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the requested approximate coupled-cluster (CC2, CC3, up to CC\ *nn*)
#   level of theory.
#
#.. psivar:: CC DIPOLE X
#   CC DIPOLE Y
#   CC DIPOLE Z
#
#   The three components of the dipole [Debye] for the requested
#   coupled cluster level of theory and root.

#.. psivar:: CC2 DIPOLE POLARIZABILITY @ xNM
#
#   The dipole polarizability [au] calculated at the CC2 level 
#   for a given (x) wavelength, (x) rounded to nearest integer. 
#
#.. psivar:: CC2 SPECIFIC ROTATION (LEN) @ xNM
#
#   The specific rotation [deg/(dm (g/cm^3))] calculated at the CC2 level in the
#   length gauge for a given (x) wavelength, (x) rounded to nearest integer.
#
#.. psivar:: CC2 SPECIFIC ROTATION (VEL) @ xNM
#
#   The specific rotation [deg/(dm (g/cm^3))] calculated at the CC2 level in the 
#   velocity gauge for a given (x) wavelength, (x) rounded to nearest integer.
#
#.. psivar:: CC2 SPECIFIC ROTATION (MVG) @ xNM
#
#   The specific rotation [deg/(dm (g/cm^3))] calculated at the CC2 level in the 
#   modified velocity gauge for a given (x) wavelength, (x) rounded to nearest integer.
#
#.. psivar:: CC QUADRUPOLE XX
#   CC QUADRUPOLE XY
#   CC QUADRUPOLE XZ
#   CC QUADRUPOLE YY
#   CC QUADRUPOLE YZ
#   CC QUADRUPOLE ZZ
#
#   The six components of the quadrupole [Debye Ang] for the requested
#   coupled cluster level of theory and root.
#
#.. psivar:: CCSD TOTAL ENERGY
#   CCSD CORRELATION ENERGY
#   CCSDT TOTAL ENERGY
#   CCSDT CORRELATION ENERGY
#   CCSDTQ TOTAL ENERGY
#   CCSDTQ CORRELATION ENERGY
#   CCn TOTAL ENERGY
#   CCn CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the requested full coupled-cluster (CCSD, CCSDT, up to CC\ *n*) 
#   level of theory.
#
#.. psivar:: CCSD(T) TOTAL ENERGY
#   CCSD(T) CORRELATION ENERGY
#   A-CCSD(T) TOTAL ENERGY
#   A-CCSD(T) CORRELATION ENERGY
#   CCSDT(Q) TOTAL ENERGY
#   CCSDT(Q) CORRELATION ENERGY
#   CC(n-1)(n) TOTAL ENERGY
#   CC(n-1)(n) CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the perturbatively corrected coupled-cluster (CCSD(T), a-CCSD(T), CCSDT(Q), 
#   up to CC(\ *n*\ -1)(\ *n*\ ) level of theory.
#
#.. psivar:: CCSDT-1a TOTAL ENERGY
#   CCSDT-1a CORRELATION ENERGY
#   CCSDTQ-1a TOTAL ENERGY
#   CCSDTQ-1a CORRELATION ENERGY
#   CCn-1a TOTAL ENERGY
#   CCn-1a CORRELATION ENERGY
#   
#   The total electronic energy [H] and correlation energy component [H]
#   for the approximate coupled-cluster (CCSD(T)-1a, CCSDT(Q)-1a, 
#   up to CC\ *n*\ -1a) level of theory.
#
#.. psivar:: CCSDT-1b TOTAL ENERGY
#   CCSDT-1b CORRELATION ENERGY
#   CCSDTQ-1b TOTAL ENERGY
#   CCSDTQ-1b CORRELATION ENERGY
#   CCn-1b TOTAL ENERGY
#   CCn-1b CORRELATION ENERGY
#   
#   The total electronic energy [H] and correlation energy component [H]
#   for the approximate coupled-cluster (CCSD(T)-1b, CCSDT(Q)-1b, 
#   up to CC\ *n*\ -1b) level of theory.
#
#.. psivar:: CCSDT-3 TOTAL ENERGY
#   CCSDT-3 CORRELATION ENERGY
#   CCSDTQ-3 TOTAL ENERGY
#   CCSDTQ-3 CORRELATION ENERGY
#   CCn-3 TOTAL ENERGY
#   CCn-3 CORRELATION ENERGY
#   
#   The total electronic energy [H] and correlation energy component [H]
#   for the approximate coupled-cluster (CCSD(T)-3, CCSDT(Q)-3, 
#   up to CC\ *n*\ -3) level of theory.
#
#.. psivar:: CCSD(T)_L TOTAL ENERGY
#   CCSD(T)_L CORRELATION ENERGY
#   CCSDT(Q)_L TOTAL ENERGY
#   CCSDT(Q)_L CORRELATION ENERGY
#   CC(n-1)(n)_L TOTAL ENERGY
#   CC(n-1)(n)_L CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the approximate coupled-cluster (CCSD(T)_L, CCSDT(Q)_L, 
#   up to CC(\ *n*\ -1)(\ *n*\ )L level of theory.
#
#.. psivar:: CCSD DIPOLE POLARIZABILITY @ xNM
#
#   The dipole polarizability [au] calculated at the CCSD level 
#   for a given (x) wavelength, (x) rounded to nearest integer. 

#.. psivar:: CCSD SPECIFIC ROTATION (LEN) @ xNM
#
#   The specific rotation [deg/(dm (g/cm^3))] calculated at the CCSD level in the
#   length gauge for a given (x) wavelength, (x) rounded to nearest integer.
#
#.. psivar:: CCSD SPECIFIC ROTATION (VEL) @ xNM
#
#   The specific rotation [deg/(dm (g/cm^3))] calculated at the CCSD level in the 
#   velocity gauge for a given (x) wavelength, (x) rounded to nearest integer.
#
#.. psivar:: CCSD SPECIFIC ROTATION (MVG) @ xNM
#
#   The specific rotation [deg/(dm (g/cm^3))] calculated at the CCSD level in the 
#   modified velocity gauge for a given (x) wavelength, (x) rounded to nearest integer.
#
#.. psivar:: CEPA(0) DIPOLE X
#   CEPA(0) DIPOLE Y
#   CEPA(0) DIPOLE Z
#
#   The three components of the dipole [Debye] for the 
#   coupled electron pair approximation variant 0 level of theory.
#
#.. psivar:: CEPA(0) QUADRUPOLE XX
#   CEPA(0) QUADRUPOLE XY
#   CEPA(0) QUADRUPOLE XZ
#   CEPA(0) QUADRUPOLE YY
#   CEPA(0) QUADRUPOLE YZ
#   CEPA(0) QUADRUPOLE ZZ
#
#   The six components of the quadrupole [Debye Ang] for the 
#   coupled electron pair approximation variant 0 level of theory.

#.. psivar:: CEPA(0) TOTAL ENERGY
#   CEPA(0) CORRELATION ENERGY
#   CEPA(1) TOTAL ENERGY
#   CEPA(1) CORRELATION ENERGY
#   CEPA(2) TOTAL ENERGY
#   CEPA(2) CORRELATION ENERGY
#   CEPA(3) TOTAL ENERGY
#   CEPA(3) CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the requested variant of coupled electron pair approximation level of theory.
#
#.. psivar:: CFOUR ERROR CODE
#
#   The non-zero return value from a Cfour execution.
#
#.. psivar:: CI DIPOLE X
#   CI DIPOLE Y
#   CI DIPOLE Z
#
#   The three components of the dipole [Debye] for the requested
#   configuration interaction level of theory and root.
#
#.. psivar:: CI QUADRUPOLE XX
#   CI QUADRUPOLE XY
#   CI QUADRUPOLE XZ
#   CI QUADRUPOLE YY
#   CI QUADRUPOLE YZ
#   CI QUADRUPOLE ZZ

#   The six components of the quadrupole [Debye Ang] for the requested
#   configuration interaction level of theory and root.
#
#.. psivar:: CI ROOT n -> ROOT m DIPOLE X
#   CI ROOT n -> ROOT m DIPOLE Y
#   CI ROOT n -> ROOT m DIPOLE Z
#
#   The three components of the transition dipole [Debye] between roots *n*
#   and *m* for the requested configuration interaction level of theory.
#
#.. psivar:: CI ROOT n -> ROOT m QUADRUPOLE XX
#   CI ROOT n -> ROOT m QUADRUPOLE XY
#   CI ROOT n -> ROOT m QUADRUPOLE XZ
#   CI ROOT n -> ROOT m QUADRUPOLE YY
#   CI ROOT n -> ROOT m QUADRUPOLE YZ
#   CI ROOT n -> ROOT m QUADRUPOLE ZZ
#
#   The three components of the transition quadrupole [Debye Ang] between
#   roots *n* and *m* for the requested configuration interaction level of
#   theory.
#
#.. psivar:: CI ROOT n DIPOLE X
#   CI ROOT n DIPOLE Y 
#   CI ROOT n DIPOLE Z
#
#   The three components of the dipole [Debye] for the requested
#   configuration interaction level of theory and root *n*.
#
#.. psivar:: CI ROOT n QUADRUPOLE XX
#   CI ROOT n QUADRUPOLE XY
#   CI ROOT n QUADRUPOLE XZ
#   CI ROOT n QUADRUPOLE YY
#   CI ROOT n QUADRUPOLE YZ
#   CI ROOT n QUADRUPOLE ZZ
#
#   The six components of the quadrupole [Debye Ang] for the requested
#   configuration interaction level of theory and root *n*.

#.. psivar:: CI ROOT n TOTAL ENERGY
#   CI ROOT n CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the requested configuration interaction level of theory and root 
#   *n* (numbering starts at 0).
#
#.. psivar:: CI STATE-AVERAGED TOTAL ENERGY
#   CI STATE-AVERAGED CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for state-averaged CI/CASSCF levels of theory.
#   
#.. psivar:: CI TOTAL ENERGY
#   CI CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the requested configuration interaction level of theory and root.
#
#.. psivar:: CISD DIPOLE X
#   CISD DIPOLE Y
#   CISD DIPOLE Z
#
#   The three components of the dipole [Debye] for the 
#   configuration interaction singles and doubles level of theory and root.
#
#.. psivar:: CISD QUADRUPOLE XX
#   CISD QUADRUPOLE XY
#   CISD QUADRUPOLE XZ
#   CISD QUADRUPOLE YY
#   CISD QUADRUPOLE YZ
#   CISD QUADRUPOLE ZZ
#
#   The six components of the quadrupole [Debye Ang] for the 
#   configuration interaction singles and doubles level of theory and root.

#.. psivar:: CISD TOTAL ENERGY
#   CISD CORRELATION ENERGY
#   CISDT TOTAL ENERGY
#   CISDT CORRELATION ENERGY
#   CISDTQ CORRELATION ENERGY
#   CISDTQ TOTAL ENERGY
#   CIn CORRELATION ENERGY
#   CIn TOTAL ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the labeled configuration interaction level of theory and root.
#   *n* is CI order for *n* > 4.
#
#.. psivar:: CP-CORRECTED 2-BODY INTERACTION ENERGY
#
#   The interaction energy [H] considering only two-body interactions,
#   computed with counterpoise correction.
#   Related variable :psivar:`UNCP-CORRECTED 2-BODY INTERACTION ENERGY <UNCP-CORRECTED2-BODYINTERACTIONENERGY>`.
#
#   .. math:: E_{\text{IE}} = E_{dimer} - \sum_{monomer}^{n}{E_{monomer}^{\text{CP}}}

qcvardefs['CURRENT CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The correlation energy corresponding to the :psivar:`CURRENT ENERGY <CURRENTENERGY>` variable.
"""}

qcvardefs['CURRENT ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The total electronic energy of the most recent stage of a
   calculation (frequently overwritten). This is the quantity tracked by
   the geometry optimizer.
"""}

qcvardefs['CURRENT GRADIENT'] = {
    'units': 'Eh/a0',
    'glossary': """
   The total electronic gradient of the most recent stage of a
   calculation (frequently overwritten). This is the quantity tracked by
   the geometry optimizer.
"""}

qcvardefs['CURRENT HESSIAN'] = {
    'units': 'Eh/a0/a0',
    'glossary': """
   The total electronic Hessian of the most recent stage of a
   calculation.
"""}

qcvardefs['CURRENT REFERENCE ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The total electronic energy of the reference stage corresponding to
   the :psivar:`CURRENT ENERGY <CURRENTENERGY>` variable.
"""}

qcvardefs['CURRENT DIPOLE X'] = {
    'units': 'D',
    'glossary': """
   The X component of the dipole [Debye] for the requested
   level of theory and root.
"""}

qcvardefs['CURRENT DIPOLE Y'] = {
    'units': 'D',
    'glossary': """
   The Y component of the dipole [Debye] for the requested
   level of theory and root.
"""}

qcvardefs['CURRENT DIPOLE Z'] = {
    'units': 'D',
    'glossary': """
   The Z component of the dipole [Debye] for the requested
   level of theory and root.
"""}

def define_prop_qcvars(mtd, extra=''):
    mtd = mtd.upper()

    for i in _dip_components:
        qcvardefs['{} DIPOLE {}'.format(mtd, i)] = {
            'units': 'D',
            'glossary': """
           The {} component of the dipole for the {} level of theory
           and root *n* (number starts at GS = 0). {}
    """.format(i, mtd, extra)}
    
    for i in _quad_components:
        qcvardefs['{} QUADRUPOLE {}'.format(mtd, i)] = {
            'units': 'D A',
            'glossary': """
           The {} component of the quadrupole for the {} level of theory
           and root *n* (number starts at GS = 0). {}
    """.format(i, mtd, extra)}


def define_scf_qcvars(mtd, is_dft=True, extra='', is_dh=False):
    global qcvardefs

    if mtd + 'TOTAL ENERGY' not in qcvardefs:
        qcvardefs['{} TOTAL ENERGY'.format(mtd)] = {
            'units': 'Eh',
            'glossary': """
           The total electronic energy for the {} level of theory. {}
        """.format(mtd, extra)}

    if is_dft:
        qcvardefs['{} FUNCTIONAL TOTAL ENERGY'.format(mtd)] = {
            'units': 'Eh',
            'glossary': r""" 
           The total electronic energy for the underlying functional of the
           requested DFT method {}, without any dispersion correction. {}
        """.format(mtd, extra)}

    if is_dft and is_dh:
        qcvardefs['{} DOUBLE-HYBRID CORRECTION ENERGY'.format(mtd)] = {
            'units': 'Eh',
            'glossary': r"""
           The scaled MP2 correlation energy correction appended to an 
           underlying functional {}. {}
        """.format(mtd, extra)}

    for i in _dip_components:
        qcvardefs['{} DIPOLE {}'.format(mtd, i)] = {
            'units': 'D',
            'glossary': """
           The {} component of the dipole for the {} level of theory. {}
    """.format(i, mtd, extra)}
    
    for i in _quad_components:
        qcvardefs['{} QUADRUPOLE {}'.format(mtd, i)] = {
            'units': 'D A',
            'glossary': """
           The {} component of the quadrupole for the {} level of theory. {}
    """.format(i, mtd, extra)}


def define_dashd_qcvars(fctl, dashes, extra=''):
    for dd in dashes:
        qcvardefs['{}-{} DISPERSION CORRECTION ENERGY'.format(fctl.upper(), dd.upper())] = {
            'units': 'Eh',
            'glossary': """
   The dispersion correction defined for appending to underlying functional
   {} when a DFT-D method is requested. {}
    """.format(fctl, extra)}

        qcvardefs['{}-{} DISPERSION CORRECTION GRADIENT'.format(fctl.upper(), dd.upper())] = {
            'units': 'Eh',
            'glossary': """
   The gradient to the dispersion correction defined for appending to underlying functional
   {} when a DFT-D method is requested. {}
    """.format(fctl, extra)}

        qcvardefs['{}-{} TOTAL ENERGY'.format(fctl.upper(), dd.upper())] = {
            'units': 'Eh',
            'glossary': r""" 
           The total electronic energy for the underlying functional of the
           requested DFT method {}, with dispersion correction. {}
        """.format(fctl, extra)}

#TRACELESS QUADRUPOLE POLARIZABILITY XZYY
#.. psivar:: db_name DATABASE MEAN ABSOLUTE DEVIATION
#
#   The mean absolute deviation [\ |kcalpermol|\ ] of the requested method
#   *name* from the stored reference values for the requested reactions in
#   database *db_name*. If no reference is available, this will be a large
#   and nonsensical value.
#
#   .. math:: \frac{1}{n}\sum_{rxn}^{n}{| \textsf{\textsl{name}}_{rxn}-\text{REF}_{rxn} | }
#
#.. psivar:: db_name DATABASE MEAN SIGNED DEVIATION
#
#   The mean deviation [\ |kcalpermol|\ ] of the requested method *name*
#   from the stored reference values for the requested reactions in
#   database *db_name*. If no reference is available, this will be a large
#   and nonsensical value.
#
#   .. math:: \frac{1}{n}\sum_{rxn}^{n}{\textsf{\textsl{name}}_{rxn}-\text{REF}_{rxn}}
#
#.. psivar:: db_name DATABASE ROOT-MEAN-SQUARE SIGNED DEVIATION
#
#   The rms deviation [\ |kcalpermol|\ ] of the requested method *name*
#   from the stored reference values for the requested reactions in
#   database *db_name*. If no reference is available, this will be a large
#   and nonsensical value.
#
#   .. math:: \sqrt{\frac{1}{n}\sum_{rxn}^{n}{(\textsf{\textsl{name}}_{rxn}-\text{REF}_{rxn})^2}}

qcvardefs['DFT FUNCTIONAL TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for the underlying functional of the
   requested DFT method, without any dispersion correction; the first four
   terms in Eq. :eq:`SCFterms` or :eq:`DFTterms`. Quantity
   :math:`E_{\text{FCTL}}` in Eqs.  :eq:`SCFterms` and :eq:`DFTterms`.
   Unless the method includes a dispersion correction, this quantity is
   equal to :psivar:`SCF TOTAL ENERGY <SCFTOTALENERGY>`.
"""}

qcvardefs['DFT TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for the requested DFT method, 
   :math:`E_{\text{DFT}}` in Eq. :eq:`DFTterms`.

   .. math:: 
      :nowrap:
      :label: DFTterms

         \begin{align*}
            E_{\text{DFT}} & = E_{NN} + E_{1e^-} + E_{2e^-} + E_{xc} + E_{\text{-D}} + E_{\text{DH}} \\
                           & = E_{\text{FCTL}} + E_{\text{-D}} + E_{\text{DH}} \\
                           & = E_{\text{SCF}} + E_{\text{DH}}
         \end{align*}

   Unless the method is a DFT double-hybrid, this quantity is equal to
   :psivar:`SCF TOTAL ENERGY <SCFTOTALENERGY>`. If the method is neither a
   double-hybrid, nor dispersion corrected, this quantity is equal to
   :psivar:`DFT FUNCTIONAL TOTAL ENERGY <DFTFUNCTIONALTOTALENERGY>`.
"""}

qcvardefs['DFT VV10 ENERGY'] = {
    'units': 'Eh',
    'glossary' : r"""
   The functional energy contribution to the total SCF energy (DFT only).
"""}

qcvardefs['DFT XC ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The functional energy contribution [H] to the total SCF energy (DFT only).
   Quantity :math:`E_{xc}` in Eqs. :eq:`SCFterms` and :eq:`DFTterms`.
"""}

qcvardefs['DISPERSION CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The dispersion correction appended to an underlying functional
   when a DFT-D method is requested. Quantity :math:`E_{\text{-D}}`
   in Eqs. :eq:`SCFterms` and :eq:`DFTterms`.
"""}

qcvardefs['DISPERSION CORRECTION GRADIENT'] = {
    'units': 'Eh/a0',
    'glossary': r"""
   The gradient to the dispersion correction appended to an underlying functional
   when a DFT-D method is requested. Quantity :math:`E_{\text{-D}}`
"""}

qcvardefs['DOUBLE-HYBRID CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The scaled MP2 correlation energy correction [H] appended to an 
   underlying functional when a DH-DFT method is requested.
   Quantity :math:`E_{\text{DH}}` in Eq. :eq:`DFTterms`.
"""}

#.. psivar:: FCI TOTAL ENERGY
#   FCI CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the full configuration interaction level of theory.

qcvardefs['HF TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for the Hartree--Fock method, without
   any dispersion correction; the first three (or four, since 
   :math:`E_{xc} = 0`) terms in Eq. :eq:`SCFterms`. Quantity :math:`E_{\text{HF}}`
   in Eq. :eq:`SCFterms`.
"""}

qcvardefs['HF TOTAL HESSIAN'] = {
    'units': 'Eh/a0/a0',
    'glossary': """
   The total electronic energy for the Hartree-Fock method.
"""}

qcvardefs['DMRG-SCF TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The total DMRG total electonic energy. Not unique b/c oribital spaces
"""}

qcvardefs['DMRG-CASPT2 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': """
   The total DMRG plus CASPT2 total electonic energy. Not unique b/c orbital spaces.
"""}

#.. psivar:: LCC2 (+LMP2) TOTAL ENERGY
#
#   The total electronic energy [H] for the local CC2 level of theory.
#
#.. psivar:: LCCSD (+LMP2) TOTAL ENERGY
#
#   The total electronic energy [H] for the local CCSD level of theory.

qcvardefs['MP2 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy 
   for the MP2 level of theory.
"""}

qcvardefs['MP2 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component
   for the MP2 level of theory.

.. psivar:: MP2 CORRELATION ENERGY

   The MP2 correlation energy for the requested DFT method, 
   :math:`E_{\text{MP2corl}}` in Eq. :eq:`MP2corl`.

   .. math:: 
      :nowrap:
      :label: MP2corl

         \begin{align*}
            E_{\text{MP2corl}} & = E_{\text{S}} + E_{\text{SS}} + E_{\text{OS}} \\
                               & = E_{\text{S}} + E_{\text{D}} \\
#                               & = E_{NN} + E_{1e^-} + E_{2e^-} + E_{xc} + E_{\text{-D}} + E_{\text{DH}} \\
#                               & = E_{\text{FCTL}} + E_{\text{-D}} + E_{\text{DH}} \\
#                               & = E_{\text{SCF}} + E_{\text{DH}}
         \end{align*}

#   Unless the method is a DFT double-hybrid, this quantity is equal to
#   :psivar:`SCF TOTAL ENERGY <SCFTOTALENERGY>`. If the method is neither a
#   double-hybrid, nor dispersion corrected, this quantity is equal to
#   :psivar:`DFT FUNCTIONAL TOTAL ENERGY <DFTFUNCTIONALTOTALENERGY>`.

"""}

qcvardefs['MP2 SAME-SPIN CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The unscaled portion of the MP2 correlation energy
   from same-spin or triplet doubles correlations.

   canonical_corl(os_scale=1, ss_scale=1) = singles + os_scale * (tot_corl - ss_corl) + ss_scale * ss_corl
   :math:`E_{\text{SS}}` in Eq. :eq:`MP2corl`.
"""}

qcvardefs['MP2 OPPOSITE-SPIN CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The unscaled portion of the MP2 correlation energy
   from opposite-spin or singlet doubles correlations.
   :math:`E_{\text{OS}}` in Eq. :eq:`MP2corl`.
"""}

qcvardefs['MP2 SINGLES ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The singles portion of the MP2 correlation energy.
   Zero except in ROHF.
   :math:`E_{\text{S}}` in Eq. :eq:`MP2corl`.
"""}

qcvardefs['MP2 DOUBLES ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The doubles portion of the MP2 correlation energy
   including same-spin and opposite-spin correlations.
   :math:`E_{\text{D}}` in Eq. :eq:`MP2corl`.
"""}

qcvardefs['SCS-MP2 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The MP2-like correlation energy by reweighting 
   MP2 DOUBLES ENERGY by 6/5 opposite-spin
   and 1/3 same-spin contributions, with any singles
   carried along.
"""}

qcvardefs['SCS-MP2 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total energy built from SCS-MP2 CORRELATION ENERGY
   and reference.
"""}

qcvardefs['CUSTOM SCS-MP2 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   Changeable quantity. The MP2-like correlation
   energy by any reweighting of SAME-SPIN or
   OPPOSITE-SPIN components. Depending on weights,
   this may equal any of MP2, SCS-MP2, SCS(N)-MP2,
   etc. quantities.
"""}

qcvardefs['CUSTOM SCS-MP2 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total energy built from 
   CUSTOM SCS-MP2 CORRELATION ENERGY and reference.
"""}

qcvardefs['SCS(N)-MP2 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'doi': '10.1021/ct6002737',
    'glossary': r"""
   The MP2-like correlation energy by reweighting 
   MP2 DOUBLES ENERGY by 0 opposite-spin
   and 1.76 same-spin contributions, with any singles
   carried along.
"""}

qcvardefs['SCS(N)-MP2 TOTAL ENERGY'] = {
    'units': 'Eh',
    'doi': '10.1021/ct6002737',
    'glossary': r"""
   The total energy built from SCS(N)-MP2 CORRELATION ENERGY
   and reference.
"""}

qcvardefs['CUSTOM D2 DISPERSION CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   Label for D2-formula dispersion correction when
   parameters match no functional.
"""}

qcvardefs['CUSTOM D2 DISPERSION CORRECTION GRADIENT'] = {
    'units': 'Eh',
    'glossary': r"""
   Label for D2-formula dispersion correction gradient when
   parameters match no functional.
"""}

qcvardefs[''] = {
    'units': 'Eh',
    'glossary': r"""
"""}

qcvardefs[''] = {
    'units': 'Eh',
    'glossary': r"""
"""}

qcvardefs[''] = {
    'units': 'Eh',
    'glossary': r"""
"""}

qcvardefs[''] = {
    'units': 'Eh',
    'glossary': r"""
"""}

qcvardefs[''] = {
    'units': 'Eh',
    'glossary': r"""
"""}

qcvardefs[''] = {
    'units': 'Eh',
    'glossary': r"""
"""}

qcvardefs['MP2.5 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for the MP2.5 level of theory.
"""}

qcvardefs['MP2.5 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component for the MP2.5 level of theory.
"""}

#.. psivar:: MP3 TOTAL ENERGY
#   MP3 CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the MP3 level of theory.
#
#.. psivar:: MP4(SDQ) TOTAL ENERGY
#   MP4(SDQ) CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the MP4 singles, doubles, quadruples level of theory.  Quantity
#   :psivar:`MP4(SDQ) CORRELATION ENERGY <MP4(SDQ)CORRELATIONENERGY>` is
#   first right-hand term in Eq. :eq:`MP4terms`.
#
#.. psivar:: MP4 TOTAL ENERGY
#   MP4 CORRELATION ENERGY
#   MP4(SDTQ) TOTAL ENERGY
#   MP4(SDTQ) CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the full MP4 level of theory. Quantity :psivar:`MP4 CORRELATION
#   ENERGY <MP4CORRELATIONENERGY>` / :psivar:`MP4(SDTQ) CORRELATION ENERGY
#   <MP4(SDTQ)CORRELATIONENERGY>` is left-hand term in Eq. :eq:`MP4terms`.
#
#   .. math:: E_{\text{MP4}} = E_{\text{MP4(SDQ)}} + E_{\text{MP4(T)}}
#      :label: MP4terms
#
#.. psivar:: MPn TOTAL ENERGY
#   MPn CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the labeled |MollerPlesset| perturbation theory level.
#   *n* is MP perturbation order.

qcvardefs['MP3 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for 3-order Perturbation theory.
"""}

qcvardefs['MP3 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component for 3-order Perturbation theory.
"""}

qcvardefs['MP4 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for 4-order Perturbation theory.
"""}

qcvardefs['MP4 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component for 4-order Perturbation theory.
"""}

qcvardefs['MP5 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for 5-order Perturbation theory.
"""}

qcvardefs['MP5 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component for 5-order Perturbation theory.
"""}

qcvardefs['MP6 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy for 6-order Perturbation theory.
"""}

qcvardefs['MP6 CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component for 6-order Perturbation theory.
"""}

qcvardefs['CCSD TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy 
   for the coupled cluster singles and doubles level of theory.
"""}

qcvardefs['CCSD CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component
   for the coupled cluster singles and doubles level of theory.

.. psivar:: CCSD CORRELATION ENERGY

   The CCSD correlation energy for the requested DFT method, 
   :math:`E_{\text{CCSDcorl}}` in Eq. :eq:`CCSDcorl`.

   .. math:: 
      :nowrap:
      :label: CCSDcorl

         \begin{align*}
#            E_{\text{CCSDcorl}} & = E_{\text{S}} + E_{\text{SS}} + E_{\text{OS}} \\
#                               & = E_{\text{S}} + E_{\text{D}} \\
         \end{align*}

"""}

qcvardefs['CCSDT (PBE) TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy 
   for the coupled cluster singles, doubles, and triples level of theory.
"""}

qcvardefs['CCSDT (PBE) CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component
   for the coupled cluster singles, doubles, and triples level of theory.

.. psivar:: CCSDT CORRELATION ENERGY

   The CCSDT correlation energy for the requested DFT method, 
   :math:`E_{\text{CCSDcorl}}` in Eq. :eq:`CCSDcorl`.

   .. math:: 
      :nowrap:
      :label: CCSDcorl

         \begin{align*}
#            E_{\text{CCSDcorl}} & = E_{\text{S}} + E_{\text{SS}} + E_{\text{OS}} \\
#                               & = E_{\text{S}} + E_{\text{D}} \\
         \end{align*}

"""}

qcvardefs['CCSD SAME-SPIN CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The unscaled portion of the CCSD correlation energy
#   from same-spin or triplet doubles correlations.

#   canonical_corl(os_scale=1, ss_scale=1) = singles + os_scale * (tot_corl - ss_corl) + ss_scale * ss_corl
#   :math:`E_{\text{SS}}` in Eq. :eq:`CCSDcorl`.
"""}

qcvardefs['CCSD OPPOSITE-SPIN CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
#   The unscaled portion of the CCSD correlation energy
#   from opposite-spin or singlet doubles correlations.
#   :math:`E_{\text{OS}}` in Eq. :eq:`CCSDcorl`.
"""}

qcvardefs['CCSD(T) TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy 
   for the coupled cluster singles and doubles plus perturbative triples level of theory.
"""}

qcvardefs['CCSD(T) CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component
   for the coupled cluster singles and doubles plus perturbative triples level of theory.
"""}

qcvardefs['CCSDT TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy 
   for the coupled cluster singles and doubles plus perturbative triples level of theory.
"""}

qcvardefs['CCSDT CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component
   for the coupled cluster singles and doubles plus perturbative triples level of theory.
"""}

qcvardefs['CCSD[T] TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy 
   for the coupled cluster singles and doubles plus bracket perturbative triples level of theory.
"""}

qcvardefs['CCSD[T] CORRELATION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The correlation energy component
   for the coupled cluster singles and doubles plus bracket perturbative triples level of theory.
"""}

qcvardefs['NUCLEAR REPULSION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The nuclear repulsion energy contribution [H] to the total SCF energy.
   Quantity :math:`E_{NN}` in Eq. :eq:`SCFterms`.

   .. math:: E_{NN} = \sum_{i, j<i}^{N_{atom}}\frac{Z_i Z_j}{|\mathbf{R}_i - \mathbf{R}_j|}
      :label: ENN
"""}  # TODO EFP?

#.. psivar:: OCEPA(0) TOTAL ENERGY
#   OCEPA(0) CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the orbital-optimized CEPA(0) level of theory.
#
#.. psivar:: OMP2 TOTAL ENERGY
#   OMP2 CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the orbital-optimized MP2 level of theory.
#
#.. psivar:: OMP3 TOTAL ENERGY
#   OMP3 CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the orbital-optimized MP3 level of theory.

qcvardefs['ONE-ELECTRON ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The one-electron energy contribution [H] to the total SCF energy.
   Quantity :math:`E_{1e^-}` in Eq. :eq:`SCFterms`.
"""}

#.. psivar:: QCISD TOTAL ENERGY
#   QCISD CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the quadratic configuration interaction singles and doubles level
#   of theory.
#
#.. psivar:: QCISD(T) TOTAL ENERGY
#   QCISD(T) CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the quadratic configuration interaction singles and doubles with
#   perturbative triples correction level of theory.
#
#.. psivar:: SAPT DISP ENERGY
#   SAPT ELST ENERGY
#   SAPT EXCH ENERGY
#   SAPT IND ENERGY
#
#   Respectively, the dispersion, electrostatics, exchange, and induction
#   components of the total electronic interaction energy [H] for the the
#   requested SAPT level of theory. The sum of these four components yields
#   :psivar:`SAPT TOTAL ENERGY <SAPTTOTALENERGY>`.
#
#.. psivar:: SAPT TOTAL ENERGY
#
#   The total electronic interaction energy [H] for the requested SAPT
#   level of theory.
#
#.. psivar:: SAPT0 TOTAL ENERGY
#   SSAPT0 TOTAL ENERGY
#   SAPT2 TOTAL ENERGY
#   SAPT2+ TOTAL ENERGY
#   SAPT2+(3) TOTAL ENERGY
#   SAPT2+3 TOTAL ENERGY
#
#   The total electronic interaction energy [H] for the labeled SAPT level
#   of theory.
#
#.. psivar:: SAPT2+(CCD) TOTAL ENERGY
#   SAPT2+(3)(CCD) TOTAL ENERGY
#   SAPT2+3(CCD) TOTAL ENERGY
#
#   The total electronic interaction energy [H] for the labeled SAPT level
#   of theory that incorporates coupled-cluster dispersion.
#
#.. psivar:: SAPT2+DMP2 TOTAL ENERGY
#   SAPT2+(3)DMP2 TOTAL ENERGY
#   SAPT2+3DMP2 TOTAL ENERGY
#   SAPT2+(CCD)DMP2 TOTAL ENERGY
#   SAPT2+(3)(CCD)DMP2 TOTAL ENERGY
#   SAPT2+3(CCD)DMP2 TOTAL ENERGY
#
#   The total electronic interaction energy [H] for the labeled SAPT level
#   of theory that incorporates MP2 induction correction.
#
#.. psivar:: SCF DIPOLE X
#   SCF DIPOLE Y
#   SCF DIPOLE Z
#
#   The three components of the SCF dipole [Debye].

qcvardefs['SCF ITERATIONS'] = {
    'units': '',
    'glossary': r"""
   The number of iterations in final? SCF set.
"""}

#.. psivar:: SCF QUADRUPOLE XX
#   SCF QUADRUPOLE XY
#   SCF QUADRUPOLE XZ
#   SCF QUADRUPOLE YY
#   SCF QUADRUPOLE YZ
#   SCF QUADRUPOLE ZZ
#
#   The six components of the SCF quadrupole [Debye Ang].

qcvardefs['SCF TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The total electronic energy of the SCF stage of the calculation.
   The :psivar:`CORRELATION ENERGY` variables from subsequent stages of a
   calculation are often the corresponding :psivar:`TOTAL ENERGY`
   variables less this quantity. Constructed from Eq. :eq:`SCFterms`,
   where this quantity is :math:`E_{\text{SCF}}`.

   .. math:: 
      :nowrap:
      :label: SCFterms

         \begin{align*}
            E_{\text{SCF}} & = E_{NN} + E_{1e^-} + E_{2e^-} + E_{xc} + E_{\text{-D}} \\
                           & = E_{\text{FCTL/HF}} + E_{\text{-D}}
         \end{align*}

   Unless the method includes a dispersion correction, this quantity is equal to :psivar:`HF TOTAL ENERGY <HFTOTALENERGY>` (for HF) or
   :psivar:`DFT FUNCTIONAL TOTAL ENERGY <DFTFUNCTIONALTOTALENERGY>` (for
   DFT). Unless the method is a DFT double-hybrid, this quantity is equal
   to :psivar:`DFT TOTAL ENERGY <DFTTOTALENERGY>`.
"""}

qcvardefs['SCF TOTAL HESSIAN'] = {
    'units': 'Eh/a0/a0',
    'glossary': """
   The total electronic Hessian of the SCF stage of a calculation.
   May be HF or DFT.
"""}

qcvardefs['TWO-ELECTRON ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   The two-electron energy contribution [H] to the total SCF energy.
   Quantity :math:`E_{2e^-}` in Eq. :eq:`SCFterms`.
"""}

qcvardefs['DLDF-DAS2009 DISPERSION CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   disp correction attaching to DLDF+D09 ORPHAN
"""}

qcvardefs['WB97-CHG DISPERSION CORRECTION ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   disp correction attaching to DLDF+D09 ORPHAN
"""}

qcvardefs['B97-D TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   functional energy for B97-D w/ disp correction ORPHAN
"""} 

qcvardefs['B97-D FUNCTIONAL TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   functional energy for B97-D w/o disp correction ORPHAN
"""} 

# why not normal for this?
qcvardefs['B97-0 TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   functional energy for original hybrid B97-0 w/o disp correction ORPHAN
"""} 

qcvardefs['B97-0 FUNCTIONAL TOTAL ENERGY'] = {
    'units': 'Eh',
    'glossary': r"""
   functional energy for original hybrid B97-0 w/o disp correction ORPHAN
"""} 

#.. psivar:: UNCP-CORRECTED 2-BODY INTERACTION ENERGY
#
#   The interaction energy [H] considering only two-body interactions,
#   computed without counterpoise correction.
#   Related variable :psivar:`CP-CORRECTED 2-BODY INTERACTION ENERGY <CP-CORRECTED2-BODYINTERACTIONENERGY>`.
#
#   .. math:: E_{\text{IE}} = E_{dimer} - \sum_{monomer}^{n}{E_{monomer}^{\text{unCP}}}
#
#.. psivar:: ZAPTn TOTAL ENERGY
#   ZAPTn CORRELATION ENERGY
#
#   The total electronic energy [H] and correlation energy component [H]
#   for the labeled Z-averaged perturbation theory level.
#   *n* is ZAPT perturbation order.
define_scf_qcvars('HF', is_dft=False)
define_scf_qcvars('B3LYP')
define_scf_qcvars('B3LYP5')
define_scf_qcvars('SCF', is_dft=False, extra=' This is a generic HF/DFT quantity and not necessarily aligned across different calcs.')
define_scf_qcvars('B2PLYP', is_dh=True)
define_scf_qcvars('DSD-PBEP86', is_dh=True)
define_scf_qcvars('WPBE', is_dh=False)
define_scf_qcvars('WB97', is_dh=False)
define_scf_qcvars('PBE', is_dh=False)
define_scf_qcvars('CAM-B3LYP', is_dh=False)
define_scf_qcvars('DLDF+D09', is_dh=False)
define_scf_qcvars('WB97X', is_dh=False)
define_scf_qcvars('PBE0-2', is_dh=True)
define_scf_qcvars('PBE0', is_dh=False)
define_scf_qcvars('SVWN', is_dh=False)
define_scf_qcvars('WB97X-D', is_dh=False)
define_scf_qcvars('PW91', is_dh=False)
define_scf_qcvars('BLYP', is_dh=False)
define_scf_qcvars('PW86PBE', is_dh=False)
define_scf_qcvars('FT97', is_dh=False)
define_scf_qcvars('BOP', is_dh=False)
define_scf_qcvars('MPWPW', is_dh=False)
define_scf_qcvars('SOGGA11', is_dh=False)
define_scf_qcvars('BP86', is_dh=False)
define_scf_qcvars('B86BPBE', is_dh=False)
define_scf_qcvars('PW6B95', is_dh=False)
define_scf_qcvars('MN15', is_dh=False)
define_scf_qcvars('SOGGA11-X', is_dh=False)
define_scf_qcvars('B2GPPLYP', is_dh=True)
define_scf_qcvars('PTPSS', is_dh=True)
define_scf_qcvars('PWPB95', is_dh=True)
define_scf_qcvars('DSD-BLYP', is_dh=True), 
define_scf_qcvars('PBE0-DH', is_dh=True)
#define_scf_qcvars('B97-D', is_dh=False)
define_dashd_qcvars('bp86', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('b3lyp', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('b3lyp5', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('b2plyp', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('pbe', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('b97', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('blyp', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('pbe0', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
define_dashd_qcvars('wpbe', dashes=['d2', 'd3', 'd3(bj)', 'd3m', 'd3m(bj)'])
#define_dashd_qcvars('wb97x', dashes=['d'])

define_prop_qcvars('ccsd')
define_prop_qcvars('cc')  # TODO reconsider
