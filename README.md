# Flight & Transit Journey Planner

A capstone project developed for **EF234405 Design & Analysis of Algorithms** (Classes E): Flight & Transit Journey Planner


## 👥 Group Members & Contributions
Naufaldi Faqih Abimanyu (Student ID: `5025241184`)


---

## 📌 Problem Formulation & Graph Abstraction
The application abstracts a global airline network into a directed, edge-weighted graph model defined as $\mathcal{G} = (V, E, w)$[cite: 20]:
Vertices ($V$):** Represent distinct airports or international transit hubs[cite: 21].
Edges ($E$):** Represent directed operational flight routes connecting individual airports[cite: 21].
Weights ($w$):** Represent the dynamic financial ticket price (in USD) or uniform scaling factors ($w=1$ for baseline hop evaluations)[cite: 21, 23].

We systematically compare two routing strategies to evaluate quality-versus-speed trade-offs[cite: 24]:
1.  Algorithm A (Core):** Dijkstra's Algorithm backed by a proprietary, custom-built **Binary Min-Heap** prioritizer to find the absolute cheapest itinerary ($O((V+E)\log V)$)[cite: 22, 23, 228].
2. Algorithm B (Baseline):** Breadth-First Search (BFS) operating layer-by-layer to discover routes with the absolute fewest transits ($O(V+E)$)[cite: 23, 228].

*Note: All core algorithmic logic, adjacency lists, and priority heap queues are coded natively from scratch without reliance on network graph libraries (e.g., NetworkX) to guarantee structural ownership[cite: 31, 32].*

Output: 

![imagealt](https://github.com/xaldinzz/Final-Exam-DAA/blob/main/image/Screenshot%202026-06-18%20184916.png?raw=true)

