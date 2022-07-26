#program that writes the first four powers of the numbers between 1 &
# 1,000 to a text file using comma-separated fields

# with open("exercise1.txt", "w") as f:
#     for i in range(1, 1001):
#         print(i, i**2, i**3, i**4, sep=", ", file=f)

# f = open("exercise1.txt", "r")

#correction, another way:

def write_powers_to_file(file_path, n_numbers=1000):
    """Writes the first four powers of each number to the given text file

    Args:
        file_path (_type_): _description_
        n_numbers (int, optional): _description_
    """
    with open(file_path, "w") as f:
        for i in range(1, n_numbers + 1):
            print(i, i**2, i**3, i**4, sep=",", file=f)

def read_cubes_from_file(file_path, low=100, high=200):
    """Reads all the cubes of numbers from low to high from the text file

    Args:
        file_path (_type_): _description_
        low(int): defaults 100
        high(int): defaults 200
    """
    with open(file_path) as f:
        for line in f:
            numbers = line.split(",")
            numbers = [int(num) for num in numbers]
            if low <= numbers[0] <= high:
                print(numbers[0], numbers[2])
            if numbers[0] == high:
                break

POWERS_FILE = "powers.txt"
# write_powers_to_file(POWERS_FILE)
read_cubes_from_file(POWERS_FILE)