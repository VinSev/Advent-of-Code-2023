from pattern_analyzer import PatternAnalyzer


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_file('day_13/input.txt')
    pattern_analyzer = PatternAnalyzer(data)

    total_reflection = pattern_analyzer.analyze_reflection(False)
    print(total_reflection)

    total_reflection = pattern_analyzer.analyze_reflection(True)
    print(total_reflection)


if __name__ == '__main__':
    main()
