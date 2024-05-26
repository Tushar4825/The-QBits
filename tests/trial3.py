import numpy as np
from qiskit import QuantumCircuit, transpile, Aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
from random import choice
from typing import List, Dict
import matplotlib.pyplot as plt

# Function to add a random single-qubit gate
def add_random_single_qubit_gate(qc: QuantumCircuit, qubit: int) -> None:
    gates = ['x', 'y', 'z', 'h', 's', 't']
    gate = choice(gates)
    if gate == 'x':
        qc.x(qubit)
    elif gate == 'y':
        qc.y(qubit)
    elif gate == 'z':
        qc.z(qubit)
    elif gate == 'h':
        qc.h(qubit)
    elif gate == 's':
        qc.s(qubit)
    elif gate == 't':
        qc.t(qubit)

# Function to add a random two-qubit gate
def add_random_two_qubit_gate(qc: QuantumCircuit, qubit1: int, qubit2: int) -> None:
    gates = ['cx', 'cz', 'swap']
    gate = choice(gates)
    if gate == 'cx':
        qc.cx(qubit1, qubit2)
    elif gate == 'cz':
        qc.cz(qubit1, qubit2)
    elif gate == 'swap':
        qc.swap(qubit1, qubit2)

# Function to create a random quantum circuit
def create_random_quantum_circuit(num_qubits: int) -> QuantumCircuit:
    qc = QuantumCircuit(num_qubits, num_qubits)
    for qubit in range(num_qubits):
        add_random_single_qubit_gate(qc, qubit)
    add_random_two_qubit_gate(qc, 0, 1)
    add_random_two_qubit_gate(qc, 1, 2)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

# Function to simulate measurements
def simulate_measurements(qc: QuantumCircuit, shots: int = 1024) -> Dict[str, int]:
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    return result.get_counts(compiled_circuit)

# Main function to create the circuit, and simulate measurements
def main():
    num_qubits = 3
    qc = create_random_quantum_circuit(num_qubits)
    print("Quantum Circuit:")
    circuit_drawer(qc, output='mpl', style='clifford').show()

    counts = simulate_measurements(qc)
    print("\nMeasurement counts:")
    print(counts)
    plot_histogram(counts)
    plt.show()

# Unit tests for gate functions
def test_add_random_single_qubit_gate():
    qc = QuantumCircuit(1)
    add_random_single_qubit_gate(qc, 0)
    assert qc

def test_add_random_two_qubit_gate():
    qc = QuantumCircuit(2)
    add_random_two_qubit_gate(qc, 0, 1)
    assert qc

# Run the tests and main function
if __name__ == "__main__":
    test_add_random_single_qubit_gate()
    test_add_random_two_qubit_gate()
    main()
