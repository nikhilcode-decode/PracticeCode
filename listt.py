def display_menu():
    print("\n====== List Operations Menu ======")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index of Element")
    print("8. Count Occurrences")
    print("9. Reverse")
    print("10. Sort Ascending")
    print("11. Sort Descending")
    print("12. Copy List")
    print("13. Length of List")
    print("14. Check if Item Exists")
    print("15. Concatenate Another List")
    print("16. Multiply List")
    print("17. Slice List")
    print("18. Minimum Element")
    print("19. Maximum Element")
    print("20. Sum of Elements")
    print("0. Exit")

def main():
    my_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (0-20): ")

        if choice == '1':
            item = input("Enter item to append: ")
            my_list.append(item)
        elif choice == '2':
            items = input("Enter elements separated by space: ").split()
            my_list.extend(items)
        elif choice == '3':
            item = input("Enter item to insert: ")
            pos = int(input("Enter position to insert at: "))
            my_list.insert(pos, item)
        elif choice == '4':
            item = input("Enter item to remove: ")
            if item in my_list:
                my_list.remove(item)
            else:
                print("Item not found.")
        elif choice == '5':
            if my_list:
                print("Popped:", my_list.pop())
            else:
                print("List is empty.")
        elif choice == '6':
            my_list.clear()
            print("List cleared.")
        elif choice == '7':
            item = input("Enter item to find index: ")
            if item in my_list:
                print("Index:", my_list.index(item))
            else:
                print("Item not found.")
        elif choice == '8':
            item = input("Enter item to count: ")
            print("Count:", my_list.count(item))
        elif choice == '9':
            my_list.reverse()
            print("List reversed.")
        elif choice == '10':
            try:
                my_list.sort()
                print("List sorted in ascending order.")
            except TypeError:
                print("Cannot sort list with mixed data types.")
        elif choice == '11':
            try:
                my_list.sort(reverse=True)
                print("List sorted in descending order.")
            except TypeError:
                print("Cannot sort list with mixed data types.")
        elif choice == '12':
            copied_list = my_list.copy()
            print("Copied list:", copied_list)
        elif choice == '13':
            print("Length of list:", len(my_list))
        elif choice == '14':
            item = input("Enter item to check: ")
            print("Exists in list:" , item in my_list)
        elif choice == '15':
            items = input("Enter elements of second list separated by space: ").split()
            my_list += items
        elif choice == '16':
            times = int(input("Enter how many times to repeat the list: "))
            my_list *= times
        elif choice == '17':
            start = int(input("Start index: "))
            end = int(input("End index: "))
            print("Sliced list:", my_list[start:end])
        elif choice == '18':
            try:
                print("Minimum:", min(my_list))
            except:
                print("Cannot find minimum. Ensure list has comparable elements.")
        elif choice == '19':
            try:
                print("Maximum:", max(my_list))
            except:
                print("Cannot find maximum. Ensure list has comparable elements.")
        elif choice == '20':
            try:
                print("Sum:", sum(map(float, my_list)))
            except:
                print("Sum operation failed. Ensure all items are numeric.")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

        print("Current List:", my_list)

if __name__ == "__main__":
    main()
