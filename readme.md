# KMB algorithm for Steiner Trees

### Python

```bash
cd python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### C++

```bash
cd cpp
cmake .
make
```

### To run KMB algorithm with `instance050` as input from `instances/` folder:

```bash
./cpp/build/kmb < instances/instance050.gr -o
```

### Flags

- `-o` to run in outer parallel mode
- `-i` to run in inner parallel mode
- `-b` to run in both parallel mode
- `-s` to run in sequential mode

### Run original research code

```bash
./cpp/build/og < instances/instance050.gr
```

## KMB Algorithm

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

## References

Pace Challenge 2018: [STP](https://pacechallenge.org/2018/)
<br />
ACM Research Paper : [Accelerating Computation of Steiner Trees on GPUs
](https://dl.acm.org/doi/abs/10.1007/s10766-021-00723-0)
