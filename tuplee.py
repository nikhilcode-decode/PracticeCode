def get_tuple_input(prompt="Enter comma-separated values for the tuple: "):
    raw = input(prompt)
    return tuple(raw.strip().split(','))

def menu():
    print("\n==== TUPLE OPERATIONS MENU ====")
    print("1. Create a new tuple")
    print("2. Display the tuple")
    print("3. Length of tuple")
    print("4. Access element by index")
    print("5. Slice the tuple")
    print("6. Repeat the tuple")
    print("7. Check membership")
    print("8. Concatenate another tuple")
    print("9. Convert to list")
    print("10. Convert list to tuple")
    print("11. Count an element")
    print("12. Index of an element")
    print("13. Unpack tuple")
    print("14. Max value (numeric only)")
    print("15. Min value (numeric only)")
    print("16. Sort the tuple (as list)")
    print("17. Reverse the tuple")
    print("18. Create a tuple of tuples")
    print("19. Check if all elements are digits")
    print("20. Join elements into a string")
    print("0. Exit")
    print("===============================")

tuple_data = ()
list_data = []

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        tuple_data = get_tuple_input()
        print("Tuple created:", tuple_data)

    elif choice == '2':
        print("Current tuple:", tuple_data)

    elif choice == '3':
        print("Length of tuple:", len(tuple_data))

    elif choice == '4':
        index = int(input("Enter index: "))
        print("Element at index", index, ":", tuple_data[index])

    elif choice == '5':
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Tuple slice:", tuple_data[start:end])

    elif choice == '6':
        times = int(input("Enter number of repetitions: "))
        print("Repeated tuple:", tuple_data * times)

    elif choice == '7':
        item = input("Enter item to check: ")
        print("Membership:", item in tuple_data)

    elif choice == '8':
        new_tuple = get_tuple_input("Enter another tuple to concatenate: ")
        tuple_data += new_tuple
        print("Concatenated tuple:", tuple_data)

    elif choice == '9':
        list_data = list(tuple_data)
        print("Converted to list:", list_data)

    elif choice == '10':
        tuple_data = tuple(list_data)
        print("Converted back to tuple:", tuple_data)

    elif choice == '11':
        element = input("Enter element to count: ")
        print("Count:", tuple_data.count(element))

    elif choice == '12':
        element = input("Enter element to find index: ")
        if element in tuple_data:
            print("Index of element:", tuple_data.index(element))
        else:
            print("Element not found.")

    elif choice == '13':
        if len(tuple_data) >= 2:
            a, b, *rest = tuple_data
            print("Unpacked:", "First:", a, "Second:", b, "Rest:", rest)
        else:
            print("Not enough elements to unpack.")

    elif choice == '14':
        try:
            nums = tuple(map(float, tuple_data))
            print("Max value:", max(nums))
        except:
            print("Tuple contains non-numeric values.")

    elif choice == '15':
        try:
            nums = tuple(map(float, tuple_data))
            print("Min value:", min(nums))
        except:
            print("Tuple contains non-numeric values.")

    elif choice == '16':
        print("Sorted tuple as list:", sorted(tuple_data))

    elif choice == '17':
        print("Reversed tuple:", tuple(reversed(tuple_data)))

    elif choice == '18':
        new_tuple = get_tuple_input("Enter another tuple: ")
        print("Tuple of tuples:", (tuple_data, new_tuple))

    elif choice == '19':
        print("All elements are digits?", all(item.isdigit() for item in tuple_data))

    elif choice == '20':
        print("Joined elements:", ', '.join(tuple_data))

    elif choice == '0':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
