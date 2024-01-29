from typing import List, Tuple

from parsers import WorkflowParser, PartRatingParser
from workflow_executor import WorkflowExecutor
from workflow_counter import WorkflowCounter


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        content = file.read().strip()

    return content


def parse_file(data: str) -> Tuple[List[str], List[str]]:
    return data.split('\n\n')


def main():
    data = read_file('day_19/input.txt')
    workflow_lines, part_ratings  = parse_file(data)

    workflows = WorkflowParser().parse_workflow_lines(workflow_lines.splitlines())
    part_ratings = PartRatingParser().parse_part_ratings(part_ratings.splitlines())

    sum_of_executed_workflows = sum(WorkflowExecutor(part_rating).execute_workflow_rules(workflows) for part_rating in part_ratings)
    print(sum_of_executed_workflows)

    part_rating_ranges = {part_rating: (1, 4000) for part_rating in 'xmas'}
    count_of_accepted_workflows = WorkflowCounter(workflows).calculate_accepted_workflow_count(part_rating_ranges, 'in')
    print(count_of_accepted_workflows)

if __name__ == '__main__':
    main()