#! single-point DFT-CCSDT/sto-3g on water

import os
import sys
import utils
import addons
import qcdb

print('        <<< Literal input to NWChem >>>')
print(''' 
memory 600 mb

nwchem {
geometry
O     0.000000000000    0.000000000000   -0.065638538099
H     0.000000000000   -0.757480611647    0.520865616174
H     0.000000000000    0.757480611647    0.520865616174
end

basis spherical
* library sto-3g
end

dft
 xc b3lyp
 grid lebedev 99 11
 convergence density 1.e-12
end

tce
 dft
 ccsdt
 thresh 1.e-12
end

task tce energy
}

energy('nwchem')

clean()
clean_variables()
nwchem {}
''')
h2o= qcdb.set_molecule('''
        O     0.000000000000    0.000000000000   -0.065638538099
        H     0.000000000000   -0.757480611647    0.520865616174
        H     0.000000000000    0.757480611647    0.520865616174
        ''')

print(h2o)
qcdb.set_options({
    'memory': '600 mb',
    'basis': 'sto-3g',
    'nwchem_dft__convergence__density':1.0e-12,
    'task_tce': 'energy'
    #need dft_xc,grid and tce options
    })

print(qcdb.get_active_options().print_charged())

def check_dft(return_value, is_df):

print( '        <<< Translation of NWChem input to Psi4 format to NWChem >>>')
print('''
molecule {
O
H 1 R
H 1 R 2 A

R=0.958
A=104.5
}

set {
basis sto-3g
dft_spherical_points 302
dft_radial_points 99
reference rks #not necessary 
d_convergence 12
dft_functional b3lyp
nwchem_tce_thresh 1.0e-12
nwchem_tce_dft true
nwchem_tce ccsdt
}

energy('nwchem-tce')''')