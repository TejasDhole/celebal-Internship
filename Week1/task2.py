from itertools import groupby

s = input().strip()

result = [(len(list(g)), int(k)) for k, g in groupby(s)]

print(' '.join(f'({count}, {char})' for count, char in result))
