if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
   
tuple_values = tuple(integer_list)

result = hash(tuple_values)

print(result)
