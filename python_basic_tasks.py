# 1. Swap variables: a, b = 10, 20 → print swapped
a, b = 8, 9
print(f"before swap a : {a} , b: {b}")
a, b = b, a
print(f"after swap a: {a} , b: {b}")

# 2. Max of 3 numbers
a, b, c = 1, 2, 3
print(max(a, b, c))
print(max([a, b, c]))


# 3. Factorial recursive
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
factorial(5)


# 4. Filter even numbers from list
random_numbers = range(0, 300)
even_list = [n for n in random_numbers if n % 2 == 0]
print(even_list)


# 5. Simple calculator (add/sub/mul/div)
def basic_calculator(operation, p1, p2):
    if p1 is None or p2 is None:
        return "parameters missing"
    match operation:
        case "add":
            return sum([p1, p2])
        case "sub":
            return p1 - p2
        case "mul":
            return p1 * p2
        case "div":
            return p1 / p2
        case _:
            return "invalid operation"


operation = input("enter operation: ").strip()
p1_raw = input("enter p1: ").strip()
p2_raw = input("enter p2: ").strip()

try:
    p1 = float(p1_raw)
    p2 = float(p2_raw)

except ValueError:
    print("invalid inputs : only numbers allowed")

else:
    answer = basic_calculator(operation, p1, p2)
    print(answer)
