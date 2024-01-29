


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_file('day_0/input.txt')
    print(data)


if __name__ == '__main__':
    main()
