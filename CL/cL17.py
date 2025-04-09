"""example 1: grocery_list"""

grocery_list: list[str]  # declaring the type of a list
grocery_list: list[str] = (
    list()
)  # initializing a list with a constructor list(), a function that returns the literal[]
grocery_list: list[str] = (
    []
)  # initializing a list with a literal [], a function that returns the literal []
grocery_list: list[str] = [
    "apples",
    "bananas",
    "pears",
]  # declares the variable and initializes list to contain certain values
grocery_list.append("bananas")  # adds an item to the list, in this case "bananas"

"""example 2: my_numbers"""
my_numbers: list[float] = list()  # constructor, returns []
my_numbers: list[float] = []  # literal, returns []
print(my_numbers)  # returns [] because the list is empty
my_numbers.append(1.5)  # adds an item, in this case 1.5, to the list
print(my_numbers)  # returns [1.5] because <list name>.append(item) adds value to list


"""example 3: game_points"""
game_points: list[int] = [102, 86, 94]
print(game_points[2])  # prints the value 94 using subscription notation
game_points[1] = 72  # updates the value 86 to 72 using subscription notation
print(game_points)  # returns [102, 72, 94] because 86 changed to 72
print(len(game_points))  # returns 3 because there are 3 values in the list game_point
game_points.pop(
    1
)  # list_name.pop(index) removes value at index 1, which is 72, so returns (102,94)
