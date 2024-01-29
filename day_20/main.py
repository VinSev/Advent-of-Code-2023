from tile_parser import TileParser
from tile_processor import TileProcessor


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_file('day_20/input.txt')
    tile_types, tile_connections, receiver_inputs = TileParser().parse_tiles(data)
    tile_processor = TileProcessor(tile_types, tile_connections, receiver_inputs)
    tile_processor.process_tiles()


if __name__ == '__main__':
    main()
