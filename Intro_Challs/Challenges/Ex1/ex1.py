input = 'abc'
shift = 2

output = ''
for c in input:
    output += chr(ord(c) + shift)

print(output)