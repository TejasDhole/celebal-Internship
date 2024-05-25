from itertools import combinations


n = int(input())  
letters = input().split()  
k = int(input()) 

count_a = letters.count('a')

total_combinations = len(list(combinations(range(n), k)))

combinations_with_a = sum(1 for comb in combinations(range(n), k) if 'a' in [letters[i] for i in comb])

probability = combinations_with_a / total_combinations

print("{:.4f}".format(probability))
