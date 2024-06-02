from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    graph = Graph()
    for node in [
        'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z','z','1A','1B','1C','1D','1E','1F','1G','1H','1J',
        '1M','1K','2A','2B','2C','2D','2E','2F','2G','2L','2H','2J','2K','3A','3D','3C',
        '3E','3F','3G','3L','3H','3J','3K','5M','5E','5L','5A','6M','6E','6L', '6A', 'a', 
        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
        'r','s', 't', 'u', 'v', 'w', 'x', 'z'
    ]:
        graph.add_node(node)
    
    graph.add_edge('G', 'F', 48.13)
    graph.add_edge('G', '1F', 56.94)
    graph.add_edge('F', 'E', 15.95)
    graph.add_edge('E', '1D', 25.54)
    graph.add_edge('F', '1B', 66.53)
    graph.add_edge('D', '1B', 8.45)
    graph.add_edge('E', '1B', 19.12)
    graph.add_edge('E', '1E', 46.74)
    graph.add_edge('1E', '1F', 57.97)
    graph.add_edge('E', 'D', 17.04)
    graph.add_edge('D', 'C', 9.45)
    graph.add_edge('C', 'B', 9.50)
    graph.add_edge('B', 'A', 9.46)
    graph.add_edge('A', '1A', 6.34)
    graph.add_edge('1C', 'D', 6.46)
    graph.add_edge('H', '1A', 29.05)
    graph.add_edge('H', 'C', 11.31)
    graph.add_edge('H', '1C', 25.05)
    graph.add_edge('H', '1D', 25.39)
    graph.add_edge('1D', '1C', 19.99)
    graph.add_edge('1D', '1E', 31.65)
    graph.add_edge('1A', '1D', 57.67)
    graph.add_edge('E', '1C', 36.96)
    graph.add_edge('F', '1F', 59.04)
    graph.add_edge('1E', 'J', 30.57)
    graph.add_edge('1E', 'ID', 50.03)
    graph.add_edge('1F', 'I', 9.41)
    graph.add_edge('I', 'J', 42.89)
    graph.add_edge('1F', '1G', 27.80)
    graph.add_edge('1G', 'J', 61.45)
    graph.add_edge('J', '1K', 73.27)
    graph.add_edge('J', '1J', 82.77)
    graph.add_edge('1H', '1J', 5.37)
    graph.add_edge('1H', 'J', 94.57)
    graph.add_edge('1H', '1K', 33.34)
    graph.add_edge('1J', '1K', 30.24)
    graph.add_edge('1K', '1M', 5.38)
    graph.add_edge('1M', 'J', 67.90)
    graph.add_edge('1M', '1H', 30.24)
    graph.add_edge('1H', 'K', 16.33)
    graph.add_edge('1J', 'K', 27.05)
    graph.add_edge('1A', '1H', 182.12)
    graph.add_edge('P', '2B', 15.41)
    graph.add_edge('2B', 'O', 8.36)
    graph.add_edge('2B', '2C', 24.27)
    graph.add_edge('O', '2C', 6.46)
    graph.add_edge('O', 'N', 9.45)
    graph.add_edge('N', 'M', 9.50)
    graph.add_edge('M', 'L', 9.46)
    graph.add_edge('L', '2A', 6.34)
    graph.add_edge('2A', '2D', 57.67)
    graph.add_edge('2A', '2L', 73.34)
    graph.add_edge('2D', '2L', 72.34)
    graph.add_edge('2C', 'Q', 19.60)
    graph.add_edge('2D', '2C', 19.99)
    graph.add_edge('2D', 'Q', 32.38)
    graph.add_edge('2D', '2E', 31.65)
    graph.add_edge('2E', '2F', 59.44)
    graph.add_edge('2F', 'z', 3.81)
    graph.add_edge('2F', 'R', 14.65)
    graph.add_edge('R', '2G', 9.63)
    graph.add_edge('2E', '2L', 24.89)
    graph.add_edge('2E', '2G', 83.88)
    graph.add_edge('2G', '2K', 122.97)
    graph.add_edge('2E', '2K', 73.27)
    graph.add_edge('2E', '2H', 98.64)
    graph.add_edge('2H', '2J', 5.37)
    graph.add_edge('2K', '2J', 25.37)
    graph.add_edge('2H', '2L', 108.76)
    graph.add_edge('2H', '2K', 33.34)
    graph.add_edge('2H', '2G', 45.34)
    graph.add_edge('2L', '2F', 102.26)
    graph.add_edge('2G', '2L', 41.90)
    graph.add_edge('3A', 'S', 6.34)
    graph.add_edge('S', 'T', 9.45)
    graph.add_edge('T', 'U', 9.50)
    graph.add_edge('U', 'V', 9.46)
    graph.add_edge('V', '3C', 6.46)
    graph.add_edge('3A', '3L', 73.34)
    graph.add_edge('3C', '3D', 19.99)
    graph.add_edge('3A', '3D', 67.66)
    graph.add_edge('3D', '3L', 72.74)
    graph.add_edge('3D', '3E', 31.65)
    graph.add_edge('3E', '3F', 59.44)
    graph.add_edge('3L', '3F', 102.26)
    graph.add_edge('3E', '3L', 24.28)
    graph.add_edge('3F', '3G', 41.90)
    graph.add_edge('3G', '3L', 122.97)
    graph.add_edge('3G', '3K', 33.34)
    graph.add_edge('3K', '3H', 45.34)
    graph.add_edge('3G', '3H', 98.64)
    graph.add_edge('3E', '3H', 5.37)
    graph.add_edge('3H', '3J', 108.76)
    graph.add_edge('3H', '3L', 25.37)
    graph.add_edge('3J', '3K', 8.02)
    graph.add_edge('5M', 'a', 8.05)
    graph.add_edge('a', 'b', 8.05)
    graph.add_edge('b', 'c', 8.05)
    graph.add_edge('c', 'd', 8.05)
    graph.add_edge('d', 'e', 8.06)
    graph.add_edge('e', 'f', 10.31)
    graph.add_edge('f', 'W', 8.04)
    graph.add_edge('W', '5E', 24.10)
    graph.add_edge('W', 'X', 7.14)
    graph.add_edge('X', '5L', 13.71)
    graph.add_edge('X', 'g', 10.31)
    graph.add_edge('g', 'h', 7.09)
    graph.add_edge('h', 'i', 7.09)
    graph.add_edge('i', 'j', 7.10)
    graph.add_edge('j', 'k', 7.10)
    graph.add_edge('k', 'l', 7.10)
    graph.add_edge('l', '5A', 12.58)
    graph.add_edge('6M', 'm', 8.02)
    graph.add_edge('m', 'n', 8.05)
    graph.add_edge('n', 'o', 8.05)
    graph.add_edge('o', 'p', 8.06)
    graph.add_edge('p', 'q', 8.04)
    graph.add_edge('q', 'r', 8.10)
    graph.add_edge('r', 'Y', 10.31)
    graph.add_edge('Y', '6E', 7.43)
    graph.add_edge('Y', 'Z', 24.10)
    graph.add_edge('Z', '6L', 7.14)
    graph.add_edge('Z', 's', 13.71)
    graph.add_edge('s', 't', 10.31)
    graph.add_edge('t', 'u', 7.09)
    graph.add_edge('u', 'v', 7.08)
    graph.add_edge('v', 'w', 7.10)
    graph.add_edge('w', 'x', 7.10)
    graph.add_edge('x', '6A', 12.58)
    graph.add_edge('1A', '2A', 4.98)
    graph.add_edge('2A', '3A', 5.12)
    graph.add_edge('3A', '5A', 14.66)
    graph.add_edge('5A', '6A', 7.35)
    graph.add_edge('1B', '2B', 4.98)
    graph.add_edge('1C', '2C', 4.98)
    graph.add_edge('2C', '3C', 5.12)
    graph.add_edge('1D', '2D', 4.98)
    graph.add_edge('2D', '3D', 5.12)
    graph.add_edge('1E', '2E', 4.98)
    graph.add_edge('2E', '3E', 5.12)
    graph.add_edge('3E', '5E', 14.66)
    graph.add_edge('5E', '6E', 7.35)
    graph.add_edge('1F', '2F', 4.98)
    graph.add_edge('2F', '3F', 5.12)
    graph.add_edge('1G', '2G', 4.98)
    graph.add_edge('2G', '3G', 5.12)
    graph.add_edge('1M', '5M', 24.76)
    graph.add_edge('5M', '6M', 7.35)
    graph.add_edge('1H', '2H', 4.98)
    graph.add_edge('2H', '3H', 5.12)
    graph.add_edge('1J', '2J', 4.98)
    graph.add_edge('2J', '3J', 5.12)
    graph.add_edge('1K', '2K', 4.98)
    graph.add_edge('2K', '3K', 5.12)
    graph.add_edge('2L', '3L', 35.12)
    graph.add_edge('3L', '5L', 14.66)
    graph.add_edge('5L', '6L', 7.35)
    
    print(shortest_path(graph, 'G', 'F'))
