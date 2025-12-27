from hash_table import HashTable


def main():
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    H.delete("orange")

    print(H.get("apple"))
    print(H.get("orange"))


if __name__ == "__main__":
    main()
