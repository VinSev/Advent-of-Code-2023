from schematic_partser import SchematicParser
from part_counter import PartCounter
from gear_ratios_calculator import GearRatiosCalculator, TwoCountsGearRatioStrategy


def main() -> None:
    input_file_path = 'day_3/input.txt'
    schematic_parser = SchematicParser(input_file_path)
    schematic_grid = schematic_parser.parse_input_file()

    part_counter = PartCounter(schematic_grid)
    sum_part_counts, parts = part_counter.count_parts()
    print(f'Sum of Part Counts: {sum_part_counts}')

    strategies = [TwoCountsGearRatioStrategy()]
    gear_ratios = GearRatiosCalculator(parts, strategies)
    sum_gear_ratios = gear_ratios.calculate_gear_ratios()
    print(f'Sum of Gear Ratios: {sum_gear_ratios}')


if __name__ == '__main__':
    main()
