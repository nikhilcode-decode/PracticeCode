import numpy as np

def get_array():
    data = input("Enter elements of the array separated by spaces: ")
    arr = np.array(list(map(float, data.split())))
    return arr

def menu():
    print("\n=== NumPy Menu ===")
    print("1. Reshape")
    print("2. Transpose")
    print("3. Mean")
    print("4. Median")
    print("5. Standard Deviation")
    print("6. Variance")
    print("7. Sort")
    print("8. Max")
    print("9. Min")
    print("10. Sum")
    print("11. Cumulative Sum")
    print("12. Unique Elements")
    print("13. Dot Product")
    print("14. Matrix Multiplication")
    print("15. Flatten")
    print("16. Square Root")
    print("17. Power")
    print("18. Replace Element")
    print("19. Slice Array")
    print("20. Exit")

def main():
    print("Create your array:")
    arr = get_array()

    while True:
        menu()
        choice = int(input("Enter your choice (1-20): "))

        if choice == 1:
            shape = tuple(map(int, input("Enter new shape (e.g., 2 3): ").split()))
            try:
                print("Reshaped Array:\n", arr.reshape(shape))
            except:
                print("Invalid shape for this array.")
        elif choice == 2:
            try:
                print("Transposed:\n", arr.T)
            except:
                print("Transpose not possible.")
        elif choice == 3:
            print("Mean:", np.mean(arr))
        elif choice == 4:
            print("Median:", np.median(arr))
        elif choice == 5:
            print("Standard Deviation:", np.std(arr))
        elif choice == 6:
            print("Variance:", np.var(arr))
        elif choice == 7:
            print("Sorted Array:", np.sort(arr))
        elif choice == 8:
            print("Maximum:", np.max(arr))
        elif choice == 9:
            print("Minimum:", np.min(arr))
        elif choice == 10:
            print("Sum:", np.sum(arr))
        elif choice == 11:
            print("Cumulative Sum:", np.cumsum(arr))
        elif choice == 12:
            print("Unique Elements:", np.unique(arr))
        elif choice == 13:
            b = get_array()
            if arr.size == b.size:
                print("Dot Product:", np.dot(arr, b))
            else:
                print("Arrays must be the same size for dot product.")
        elif choice == 14:
            rows = int(input("Enter number of rows for first matrix: "))
            arr1 = arr.reshape((rows, -1))
            b = get_array()
            try:
                cols = arr1.shape[1]
                arr2 = b.reshape((cols, -1))
                print("Matrix Multiplication:\n", np.matmul(arr1, arr2))
            except:
                print("Matrix dimensions mismatch.")
        elif choice == 15:
            print("Flattened Array:", arr.flatten())
        elif choice == 16:
            print("Square Roots:", np.sqrt(arr))
        elif choice == 17:
            power = float(input("Enter the power: "))
            print("Powered Array:", np.power(arr, power))
        elif choice == 18:
            old = float(input("Enter value to replace: "))
            new = float(input("Enter new value: "))
            print("Updated Array:", np.where(arr == old, new, arr))
        elif choice == 19:
            start = int(input("Start index: "))
            end = int(input("End index: "))
            print("Sliced Array:", arr[start:end])
        elif choice == 20:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
