# KMB algorithm for Steiner Trees

## Run

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

### KMB Algorithm Visualization

![KMB Algorithm Visualization](https://github.com/pratikpakhale/kmb-cpu/blob/main/kmb.png?raw=true)

### Steiner Tree

![Steiner Tree](https://github.com/pratikpakhale/kmb-cpu/blob/main/steiner.png?raw=true)

## Stats

[Processor Information](./processor_info.txt)

### Generate Results Data `results/`

Modify the `stats.sh` file as per requirements

```bash
cd cpp/
chmod +x ./stats.sh
./stats.sh kmb # to run kmb exec for 1 to 50 instances
```

### Parallel Execution Performance

![Parallel Execution Performance](https://github.com/pratikpakhale/kmb-cpu/blob/main/performance_seq_parallel.png?raw=true)

### Our vs Original | Accuracy

![Our vs Original | Accuracy](https://github.com/pratikpakhale/kmb-cpu/blob/main/accuracy.png?raw=true)

### Our vs Original | Time

![Our vs Original | Time](https://github.com/pratikpakhale/kmb-cpu/blob/main/time.png?raw=true)

## References

Pace Challenge 2018: [STP](https://pacechallenge.org/2018/)
<br />
ACM Research Paper : [Accelerating Computation of Steiner Trees on GPUs
](https://dl.acm.org/doi/abs/10.1007/s10766-021-00723-0)
