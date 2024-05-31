from collections import Counter

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    # Reading the number of items in the inventory
    index = 0
    n = int(data[index])
    index += 1
    
    # Reading the inventory items
    inventory_items = list(map(int, data[index:index+n]))
    index += n
    
    # Creating a Counter object to count occurrences in the inventory
    inventory = Counter(inventory_items)
    
    # Reading the number of transactions
    m = int(data[index])
    index += 1
    
    # Process each transaction
    total_earnings = 0
    for _ in range(m):
        quantity = int(data[index])
        price = int(data[index+1])
        index += 2
        
        # If the item is available in the inventory
        if inventory[quantity] > 0:
            total_earnings += price
            inventory[quantity] -= 1  # Reduce the count of the item in the inventory
    
    print(total_earnings)

if __name__ == '__main__':
    solve()
