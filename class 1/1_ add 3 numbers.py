# function add 3 numbers together
def add_three_numbers(num1, num2, num3):
    three_added_numbers = num1 + num2 + num3
    return three_added_numbers


def get_numbers():
    numbers = []
    count = 0
    print("Enter 3 numbers. ")
    while count < 3:
        count += 1
        number = int(input(f"Enter the number {count}: "))
        numbers.append(number)
    return numbers


def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum


def print_sum(total_sum):
    print("The total sum of the numbers is: ", total_sum)


# CALL ALL 3 SUM
numbers = get_numbers()
total_sum = calculate_sum(numbers)
print_sum(total_sum)


