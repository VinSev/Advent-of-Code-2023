from typing import List, Dict, Tuple
from math import lcm
from itertools import cycle


class NetworkNavigator:
    START_NODE_STRING: str = 'AAA'
    END_NODE_STRING: str = 'ZZZ'

    def __init__(self, data_file: str) -> None:
        self.instructions: List[int]
        self.network: Dict[str, List[str]]
        self.instructions, self.network = self.parse_map(data_file)

    def parse_map(self, data: str) -> Tuple[List[int], Dict[str, List[str]]]:
        instruction_data, network_data = data.split('\n\n')

        instructions = self.parse_instructions(instruction_data)
        network = self.parse_network(network_data)

        return instructions, network

    @staticmethod
    def parse_instructions(instruction_data: str) -> List[int]:
        return [0 if instruction == 'L' else 1 for instruction in instruction_data]

    @staticmethod
    def parse_network(network_data: str) -> Dict[str, List[str]]:
        network = {}

        for line in network_data.splitlines():
            node, destinations = line.split('=')
            node = node.strip()
            destinations = destinations.replace(
                '(', ' ').replace(')', ' ').replace(',', ' ').split()
            network[node] = destinations

        return network

    def have_all_nodes_reached_end(self, end_steps):
        return all(z > 0 for z in end_steps)

    def has_node_reached_end(self, end_steps, index, node):
        return end_steps[index] < 0 and node[-1] == self.END_NODE_STRING[2]

    def get_starting_nodes(self) -> List[str]:
        return [node for node in self.network.keys() if node[-1] == self.START_NODE_STRING[2]]

    def calculate_steps(self, current_nodes: List[str], start_index: int, end_steps: List[int]) -> Tuple[int, int]:
        steps = 0

        for instruction in cycle(self.instructions):
            current_nodes = [self.network[node][instruction] for node in current_nodes]
            steps += 1

            for index, node in enumerate(current_nodes):
                if self.has_node_reached_end(end_steps, index, node):
                    end_steps[index] = steps

            if self.have_all_nodes_reached_end(end_steps):
                break

        result = end_steps[start_index]
        lcm_result = lcm(*[step for step in end_steps])

        return result, lcm_result

    def navigate_network(self) -> Tuple[int, int]:
        starting_nodes = self.get_starting_nodes()
        start_index = starting_nodes.index(self.START_NODE_STRING)
        end_steps = [-1 for _ in starting_nodes]

        return self.calculate_steps(starting_nodes, start_index, end_steps)
