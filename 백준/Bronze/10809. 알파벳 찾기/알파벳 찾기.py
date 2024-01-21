import string

text = input()
counter = []
for lo in string.ascii_lowercase:
    counter.append(str(text.find(lo)))

print(' '.join(counter))