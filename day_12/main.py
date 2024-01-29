from arrangement_counter import ArrangementCounter
from parser_strategy import DefaultParserStrategy, UnfoldParserStrategy


def read_file(file_path):
    with open(file_path) as file:
        content = file.readlines()
        
    return content


def main():
    data = read_file('day_12/input.txt')

    counter = ArrangementCounter(data, DefaultParserStrategy())
    total_arrangements = counter.count_total_arrangements()
    print(total_arrangements)

    counter = ArrangementCounter(data, UnfoldParserStrategy())
    total_arrangements = counter.count_total_arrangements()
    print(total_arrangements)


if __name__ == '__main__':
    main()