# -*- coding: utf-8 -*-
"""
Created on Thu May  8 20:34:58 2025

@author: VANTROPY
"""


# entanglement_simulator.py

"""
Simulate Entanglement Distribution via EGT and DQT
Author: Franziska Vansickle
Date: May 2025
Description:
This script compares EGT and DQT-based entanglement distribution under noisy conditions
using ancilla qubits and source-destination teleportation logic.

Tools: Qiskit AerSimulator, QuantumCircuit, ancilla-based teleportation
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_bell_pair(circuit, q0, q1):
    circuit.h(q0)
    circuit.cx(q0, q1)
    return circuit

def teleport(circuit, src, ancilla, dest):
    circuit.cx(src, ancilla)
    circuit.h(src)
    circuit.barrier()
    circuit.cx(ancilla, dest)
    circuit.cz(src, dest)
    return circuit

def simulate_circuit(circuit, shots=1024):
    simulator = AerSimulator()
    # run returns a job; .result() returns results
    result = simulator.run(circuit, shots=shots).result()
    return result.get_counts()

def run_egt():
    print("Running EGT simulation...")
    qc = QuantumCircuit(3, 3)
    create_bell_pair(qc, 0, 2)  # EGT: entangled qubit 0 and 2
    teleport(qc, 1, 0, 2)       # teleport qubit 1 to qubit 2 via ancilla 0
    qc.measure([0, 1, 2], [0, 1, 2])
    return simulate_circuit(qc)

def run_dqt():
    print("Running DQT simulation...")
    qc = QuantumCircuit(3, 3)
    create_bell_pair(qc, 0, 1)  # DQT: entangled qubit 0 and 1
    teleport(qc, 2, 0, 1)       # teleport qubit 2 to qubit 1 via ancilla 0
    qc.measure([0, 1, 2], [0, 1, 2])
    return simulate_circuit(qc)

if __name__ == "__main__":
    egt_results = run_egt()
    dqt_results = run_dqt()

    print("EGT Results:", egt_results)
    print("DQT Results:", dqt_results)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    plot_histogram(egt_results, ax=ax[0], title="EGT Output")
    plot_histogram(dqt_results, ax=ax[1], title="DQT Output")
    plt.tight_layout()
    plt.savefig("docs/simulation_results.png")
    plt.show()
