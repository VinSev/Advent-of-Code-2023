from wiring_diagram_processor import WiringDiagramProcessor

    
def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()
        
    return content


def main() -> None:
    data = read_file('day_25/input.txt')
    
    product_of_groups = WiringDiagramProcessor(data).calculate_product_of_groups()
    print(product_of_groups)


if __name__ == '__main__':
    main()
