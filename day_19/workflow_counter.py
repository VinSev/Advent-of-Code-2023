from typing import Dict, List, Tuple

from workflow import Workflow


class WorkflowCounter:
    def __init__(self, workflows: List[Workflow]):
        self.workflows = workflows
    
    def process_workflow_rules(
        self,
        part_rating_ranges: Dict[str, Tuple[int, int]],
        part_rating: str,
        operator: str,
        comparison_value: int,
        next_state: str
    ) -> int:
        lower_bound, upper_bound = part_rating_ranges[part_rating]
        total_accepted_count = 0

        if operator == '<':
            total_accepted_count += self.calculate_accepted_count_for_less_than_operator(
                part_rating_ranges, part_rating, comparison_value, next_state
            )
            part_rating_ranges[part_rating] = max(lower_bound, comparison_value), upper_bound

        elif operator == '>':
            total_accepted_count += self.calculate_accepted_count_for_greater_than_operator(
                part_rating_ranges, part_rating, comparison_value, next_state
            )
            part_rating_ranges[part_rating] = lower_bound, min(upper_bound, comparison_value)

        return total_accepted_count

    def calculate_accepted_workflow_count(
        self,
        part_rating_ranges: Dict[str, Tuple[int, int]],
        current_workflow_state: str
    ) -> int:
        if current_workflow_state == 'A':
            return self.calculate_accepted_count_for_all_part_ratings(part_rating_ranges)

        if current_workflow_state == 'R':
            return 0

        current_workflow = next((w for w in self.workflows if w.name == current_workflow_state), None)
        if current_workflow is None:
            return 0

        total_accepted_count = 0

        for part_rating, operator, comparison_value, next_state in current_workflow.rules:
            total_accepted_count += self.process_workflow_rules(
                part_rating_ranges, part_rating, operator, comparison_value, next_state
            )

        total_accepted_count += self.calculate_accepted_workflow_count(part_rating_ranges, current_workflow.final_state)

        return total_accepted_count

    def calculate_accepted_count_for_all_part_ratings(
        self,
        part_rating_ranges: Dict[str, Tuple[int, int]]
    ) -> int:
        count = 1

        for lower_bound, upper_bound in part_rating_ranges.values():
            count *= upper_bound - lower_bound + 1

        return count

    def calculate_accepted_count_for_less_than_operator(
        self,
        part_rating_ranges: Dict[str, Tuple[int, int]],
        part_rating: str,
        comparison_value: int,
        next_state: str
    ) -> int:
        lower_bound, _ = part_rating_ranges[part_rating]

        if lower_bound < comparison_value:
            part_rating_ranges[part_rating] = (lower_bound, comparison_value - 1)

            return self.calculate_accepted_workflow_count(dict(part_rating_ranges), next_state)

    def calculate_accepted_count_for_greater_than_operator(
        self,
        part_rating_ranges: Dict[str, Tuple[int, int]],
        part_rating: str,
        comparison_value: int,
        next_state: str
    ) -> int:
        _, upper_bound = part_rating_ranges[part_rating]

        if upper_bound > comparison_value:
            part_rating_ranges[part_rating] = (comparison_value + 1, upper_bound)

            return self.calculate_accepted_workflow_count(dict(part_rating_ranges), next_state)