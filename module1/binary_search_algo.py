def binary_search(list, key):
     # If key is in the list returns its position in the list, otherwise -1.
     # But list must be sorted
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return f"Item on index: {middle}"
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return "Item not Found!"

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    find = int(input("What you want to find? "))
    print(binary_search(arr, find))

if __name__ == '__main__':
    main()