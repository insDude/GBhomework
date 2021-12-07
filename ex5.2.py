words = 0
lines = 0
f = open('2.txt', 'r')
for line in f:
    lines += 1
    word = line.split()
    words = len(word)
f.close()
print(lines)
print(words)

