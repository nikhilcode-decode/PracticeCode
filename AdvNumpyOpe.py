import numpy as np

def input_array(prompt="Enter array elements (space-separated): "):
    while True:
        try:
            data = input(prompt)
            flat_list = list(map(float, data.strip().split()))
            size = int(input("How many rows? "))
            if len(flat_list) % size != 0:
                raise ValueError("Number of elements does not match the specified number of rows.")
            arr = np.array(flat_list).reshape((size, -1))
            return arr
        except Exception as e:
            print("Error in array input:", e)

def display_menu():
    print("""
=== Advanced NumPy Operations Menu ===
1. Identity Matrix
2. Diagonal Matrix from List
3. Extract Diagonal
4. Boolean Indexing (e.g., > 0)
5. Fancy Indexing by indices
6. Broadcasting (Add a row)
7. Outer Product of two vectors
8. Cross Product of 2 vectors
9. Inverse of Matrix
10. Determinant of Matrix
11. Eigenvalues & Eigenvectors
12. Rank of Matrix
13. Pseudoinverse
14. Clip Values
15. Replace NaN with Zero
16. Conditional Replace (<0 → 0)
17. Vertical Stack
18. Horizontal Stack
19. Split Array
20. Exit
""")

def main():
    print("Input your base array:")
    arr = input_array()

    while True:
        display_menu()
        try:
            choice = int(input("Select operation (1-20): "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            n = int(input("Size of identity matrix: "))
            print(np.eye(n))

        elif choice == 2:
            diag = list(map(float, input("Enter diagonal values: ").split()))
            print(np.diag(diag))

        elif choice == 3:
            print("Diagonal:", np.diag(arr))

        elif choice == 4:
            val = float(input("Enter threshold (e.g., 0): "))
            print("Filtered Elements:\n", arr[arr > val])

        elif choice == 5:
            try:
                indices = list(map(int, input("Enter flat indices: ").split()))
                print("Selected Elements:", arr.flat[indices])
            except Exception as e:
                print("Invalid indices:", e)

        elif choice == 6:
            row = np.array(list(map(float, input("Enter row to broadcast: ").split())))
            print("Broadcasted Array:\n", arr + row)

        elif choice == 7:
            a = np.array(list(map(float, input("Vector A: ").split())))
            b = np.array(list(map(float, input("Vector B: ").split())))
            print("Outer Product:\n", np.outer(a, b))

        elif choice == 8:
            a = np.array(list(map(float, input("Vector A (size 3): ").split())))
            b = np.array(list(map(float, input("Vector B (size 3): ").split())))
            print("Cross Product:", np.cross(a, b))

        elif choice == 9:
            try:
                print("Inverse:\n", np.linalg.inv(arr))
            except np.linalg.LinAlgError:
                print("Matrix not invertible.")

        elif choice == 10:
            print("Determinant:", np.linalg.det(arr))

        elif choice == 11:
            vals, vecs = np.linalg.eig(arr)
            print("Eigenvalues:", vals)
            print("Eigenvectors:\n", vecs)

        elif choice == 12:
            print("Matrix Rank:", np.linalg.matrix_rank(arr))

        elif choice == 13:
            print("Pseudoinverse:\n", np.linalg.pinv(arr))

        elif choice == 14:
            min_val = float(input("Clip Min: "))
            max_val = float(input("Clip Max: "))
            print("Clipped Array:\n", np.clip(arr, min_val, max_val))

        elif choice == 15:
            arr_nan = arr.copy()
            arr_nan[0][0] = np.nan
            print("With NaN:\n", arr_nan)
            print("Replaced NaN:\n", np.nan_to_num(arr_nan))

        elif choice == 16:
            print("Conditionally Replaced (<0 to 0):\n", np.where(arr < 0, 0, arr))

        elif choice == 17:
            a = input_array("Enter another array to stack vertically:\n")
            try:
                print("Vertically Stacked:\n", np.vstack((arr, a)))
            except ValueError as e:
                print("Shapes do not align:", e)

        elif choice == 18:
            a = input_array("Enter another array to stack horizontally:\n")
            try:
                print("Horizontally Stacked:\n", np.hstack((arr, a)))
            except ValueError as e:
                print("Shapes do not align:", e)

        elif choice == 19:
            parts = int(input("How many splits? "))
            try:
                print("Split Arrays:")
                for part in np.array_split(arr, parts):
                    print(part)
            except ValueError as e:
                print("Error splitting array:", e)

        elif choice == 20:
            print("Thank You! Exiting program.")
            break

        else:
            print("Invalid option. Please choose 1–20.")

if __name__ == "__main__":
    main()
