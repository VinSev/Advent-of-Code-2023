from lava_area_calculator import LavaAreaCalculator


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main():
    data = read_file('day_18/input.txt')
    
    area_calculator = LavaAreaCalculator(data)
    dig_plan = area_calculator.dig_plan

    trench = [direction[0] for direction in dig_plan]
    area_of_lava = area_calculator.calculate_lava_area(trench)
    print(area_of_lava)

    trench = [direction[1] for direction in dig_plan]
    area_of_lava = area_calculator.calculate_lava_area(trench)
    print(area_of_lava)


if __name__ == '__main__':
    main()
