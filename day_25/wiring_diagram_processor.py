from igraph import Graph
from typing import Set, Tuple


class WiringDiagramProcessor:
    def __init__(self, data: str):
        self.vertexes, self.edges = self.parse_wiring_diagram(data)

    @staticmethod
    def parse_wiring_diagram(data: str) -> Tuple[Set[str], Set[Tuple[str, str]]]:
        wiring_diagram = data.split('\n')

        vertexes = set()
        edges = set()

        for connection in wiring_diagram:
            component_name, connected_components = connection.split(': ')
            connected_components = connected_components.split()

            vertexes.add(component_name)

            for connected_component in connected_components:
                vertexes.add(connected_component)
                edges.add((component_name, connected_component))

        return vertexes, edges

    def create_graph(self) -> Graph:
        graph = Graph()

        for vertex in self.vertexes:
            graph.add_vertex(vertex)

        for component_name, connected_component in self.edges:
            graph.add_edge(component_name, connected_component)

        return graph

    def calculate_product_of_groups(self) -> int:
        graph = self.create_graph()
        mincut = graph.mincut()
        
        return len(mincut.partition[0]) * len(mincut.partition[1])