import argparse
import json

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("tank_size", type=int, help="Size of the tank (Gallons)")
    parser.add_argument("-l", "--loaches", type=validate_fish_count, default=0, help="Number of Clown Loaches")
    parser.add_argument("-o", "--oscars", type=validate_fish_count, default=0, help="Number of Oscars")
    parser.add_argument("-p", "--platies", type=validate_fish_count, default=0, help="Number of Platies")
    parser.add_argument("-r", "--rasboras", type=validate_fish_count, default=0, help="Number of Rasboras")
    parser.add_argument("-t", "--tetras", type=validate_fish_count, default=0, help="Number of Tetras")

    # Parse the arguments
    args = vars(parser.parse_args())
    tank_size = int(args.pop("tank_size"))
    fish_in_tank = cleanup_args(args)

    fish_data = get_fish_data("fish.json")  # Load fish data from json file

    # Check for problems
    problems = {
        "tank_size": check_tank_size(fish_data, fish_in_tank, tank_size),
        "compatibility": check_fish_compatibility(fish_data, fish_in_tank),
        "school_size": check_fish_school_size(fish_data, fish_in_tank),
        "fish_quantity_in_tank": check_fish_quantity_in_tank(fish_data, fish_in_tank, tank_size)
    }

    # Output problems
    if problems["tank_size"]:
        print("The following fish require a larger tank:")
        for fish in problems["tank_size"]:
            print(f"  - {fish}")
    if problems["compatibility"]:
        print("The following fish are incompatible with each other:")
        for fish in problems["compatibility"]:
            print(f"  - {fish[0]} and {fish[1]}")
    if problems["school_size"]:
        print("The following fish are not in an appropriate school size:")
        for status, fish in problems["school_size"]:
            if status == -1:
                print(f"  - {fish}: Too few")
            else:
                print(f"  - {fish}: Too many")
    if problems["fish_quantity_in_tank"]:
        print("There are too many fish for the tank size")

    if not any(problems.values()):
        print("No problems with stocking found!")


def validate_fish_count(value: str) -> int:
    """
    Used as type in argparse to validate number of fish input
    :param value: Value to check
    :return: Value as integer
    """
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a number")
    if ivalue < 0:
        raise argparse.ArgumentTypeError(f"'{value}' is an invalid number of fish")
    return ivalue

def cleanup_args(raw_args: dict) -> dict:
    """
    Removes any arguments that are less than or equal to 0
    :param raw_args: Raw arguments
    :return: Cleaned up arguments
    """
    return {k: v for k, v in raw_args.items() if v > 0}

def get_fish_data(json_file: str) -> dict:
    """
    Gets fish data from a json file
    :param json_file: Path to json file
    :return: Fish Data
    """
    with open(json_file, "r") as file:
        return json.load(file)

def check_tank_size(fish_data: dict, fish_in_tank: dict, tank_size: int) -> list:
    """
    Checks if the tank size is large enough
    :param fish_data: Fish Data (Loaded from json file)
    :param fish_in_tank: Fish in the tank
    :param tank_size: Size of the tank (Gallons)
    :return: List of fish that require a larger tank
    """
    problem_fish = []
    for fish in fish_in_tank.keys():  # Loop through fish in the tank
        if fish in fish_data:  # Check if fish is in the fish data
            if tank_size < fish_data[fish]["min-tank-size"]:  # Check if tank size is too small
                problem_fish.append(fish)
    return problem_fish

def check_fish_compatibility(fish_data: dict, fish_in_tank: dict) -> list:
    """
    Checks if the fish are compatible with each other
    :param fish_data: Fish Data (Loaded from json file)
    :param fish_in_tank: Fish in the tank
    :return: List of incompatible fish
    """
    problem_fish = []
    for fish in fish_in_tank.keys():  # Loop through fish in the tank
        if fish in fish_data:  # Check if fish is in the fish data
            for incompatible_fish in fish_data[fish]["incompatible"]:  # Loop through incompatible fish
                if incompatible_fish in fish_in_tank.keys():  # Check if incompatible fish is in the tank
                    if [incompatible_fish, fish] not in problem_fish:  # Check if the problem has already been added
                        problem_fish.append([fish, incompatible_fish])
    return problem_fish

def check_fish_school_size(fish_data: dict, fish_in_tank: dict) -> list:
    """
    Checks if the fish are in an appropriate school size
    :param fish_data: Fish Data (Loaded from json file)
    :param fish_in_tank: Fish in the tank
    :return: List of fish that are not in an appropriate school size (-1 = too small, 1 = too large)
    """
    problem_fish = []
    for fish, count in fish_in_tank.items():  # Loop through fish in the tank
        if fish in fish_data:  # Check if fish is in the fish data
            if count < fish_data[fish]["min-quantity"]:  # Check if school size is too small
                problem_fish.append([-1, fish])
            elif count > fish_data[fish]["max-quantity"] != -1:  # Check if school size is too large (-1 means no limit)
                problem_fish.append([1, fish])
    return problem_fish

def check_fish_quantity_in_tank(fish_data: dict, fish_in_tank: dict, tank_size: int) -> bool:
    """
    Checks if the total amount of fish is appropriate for the tank size (Based on 1-inch per gallon rule)
    :param fish_data: Fish Data (Loaded from json file)
    :param fish_in_tank: Fish in the tank
    :param tank_size: Size of the tank (Gallons)
    :return: False if the total amount of fish is appropriate, True if not
    """
    fish_size_count = 0
    for fish, count in fish_in_tank.items():
        if fish in fish_data:
            fish_size_count += fish_data[fish]["max-length"] * count
    return fish_size_count > tank_size


if __name__ == "__main__":
    main()
