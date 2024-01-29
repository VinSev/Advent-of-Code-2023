from typing import List

from grid_solver import GridSolver
    
    
def read_file(file_path: str) -> List[str]:
    with open(file_path) as file:
        content = file.readlines()
        
    return content


def main() -> None:
    data = read_file('day_21/input.txt')
    solver = GridSolver(data)
    result = solver.calculate_final_result()
    print(result)
    

if __name__ == "__main__":
    main()