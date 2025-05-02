def get_set_input(prompt):
    """Helper function to get a set from user input."""
    return set(input(prompt).split())

def print_menu():
    print("\nChoose a set operation:")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (A - B)")
    print("4. Difference (B - A)")
    print("5. Symmetric Difference")
    print("6. Is A subset of B?")
    print("7. Is B subset of A?")
    print("8. Is A superset of B?")
    print("9. Is B superset of A?")
    print("10. Are A and B disjoint?")
    print("11. Add element to A")
    print("12. Add element to B")
    print("13. Remove element from A")
    print("14. Remove element from B")
    print("15. Pop element from A")
    print("16. Pop element from B")
    print("17. Clear A")
    print("18. Clear B")
    print("19. Copy A")
    print("20. Copy B")
    print("0. Exit")

def main():
    set_a = get_set_input("Enter elements of Set A (space-separated): ")
    set_b = get_set_input("Enter elements of Set B (space-separated): ")

    while True:
        print_menu()
        choice = input("Enter your choice (0-20): ")

        if choice == '1':
            print("Union:", set_a | set_b)
        elif choice == '2':
            print("Intersection:", set_a & set_b)
        elif choice == '3':
            print("Difference (A - B):", set_a - set_b)
        elif choice == '4':
            print("Difference (B - A):", set_b - set_a)
        elif choice == '5':
            print("Symmetric Difference:", set_a ^ set_b)
        elif choice == '6':
            print("A is subset of B:", set_a <= set_b)
        elif choice == '7':
            print("B is subset of A:", set_b <= set_a)
        elif choice == '8':
            print("A is superset of B:", set_a >= set_b)
        elif choice == '9':
            print("B is superset of A:", set_b >= set_a)
        elif choice == '10':
            print("A and B are disjoint:", set_a.isdisjoint(set_b))
        elif choice == '11':
            elem = input("Enter element to add to A: ")
            set_a.add(elem)
            print("Updated Set A:", set_a)
        elif choice == '12':
            elem = input("Enter element to add to B: ")
            set_b.add(elem)
            print("Updated Set B:", set_b)
        elif choice == '13':
            elem = input("Enter element to remove from A: ")
            set_a.discard(elem)
            print("Updated Set A:", set_a)
        elif choice == '14':
            elem = input("Enter element to remove from B: ")
            set_b.discard(elem)
            print("Updated Set B:", set_b)
        elif choice == '15':
            if set_a:
                print("Popped from A:", set_a.pop())
            else:
                print("Set A is empty.")
        elif choice == '16':
            if set_b:
                print("Popped from B:", set_b.pop())
            else:
                print("Set B is empty.")
        elif choice == '17':
            set_a.clear()
            print("Set A cleared.")
        elif choice == '18':
            set_b.clear()
            print("Set B cleared.")
        elif choice == '19':
            copied = set_a.copy()
            print("Copy of A:", copied)
        elif choice == '20':
            copied = set_b.copy()
            print("Copy of B:", copied)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
