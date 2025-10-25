import time
import heapq
from typing import List, Dict, Tuple, Optional
import math

class Graph:
    """Lớp đại diện cho đồ thị vô hướng với trọng số"""
    
    def __init__(self):
        self.vertices = {}  # Tên thành phố -> index
        self.adjacency_matrix = []  # Ma trận kề
        self.vertex_names = []  # Danh sách tên các đỉnh theo thứ tự index
    
    def add_vertex(self, name: str) -> int:
        """Thêm một đỉnh mới vào đồ thị"""
        if name not in self.vertices:
            index = len(self.vertices)
            self.vertices[name] = index
            self.vertex_names.append(name)
            
            # Mở rộng ma trận kề
            for row in self.adjacency_matrix:
                row.append(float('inf'))
            self.adjacency_matrix.append([float('inf')] * (index + 1))
            
            # Đường chéo chính = 0
            self.adjacency_matrix[index][index] = 0
            
            return index
        return self.vertices[name]
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float):
        """Thêm cạnh giữa hai đỉnh"""
        from_idx = self.add_vertex(from_vertex)
        to_idx = self.add_vertex(to_vertex)
        
        self.adjacency_matrix[from_idx][to_idx] = weight
        self.adjacency_matrix[to_idx][from_idx] = weight
    
    def get_weight(self, from_idx: int, to_idx: int) -> float:
        """Lấy trọng số cạnh giữa hai đỉnh"""
        return self.adjacency_matrix[from_idx][to_idx]
    
    def get_vertex_count(self) -> int:
        """Lấy số lượng đỉnh"""
        return len(self.vertices)

class TSPBranchBoundSolver:
    """Thuật toán nhánh cận để giải bài toán TSP"""
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.n = graph.get_vertex_count()
        self.best_cost = float('inf')
        self.best_path = []
        self.nodes_explored = 0
        
    def solve(self) -> Dict:
        """Giải bài toán TSP và trả về kết quả"""
        start_time = time.time()
        
        if self.n < 2:
            return {
                'route': [self.graph.vertex_names[0]] if self.n == 1 else [],
                'total_distance': 0,
                'execution_time': 0,
                'nodes_explored': 0
            }
        
        # Khởi tạo
        self.best_cost = float('inf')
        self.best_path = []
        self.nodes_explored = 0
        
        # Tạo ma trận chi phí
        cost_matrix = self._create_cost_matrix()
        
        # Tính cận dưới ban đầu
        initial_lower_bound = self._calculate_initial_lower_bound(cost_matrix)
        
        # Bắt đầu tìm kiếm nhánh cận
        initial_path = [0]  # Bắt đầu từ đỉnh 0
        initial_cost = 0
        initial_visited = set([0])
        
        self._branch_and_bound(
            cost_matrix, 
            initial_path, 
            initial_cost, 
            initial_visited, 
            initial_lower_bound
        )
        
        execution_time = time.time() - start_time
        
        # Chuyển đổi kết quả từ index sang tên thành phố
        route_names = [self.graph.vertex_names[i] for i in self.best_path]
        
        return {
            'route': route_names,
            'total_distance': self.best_cost,
            'execution_time': execution_time,
            'nodes_explored': self.nodes_explored
        }
    
    def _create_cost_matrix(self) -> List[List[float]]:
        """Tạo ma trận chi phí từ đồ thị"""
        cost_matrix = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if i == j:
                    row.append(0)
                else:
                    weight = self.graph.get_weight(i, j)
                    row.append(weight if weight != float('inf') else float('inf'))
            cost_matrix.append(row)
        return cost_matrix
    
    def _calculate_initial_lower_bound(self, cost_matrix: List[List[float]]) -> float:
        """Tính cận dưới ban đầu bằng phương pháp cận dưới đơn giản"""
        total = 0
        
        # Tính tổng cận dưới cho mỗi hàng
        for i in range(self.n):
            row = [cost_matrix[i][j] for j in range(self.n) if i != j]
            if row:
                total += min(row)
        
        return total / 2  # Chia 2 vì mỗi cạnh được tính 2 lần
    
    def _calculate_lower_bound(self, cost_matrix: List[List[float]], 
                              path: List[int], visited: set) -> float:
        """Tính cận dưới cho trạng thái hiện tại"""
        if len(path) == self.n:
            # Đã thăm hết tất cả đỉnh, cần quay về đỉnh đầu
            return cost_matrix[path[-1]][path[0]]
        
        total = 0
        
        # Tính cận dưới cho các đỉnh đã thăm
        for i in range(len(path) - 1):
            total += cost_matrix[path[i]][path[i + 1]]
        
        # Tính cận dưới cho các đỉnh chưa thăm
        unvisited = set(range(self.n)) - visited
        
        for i in unvisited:
            # Tìm cạnh ngắn nhất từ đỉnh i đến các đỉnh chưa thăm khác
            min_out = float('inf')
            for j in unvisited:
                if i != j and cost_matrix[i][j] < min_out:
                    min_out = cost_matrix[i][j]
            
            # Tìm cạnh ngắn nhất từ các đỉnh chưa thăm khác đến đỉnh i
            min_in = float('inf')
            for j in unvisited:
                if i != j and cost_matrix[j][i] < min_in:
                    min_in = cost_matrix[j][i]
            
            if min_out != float('inf') and min_in != float('inf'):
                total += (min_out + min_in) / 2
        
        return total
    
    def _branch_and_bound(self, cost_matrix: List[List[float]], 
                         path: List[int], current_cost: float, 
                         visited: set, lower_bound: float):
        """Thuật toán nhánh cận chính"""
        self.nodes_explored += 1
        
        # Kiểm tra điều kiện dừng
        if lower_bound >= self.best_cost:
            return  # Cắt nhánh
        
        if len(path) == self.n:
            # Đã thăm hết tất cả đỉnh, kiểm tra xem có thể quay về đỉnh đầu không
            if cost_matrix[path[-1]][path[0]] != float('inf'):
                total_cost = current_cost + cost_matrix[path[-1]][path[0]]
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.best_path = path.copy()
            return
        
        # Tạo các nhánh con
        unvisited = set(range(self.n)) - visited
        current_vertex = path[-1]
        
        # Sắp xếp các đỉnh chưa thăm theo chi phí tăng dần
        candidates = []
        for next_vertex in unvisited:
            if cost_matrix[current_vertex][next_vertex] != float('inf'):
                new_cost = current_cost + cost_matrix[current_vertex][next_vertex]
                new_path = path + [next_vertex]
                new_visited = visited | {next_vertex}
                new_lower_bound = self._calculate_lower_bound(cost_matrix, new_path, new_visited)
                
                candidates.append((new_lower_bound, new_cost, new_path, new_visited))
        
        # Sắp xếp theo cận dưới tăng dần
        candidates.sort(key=lambda x: x[0])
        
        # Khám phá các nhánh theo thứ tự ưu tiên
        for lower_bound, cost, new_path, new_visited in candidates:
            if lower_bound < self.best_cost:
                self._branch_and_bound(cost_matrix, new_path, cost, new_visited, lower_bound)

