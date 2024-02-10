# KMB algorithm for Steiner Trees

```bash
pip install -r requirements.txt
python main.py
```

## Algorithm

```code

Input: G = (V, E, W), L ⊆ V

// S1
G1(L, E1= ∅);

// S2
for u ∈ L do
    for v ∈ L do
        Path(u,v) = shortest_path(u, v);
        W1(u,v) = |Path(u,v)|;
        G1.add_edge(u,v);
    end for
end for

// S3
T1 = minimum_spanning_tree(G1);

// S4
G2 = ∅;
for (u,v) ∈ E1(T1) do
    G2 = G2 ∪ Path(u,v);
end for

// S5
T2 = minimum_spanning_tree(G2);

Output: T2
```
