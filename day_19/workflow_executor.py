from typing import Dict, List, Tuple

from workflow import Workflow

class WorkflowExecutor:
    def __init__(self, part_ratings: Dict[str, int]):
        self.part_ratings = part_ratings
        
    def apply_rules(self, workflow: Workflow, last_state: str) -> str:
        for part_rating_name, operator, comparison_value, next_state in workflow.rules:
            part_rating = self.part_ratings[part_rating_name]

            if (operator == '<' and part_rating < comparison_value) or (operator == '>' and part_rating > comparison_value):
                return next_state

        return last_state

    def execute_workflow_rules(self, workflows: List[Workflow]) -> int:
        current_workflow_state = 'in'

        while current_workflow_state not in ['A', 'R']:
            current_workflow = next((workflow for workflow in workflows if workflow.name == current_workflow_state), None)
            if current_workflow is None:
                break

            current_workflow_state = self.apply_rules(current_workflow, current_workflow.final_state)

        if current_workflow_state == 'A':
            return sum(self.part_ratings.values())

        return 0