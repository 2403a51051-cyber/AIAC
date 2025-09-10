def find_common(a, b):
    """Return a list of common elements between two lists using set intersection."""
    return list(set(a) & set(b))

if __name__ == "__main__":
    list1 = input("Enter the first list (space-separated): ").split()
    list2 = input("Enter the second list (space-separated): ").split()
    common = find_common(list1, list2)
    print("Common elements:", common)