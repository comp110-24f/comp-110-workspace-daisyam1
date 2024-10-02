"""Plans a tea party by calculating different variables"""

__author__: str = "730740592"


# prints result of all functions and end values
# calls functions and replaces "people" with "guests" as the argument
def main_planner(guests: int) -> None:
    """calls each function and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost((tea_bags(guests)), (treats(guests)))))


# each person gets 2 tea bags, so people * 2
def tea_bags(people: int) -> int:
    """calculates number of tea bags needed"""
    return people * 2


# need 1.5 treats for each tea that is drank, not for each person
def treats(people: int) -> int:
    """calculates number of treats needed"""
    return int((tea_bags(people)) * 1.5)


# each tea bag costs 50 cents and each treat costs 75 cents
def cost(tea_count: int, treat_count: int) -> float:
    """calculates cost of the tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


# makes input appear to define how many guests/people there are
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
