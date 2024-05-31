def perform_division():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # First line is the number of test cases
    number_of_cases = int(data[0])
    
    results = []
    for i in range(1, number_of_cases + 1):
        a, b = data[i].split()
        try:
            result = int(a) // int(b)
            results.append(str(result))
        except ZeroDivisionError as e:
            results.append(f"Error Code: {e}")
        except ValueError as e:
            results.append(f"Error Code: {e}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    perform_division()
