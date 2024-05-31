import re

def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    regex = input().strip()
    print(is_valid_regex(regex))
