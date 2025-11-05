# Moore Machine Simulation (Converted from Mealy)
moore = {
    "A_A": {"0": "A_A", "1": "B_B"},
    "B_B": {"0": "C_A", "1": "D_B"},
    "C_A": {"0": "D_C", "1": "B_B"},
    "D_B": {"0": "B_B", "1": "C_C"},
    "C_C": {"0": "D_C", "1": "B_B"},
    "D_C": {"0": "B_B", "1": "C_C"},
    "E_C": {"0": "D_C", "1": "E_C"}
}

outputs = {
    "A_A": "A",
    "B_B": "B",
    "C_A": "A",
    "D_B": "B",
    "C_C": "C",
    "D_C": "C",
    "E_C": "C"
}

def moore_output(input_str, start="A_A"):
    state = start
    output = outputs[state]  # Moore outputs before processing inputs
    for symbol in input_str:
        state = moore[state][symbol]
        output += outputs[state]
    return output

# Test
inputs = ["00110", "11001", "1010110", "101111"]
for inp in inputs:
    print(f"Input: {inp} → Output: {moore_output(inp)}")
