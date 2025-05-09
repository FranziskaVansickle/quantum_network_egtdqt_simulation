# -*- coding: utf-8 -*-
"""
Created on Fri May  9 11:05:02 2025

@author: VANTROPY
"""

import os
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Build circuit as before…
qc = QuantumCircuit(3, 3)
qc.h(0); qc.cx(0, 2); qc.barrier()
qc.cx(1, 0); qc.h(1); qc.barrier()
qc.cx(0, 2); qc.cz(1, 2); qc.barrier()
qc.measure([0,1,2],[0,1,2])

# Draw
fig = qc.draw(output='mpl', fold=100)
fig.set_size_inches(8, 4)
plt.tight_layout()

# Compute absolute path to docs folder
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, ".."))
docs_dir = os.path.join(repo_root, "docs")
os.makedirs(docs_dir, exist_ok=True)

# Save into docs/
out_path = os.path.join(docs_dir, "egtdqt_circuit_diagram.png")
plt.savefig(out_path, dpi=100)
plt.show()

