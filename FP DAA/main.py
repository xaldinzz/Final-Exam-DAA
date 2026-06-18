import time
import random
from collections import deque

class MinHeap:
    """Manual Min-Heap implementation to optimize Dijkstra's Algorithm."""
    def __init__(self):
        self.heap = []

    def push(self, element):
        self.heap.append(element)
        self._up_heap(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._down_heap(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0

    def _up_heap(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._up_heap(parent)

    def _down_heap(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._down_heap(smallest)


class FlightGraph:
    """Flight Network Graph representation using an Adjacency List."""
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}

    def add_flight(self, u, v, price):
        self.adj_list[u].append((v, price))

def solve_dijkstra(graph, source, target):
    """Algorithm A: Dijkstra finds the route with the CHEAPEST TOTAL PRICE."""
    inf = float('inf')
    prices = [inf] * graph.V
    parent = [-1] * graph.V
    
    prices[source] = 0
    pq = MinHeap()
    pq.push((0, source))
    
    while not pq.is_empty():
        current_price, u = pq.pop()
        if current_price > prices[u]:
            continue
            
        if u == target:
            break
            
        for neighbor, flight_price in graph.adj_list[u]:
            if prices[u] + flight_price < prices[neighbor]:
                prices[neighbor] = prices[u] + flight_price
                parent[neighbor] = u
                pq.push((prices[neighbor], neighbor))
    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    
    return prices[target], path if prices[target] != inf else []


def solve_bfs(graph, source, target):
    """Algorithm B: BFS finds the route with the FEWEST TRANSITS (MIN-HOPS)."""
    visited = [False] * graph.V
    parent = [-1] * graph.V
    
    queue = deque([source])
    visited[source] = True
    
    found = False
    while queue:
        u = queue.popleft()
        if u == target:
            found = True
            break
            
        for neighbor, _ in graph.adj_list[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = u
                queue.append(neighbor)

    if not found and source != target:
        return float('inf'), []
        
    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    total_price = 0
    for i in range(len(path) - 1):
        u_curr = path[i]
        v_next = path[i+1]
        for neighbor, price in graph.adj_list[u_curr]:
            if neighbor == v_next:
                total_price += price
                break
                
    return total_price, path

def generate_random_transit_data(num_airports, edges_per_airport, seed=42):
    """Generates synthetic large-scale network data to meet scale constraints."""
    random.seed(seed)  
    graph = FlightGraph(num_airports)
    
    for u in range(num_airports):
        targets = random.sample(range(num_airports), min(edges_per_airport, num_airports))
        for v in targets:
            if u != v:
                price = random.randint(50, 500)
                graph.add_flight(u, v, price)
    return graph


def run_benchmark():
    """Benchmark framework measuring execution runtime for Report Section 3."""
    print("===============================================================")
    print("Starting Algorithm Performance Benchmark...")
    print("===============================================================")
    input_sizes = [100, 500, 1000, 3000, 5000]
    
    print(f"{'Vertices':<10} | {'Dijkstra (ms)':<15} | {'BFS (ms)':<15} | {'Quality Trade-off (Total Price)'}")
    print("-" * 80)
    
    for size in input_sizes:

        graph = generate_random_transit_data(num_airports=size, edges_per_airport=10)
        source_node = 0
        target_node = size - 1
        start_time = time.perf_counter()
        dijkstra_price, _ = solve_dijkstra(graph, source_node, target_node)
        end_time = time.perf_counter()
        dijkstra_duration = (end_time - start_time) * 1000 
        start_time = time.perf_counter()
        bfs_price, _ = solve_bfs(graph, source_node, target_node)
        end_time = time.perf_counter()
        bfs_duration = (end_time - start_time) * 1000
        
        print(f"{size::<10} | {dijkstra_duration:<15.4f} | {bfs_duration:<15.4f} | "
              f"Dijkstra: ${dijkstra_price:,} vs BFS: ${bfs_price:,}")

if __name__ == "__main__":

    print("--- TRANSIT PLANNER DEMO (SMALL-SCALE SAMPLE) ---")
    demo_graph = FlightGraph(5)

    demo_graph.add_flight(0, 1, 100)  # Sub -> Jkt ($100)
    demo_graph.add_flight(1, 4, 700)  # Jkt -> Tky ($700)
    demo_graph.add_flight(0, 2, 150)  # Sub -> Sgp ($150)
    demo_graph.add_flight(2, 3, 80)   # Sgp -> KL  ($80)
    demo_graph.add_flight(3, 4, 300)  # KL -> Tky  ($300)
    
    src, tgt = 0, 4
    
    d_price, d_path = solve_dijkstra(demo_graph, src, tgt)
    print(f"\n[Algorithm A - Dijkstra (Cheapest Route)]")
    print(f"-> Total Optimized Price : ${d_price:,}")
    print(f"-> Flight Path Chosen    : {' -> '.join(map(str, d_path))}")
    b_price, b_path = solve_bfs(demo_graph, src, tgt)
    print(f"\n[Algorithm B - BFS (Fewest Transits / Min-Hops Route)]")
    print(f"-> Total Path Price      : ${b_price:,}")
    print(f"-> Flight Path Chosen    : {' -> '.join(map(str, b_path))}")
    print(f"Clear quality-versus-speed trade-off observed: BFS picks a fast path (1 transit) but expensive, "
          f"whereas Dijkstra is cheaper via KL despite requiring 2 transits!\n")
    run_benchmark()