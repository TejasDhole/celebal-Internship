def merge_the_tools(string, k):
    # Iterate over the string in steps of k
    for i in range(0, len(string), k):
        # Extract a substring of length k
        substring = string[i:i + k]
        
        # Use an ordered set to maintain the order of first occurrence
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        
        # Join the result list into a string and print it
        print(''.join(result))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)