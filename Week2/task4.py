def print_rangoli(size):
    # Importing string module to use ascii_lowercase
    import string
    
    # Get the lowercase alphabet list
    alpha = string.ascii_lowercase

    # Initialize a list to hold the lines of the rangoli
    lines = []

    # Generate each line of the rangoli
    for i in range(size):
        # Create the sequence of letters for this line
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        # Center the sequence and add to the list of lines
        lines.append(s.center(4*size-3, '-'))

    # Print the rangoli
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)