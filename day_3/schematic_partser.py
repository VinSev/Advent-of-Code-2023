from typing import List


class SchematicParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_input_file(self) -> List[List[str]]:
        with open(self.file_path) as file:
            schematic = file.read().strip()
            return [[character for character in line] for line in schematic.split('\n')]