def display_menu():
    print("\nChoose an operation:")
    print("1. Add a key-value pair")
    print("2. Update a value")
    print("3. Delete a key")
    print("4. Check if key exists")
    print("5. Get value by key")
    print("6. Get all keys")
    print("7. Get all values")
    print("8. Get all items")
    print("9. Clear dictionary")
    print("10. Copy dictionary")
    print("11. Merge another dictionary")
    print("12. Pop a key")
    print("13. Popitem (last item)")
    print("14. Set default")
    print("15. Get dictionary length")
    print("16. Create from keys")
    print("17. Check if dictionary is empty")
    print("18. Print dictionary")
    print("19. Sort by key")
    print("20. Reverse dictionary")
    print("21. Create nested dictionary")
    print("22. Access nested value")
    print("23. Remove nested key")
    print("24. Use dictionary comprehension")
    print("25. Get min value key")
    print("26. Get max value key")
    print("27. Count specific value")
    print("28. Convert to list of tuples")
    print("29. Convert list of tuples to dict")
    print("30. Exit")


my_dict = {}

for _ in range(30):
    display_menu()
    choice = input("Enter choice (1–30): ")

    if choice == '1':
        k = input("Enter key: ")
        v = input("Enter value: ")
        my_dict[k] = v

    elif choice == '2':
        k = input("Enter key to update: ")
        if k in my_dict:
            v = input("Enter new value: ")
            my_dict[k] = v
        else:
            print("Key not found.")

    elif choice == '3':
        k = input("Enter key to delete: ")
        my_dict.pop(k, None)

    elif choice == '4':
        k = input("Enter key to check: ")
        print("Exists" if k in my_dict else "Does not exist.")

    elif choice == '5':
        k = input("Enter key: ")
        print("Value:", my_dict.get(k, "Key not found."))

    elif choice == '6':
        print("Keys:", list(my_dict.keys()))

    elif choice == '7':
        print("Values:", list(my_dict.values()))

    elif choice == '8':
        print("Items:", list(my_dict.items()))

    elif choice == '9':
        my_dict.clear()
        print("Dictionary cleared.")

    elif choice == '10':
        print("Copied dictionary:", my_dict.copy())

    elif choice == '11':
        other = {}
        n = int(input("How many items to merge? "))
        for _ in range(n):
            k = input("Enter key: ")
            v = input("Enter value: ")
            other[k] = v
        my_dict.update(other)

    elif choice == '12':
        k = input("Enter key to pop: ")
        print("Popped:", my_dict.pop(k, "Key not found."))

    elif choice == '13':
        print("Popped item:", my_dict.popitem() if my_dict else "Empty dict")

    elif choice == '14':
        k = input("Enter key: ")
        default = input("Enter default value: ")
        print("Set default:", my_dict.setdefault(k, default))

    elif choice == '15':
        print("Length:", len(my_dict))

    elif choice == '16':
        keys = input("Enter comma-separated keys: ").split(",")
        default = input("Enter default value: ")
        my_dict = dict.fromkeys(keys, default)

    elif choice == '17':
        print("Empty" if not my_dict else "Not empty")

    elif choice == '18':
        print("Dictionary:", my_dict)

    elif choice == '19':
        print("Sorted by key:", dict(sorted(my_dict.items())))

    elif choice == '20':
        print("Reversed dict:", dict(reversed(list(my_dict.items()))))

    elif choice == '21':
        outer_key = input("Enter outer key: ")
        inner_key = input("Enter inner key: ")
        inner_value = input("Enter inner value: ")
        my_dict[outer_key] = {inner_key: inner_value}
        print("Nested dict created.")

    elif choice == '22':
        outer_key = input("Outer key: ")
        inner_key = input("Inner key: ")
        try:
            print("Nested value:", my_dict[outer_key][inner_key])
        except:
            print("Nested key not found.")

    elif choice == '23':
        outer_key = input("Outer key: ")
        inner_key = input("Inner key to remove: ")
        try:
            del my_dict[outer_key][inner_key]
            print("Removed nested key.")
        except:
            print("Invalid key.")

    elif choice == '24':
        try:
            n = int(input("Create squares up to: "))
            my_dict = {str(i): i*i for i in range(1, n+1)}
            print("Created with comprehension.")
        except:
            print("Invalid number.")

    elif choice == '25':
        try:
            min_k = min(my_dict, key=my_dict.get)
            print("Key with min value:", min_k)
        except:
            print("Error (non-numeric values?)")

    elif choice == '26':
        try:
            max_k = max(my_dict, key=my_dict.get)
            print("Key with max value:", max_k)
        except:
            print("Error (non-numeric values?)")

    elif choice == '27':
        v = input("Value to count: ")
        count = list(my_dict.values()).count(v)
        print(f"'{v}' occurs {count} time(s)")

    elif choice == '28':
        print("List of tuples:", list(my_dict.items()))

    elif choice == '29':
        t = eval(input("Enter list of tuples (e.g., [('a',1),('b',2)]): "))
        if isinstance(t, list):
            my_dict = dict(t)
            print("Converted to dictionary.")
        else:
            print("Invalid input.")

    elif choice == '30':
        print("Exiting.")
        break

    else:
        print("Invalid choice.")
