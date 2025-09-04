from qiskit import QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

def quantum_perceptron_and(input_a, input_b):
    """
    Creates and executes a quantum circuit to perform the AND operation.
    
    Args:
        input_a (int): First classical input (0 or 1).
        input_b (int): Second classical input (0 or 1).
        
    Returns:
        dict: The measurement results.
    """
    
    # Create a quantum circuit with 3 qubits and 1 classical bit
    # q[0] and q[1] are inputs, q[2] is the output
    qc = QuantumCircuit(3, 1)
    
    # Encode the classical inputs into the quantum state
    # If input is 1, apply an X gate to flip the qubit from |0> to |1>
    if input_a == 1:
        qc.x(0)
    if input_b == 1:
        qc.x(1)

    # Use a barrier for visual separation in the circuit diagram
    qc.barrier()
    
    # The Toffoli gate (CCX) implements the AND logic
    # It flips the target qubit (q[2]) only if both control qubits (q[0], q[1]) are |1>
    qc.ccx(0, 1, 2)
    
    # Use a barrier for visual separation
    qc.barrier()
    
    # Measure the output qubit (q[2]) and store the result in the classical bit (c[0])
    qc.measure(2, 0)
    
    return qc

# Create a list of all input combinations
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Create a quantum simulator
backend = Aer.get_backend('qasm_simulator')

for a, b in inputs:
    # Get the quantum circuit for the current inputs
    qc = quantum_perceptron_and(a, b)
    
    # Draw the circuit for visualization
    print(f"--- Circuit for inputs ({a}, {b}) ---")
    print(qc)
    
    # Execute the circuit on the simulator
    job = execute(qc, backend, shots=1024)
    result = job.result()
    counts = result.get_counts()
    
    # The most probable result is our answer
    # This will be '0' or '1'
    predicted_output = max(counts, key=counts.get)
    
    print(f"Input: ({a}, {b}) -> Predicted Output: {predicted_output}")
    print("Measurement Counts:", counts)
    print("---------------------------------------")

    # Optional: Plot the histogram of results
    # plot_histogram(counts)