# Hàm tiện ích để tạo dữ liệu mẫu
def create_sample_data():
    """Tạo dữ liệu mẫu về các thành phố Việt Nam"""
    cities = [
        {'name': 'Hà Nội'},
        {'name': 'TP. Hồ Chí Minh'},
        {'name': 'Đà Nẵng'},
        {'name': 'Hải Phòng'},
        {'name': 'Cần Thơ'},
        {'name': 'Nha Trang'},
        {'name': 'Huế'},
        {'name': 'Vũng Tàu'}
    ]
    
    distances = [
        {'from': 'Hà Nội', 'to': 'Hải Phòng', 'weight': 102},
        {'from': 'Hà Nội', 'to': 'Đà Nẵng', 'weight': 764},
        {'from': 'Hà Nội', 'to': 'Huế', 'weight': 688},
        {'from': 'Hà Nội', 'to': 'TP. Hồ Chí Minh', 'weight': 1726},
        {'from': 'Hải Phòng', 'to': 'Đà Nẵng', 'weight': 662},
        {'from': 'Đà Nẵng', 'to': 'Huế', 'weight': 103},
        {'from': 'Đà Nẵng', 'to': 'Nha Trang', 'weight': 531},
        {'from': 'Huế', 'to': 'TP. Hồ Chí Minh', 'weight': 1038},
        {'from': 'Nha Trang', 'to': 'TP. Hồ Chí Minh', 'weight': 441},
        {'from': 'TP. Hồ Chí Minh', 'to': 'Vũng Tàu', 'weight': 95},
        {'from': 'TP. Hồ Chí Minh', 'to': 'Cần Thơ', 'weight': 169},
        {'from': 'Cần Thơ', 'to': 'Nha Trang', 'weight': 610}
    ]
    
    return cities, distances
