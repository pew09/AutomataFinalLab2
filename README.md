#Mealy Machine (DOT)


<img width="642" height="498" alt="mealy_machine" src="https://github.com/user-attachments/assets/fdf6bdaa-35a7-4abd-92a4-860af2ac779c" />


digraph Mealy {
    rankdir=LR;
    node [shape = circle, fontsize=12, style=filled, fillcolor=lightyellow];

    A [label="A"];
    B [label="B"];
    C [label="C"];
    D [label="D"];
    E [label="E"];

    // Transitions: format "input/output"
    A -> A [label="0/A"];
    A -> B [label="1/B"];
    B -> C [label="0/A"];
    B -> D [label="1/B"];
    C -> D [label="0/C"];
    C -> B [label="1/B"];
    D -> B [label="0/B"];
    D -> C [label="1/C"];
    E -> D [label="0/C"];
    E -> E [label="1/C"];
}



#Converted Mealy Machine (DOT)

<img width="817" height="612" alt="graphviz" src="https://github.com/user-attachments/assets/987eec60-2228-4c4d-8949-badef4da77df" />



digraph Moore {
    rankdir=LR;
    node [shape = circle, fontsize=12, style=filled, fillcolor=lightblue];

    // Moore states (state_output)
    A_A [label="A/A"];
    B_B [label="B/B"];
    C_A [label="C/A"];
    C_C [label="C/C"];
    D_B [label="D/B"];
    D_C [label="D/C"];
    E_C [label="E/C"];

    // Transitions (input only, since output tied to destination)
    A_A -> A_A [label="0"];
    A_A -> B_B [label="1"];
    B_B -> C_A [label="0"];
    B_B -> D_B [label="1"];
    C_A -> D_C [label="0"];
    C_A -> B_B [label="1"];
    D_B -> B_B [label="0"];
    D_B -> C_C [label="1"];
    C_C -> D_C [label="0"];
    C_C -> B_B [label="1"];
    D_C -> B_B [label="0"];
    D_C -> C_C [label="1"];
    E_C -> D_C [label="0"];
    E_C -> E_C [label="1"];
}
