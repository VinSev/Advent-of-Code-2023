from typing import List, Tuple
import sympy

from hailstone import Hailstone, Position


class HailstonePositionFinder:
    @staticmethod
    def get_equations(hailstones: List[Hailstone]) -> Tuple[List[sympy.Eq], sympy.Symbol, sympy.Symbol, sympy.Symbol]:
        positions = sympy.symbols("pos_x pos_y pos_z", real=True)
        velocities = sympy.symbols("v_x v_y v_z", real=True)
        times_to_reach = sympy.symbols("time_to_reach_first time_to_reach_second time_to_reach_third", real=True)
        
        equations = []
        for i in range(3):
            hailstone = hailstones[i]
            position, velocity = hailstone.position, hailstone.velocity
            eq_x = sympy.Eq(positions[0] + velocities[0] * times_to_reach[i], position.x + velocity.x * times_to_reach[i])
            eq_y = sympy.Eq(positions[1] + velocities[1] * times_to_reach[i], position.y + velocity.y * times_to_reach[i])
            eq_z = sympy.Eq(positions[2] + velocities[2] * times_to_reach[i], position.z + velocity.z * times_to_reach[i])
            equations.extend([eq_x, eq_y, eq_z])
        
        return equations, *positions
    
    def find_stone_position(self, hailstones: List[Hailstone]) -> Position:
        
        equations, *positions = self.get_equations(hailstones)
        position_solution = sympy.solve(equations)[0]

        return Position(position_solution[positions[0]], position_solution[positions[1]], position_solution[positions[2]])