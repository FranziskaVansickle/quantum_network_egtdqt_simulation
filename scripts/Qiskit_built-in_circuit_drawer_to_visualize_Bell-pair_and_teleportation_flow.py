# -*- coding: utf-8 -*-
"""
Created on Fri May  9 11:05:02 2025

@author: VANTROPY
"""

# scripts/draw_egtdqt_circuit.py
import os
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt

# 1) Build the EGT/DQT circuit
qc = QuantumCircuit(3, 3)
# Bell pair (q0 ↔ q2)
qc.h(0)
qc.cx(0, 2)
qc.barrier()

# Ancilla‐assisted teleport (q1 → q2 via q0)
qc.cx(1, 0)
qc.h(1)
qc.barrier()
qc.cx(0, 2)
qc.cz(1, 2)
qc.barrier()

# Measurement
qc.measure([0, 1, 2], [0, 1, 2])

# 2) Draw using the explicit drawer
fig = circuit_drawer(qc, output='mpl', style={'dpi':100})
fig.set_size_inches(8, 4)
fig.tight_layout()

# 3) Save to docs/
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root  = os.path.abspath(os.path.join(script_dir, ".."))
docs_dir   = os.path.join(repo_root, "docs")
os.makedirs(docs_dir, exist_ok=True)

out_path = os.path.join(docs_dir, "egtdqt_circuit_diagram.png")
fig.savefig(out_path, dpi=100)
print(f"Saved circuit diagram to {out_path}")

