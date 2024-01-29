from typing import Dict, List, Tuple

from workflow import Workflow


class WorkflowParser:
    @staticmethod
    def parse_workflow_rule(rule: str) -> Tuple[str, str, int, str]:
        expression, next_state = rule.split(':')
        return expression[0], expression[1], int(expression[2:]), next_state

    def parse_workflow_lines(self, workflow_lines: List[str]) -> List[Workflow]:
        workflows = []

        for workflow_line in workflow_lines:
            name, rules = workflow_line.split('{')
            rules = rules.strip()[:-1].split(',')

            rules, final_state = rules[:-1], rules[-1]
            rules = [self.parse_workflow_rule(rule) for rule in rules]

            workflow = Workflow(name, rules, final_state)
            workflows.append(workflow)

        return workflows


class PartRatingParser:
    @staticmethod
    def parse_part_ratings(part_ratings: List[str]) -> List[Dict[str, int]]:
        parsed_part_ratings = []

        for line in part_ratings:
            assignments = line[1:-1].split(',')
            part_rating_assignments = {part_rating: int(value) for part_rating, value in (assignment.split('=') for assignment in assignments)}
            parsed_part_ratings.append(part_rating_assignments)

        return parsed_part_ratings