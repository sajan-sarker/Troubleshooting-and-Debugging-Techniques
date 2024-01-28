def linear_search(list, key):
     # If key is in the list returns its position in the list, otherwise -1.
    for x, item in enumerate(list):
        if item == key:
            return f"At index: {x}"
    return "Item not Found!"

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    find = int(input("What you want to find? "))
    print(linear_search(arr, find))

if __name__ == '__main__':
    main()