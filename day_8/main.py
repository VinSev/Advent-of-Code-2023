from network_navigator import NetworkNavigator


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read().strip()

    return content


def main() -> None:
    data = read_file('day_8/input.txt')
    navigator = NetworkNavigator(data)
    result, lcm_result = navigator.navigate_network()
    
    print(result)
    print(lcm_result)


if __name__ == '__main__':
    main()
