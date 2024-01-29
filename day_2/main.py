from cube_inventory import CubeInventory


def main() -> None:
    with open('day_2/input.txt', 'r') as file:
        games = file.readlines()

    cube_inventory = CubeInventory()
    cube_inventory.process_games(games)

    print(cube_inventory.sum_of_game_ids)
    print(cube_inventory.sum_of_minimum_sets)


if __name__ == "__main__":
    main()
