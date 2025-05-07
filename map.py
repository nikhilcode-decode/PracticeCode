def square(x): return x ** 2
def cube(x): return x ** 3
def double(x): return x * 2
def halve(x): return x / 2
def increment(x): return x + 1
def decrement(x): return x - 1
def negate(x): return -x
def reciprocal(x): return 1 / x if x != 0 else 0
def add_five(x): return x + 5
def subtract_three(x): return x - 3

operations = {
    1: ("Square", square),
    2: ("Cube", cube),
    3: ("Double", double),
    4: ("Halve", halve),
    5: ("Increment", increment),
    6: ("Decrement", decrement),
    7: ("Negate", negate),
    8: ("Reciprocal", reciprocal),
    9: ("Add 5", add_five),
    10: ("Subtract 3", subtract_three),
}

while True:
    print("\nEnter numbers separated by space (or type 'exit' to quit):")
    user_input = input("> ").strip()
    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    try:
        numbers = list(map(float, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Display operation menu
    print("\nSelect an operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("0. Exit")

    try:
        choice = int(input("Enter the operation number (0–10): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        print("Exiting program.")
        break
    elif choice in operations:
        op_name, op_func = operations[choice]
        result = list(map(op_func, numbers))
        print(f"\nResult after applying '{op_name}':")
        print(result)
    else:
        print("Invalid operation choice.")
