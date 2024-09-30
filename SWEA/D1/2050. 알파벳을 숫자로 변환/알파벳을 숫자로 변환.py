s = input().strip()

for char in s:
    print(ord(char) - ord('A') + 1, end=' ')
