# Flight & Transit Journey Planner

[cite_start]A capstone project developed for **EF234405 Design & Analysis of Algorithms** (Classes D, IUP, E, F, G) at Sepuluh Nopember Institute of Technology (ITS)[cite: 1, 4, 5, 7]. 

[cite_start]This project explores the full workflow of algorithm design: formulating a real-world graph problem, proving its correctness, implementing structural solutions completely from scratch, and empirically measuring computational performance[cite: 9].

## 👥 Group Members & Contributions
* [cite_start]**Aldi** (Student ID: `5025241184`)


---

## 📌 Problem Formulation & Graph Abstraction
[cite_start]The application abstracts a global airline network into a directed, edge-weighted graph model defined as $\mathcal{G} = (V, E, w)$[cite: 20]:
* [cite_start]**Vertices ($V$):** Represent distinct airports or international transit hubs[cite: 21].
* [cite_start]**Edges ($E$):** Represent directed operational flight routes connecting individual airports[cite: 21].
* [cite_start]**Weights ($w$):** Represent the dynamic financial ticket price (in USD) or uniform scaling factors ($w=1$ for baseline hop evaluations)[cite: 21, 23].

[cite_start]We systematically compare two routing strategies to evaluate quality-versus-speed trade-offs[cite: 24]:
1.  [cite_start]**Algorithm A (Core):** Dijkstra's Algorithm backed by a proprietary, custom-built **Binary Min-Heap** prioritizer to find the absolute cheapest itinerary ($O((V+E)\log V)$)[cite: 22, 23, 228].
2.  [cite_start]**Algorithm B (Baseline):** Breadth-First Search (BFS) operating layer-by-layer to discover routes with the absolute fewest transits ($O(V+E)$)[cite: 23, 228].

[cite_start]*Note: All core algorithmic logic, adjacency lists, and priority heap queues are coded natively from scratch without reliance on network graph libraries (e.g., NetworkX) to guarantee structural ownership[cite: 31, 32].*

---

## 🛠️ Environmental Requirements
* [cite_start]**Language Environment:** Python [cite: 33]
* [cite_start]**Version Constraint:** Python 3.10 or higher (Optimized and tested on Python 3.13) [cite: 33]
* [cite_start]**Dependencies:** Standard Library Only (`time`, `random`, `collections.deque`) [cite: 31]
* **Execution Shell:** Bash, Command Prompt, or PowerShell

---

## 🚀 Deployment & Execution Guide
[cite_start]To satisfy reproducibility standards, a unified command sequence is available to clone, test, and regenerate all timing benchmark profiles under a fixed random seed (`seed=42`)[cite: 25, 29, 30].

