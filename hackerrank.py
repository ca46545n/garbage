n = raw_input()

split = map(int, n.split())

first = None
second = None
for n in split:
    if n > first:
        first, second = n, first
    elif first > n > second:
        second = n

print second