from binary_search import search


def main():
    arr = [1.5, 2.3, 3.7, 4.2, 5.9, 6.1, 7.8, 9.4]

    iterations, upper_bound = search(arr, 4.2)
    print(f"Search for 4.2: iterations={iterations}, upper_bound={upper_bound}")

    iterations, upper_bound = search(arr, 4.5)
    print(f"Search for 4.5: iterations={iterations}, upper_bound={upper_bound}")

    iterations, upper_bound = search(arr, 1.0)
    print(f"Search for 1.0: iterations={iterations}, upper_bound={upper_bound}")

    iterations, upper_bound = search(arr, 10.0)
    print(f"Search for 10.0: iterations={iterations}, upper_bound={upper_bound}")


if __name__ == "__main__":
    main()
