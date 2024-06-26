# Get input
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

# Process commands
for _ in range(num_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    elif command[0] == 'discard':
        s.discard(int(command[1]))

# Calculate and print the sum of the elements
print(sum(s))
