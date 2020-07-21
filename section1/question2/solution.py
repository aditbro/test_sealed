class Graph:
    def __init__(self, name: str, weight: int) -> 'Graph':
        self.name: str = name
        self.weight: int = weight
        self.max_weight: int = None
        self.max_path: int = None
        self.children: [Graph] = []

    def add_child(self, child: 'Graph') -> None:
        self.children.append(child)

def make_graph(inp: str) -> Graph:
    inp = inp.split('\n')
    n_vert, n_edge, start = inp[0].split(' ')
    n_vert = int(n_vert)
    n_edge = int(n_edge)

    graphs = {}

    for i in range(1, 1 + n_vert):
        name, weight = inp[i].split(' ')
        weight = int(weight)
        graphs[name] = Graph(name, weight)

    for i in range(1 + n_vert, 1 + n_vert + n_edge):
        origin, dest = inp[i].split('->')
        graphs[origin].add_child(graphs[dest])

    return graphs[start]

def find_max_path_val(node: Graph) -> (str, int):
    if len(node.children) == 0:
        node.max_path = node.name
        node.max_weight = node.weight
        return (node.name, node.weight)
    
    max_weight: int = None
    max_path: str = None

    for child in node.children:
        weight: int
        path: str
        
        if child.max_weight:
            weight = child.max_weight
            path = child.max_path
        else:
            path, weight = find_max_path_val(child)
        
        if not max_weight:
            max_weight = weight
            max_path = path
        else:
            if max_weight < weight:
                max_weight = weight
                max_path = path

    max_path = node.name + '->' + max_path
    max_weight = node.weight + max_weight

    node.max_path = max_path
    node.max_weight = max_weight

    return (max_path, max_weight)

def solution(inp: str) -> str:
    start_graph = make_graph(inp)
    path, val = find_max_path_val(start_graph)

    return '{} {}'.format(path, val)
