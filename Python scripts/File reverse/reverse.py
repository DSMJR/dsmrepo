filename = 'text.txt'
thing = ''
handle = open(filename)
x = handle.readlines()
print(x)
cd = len(x)
print(cd)
output = open('Output.txt', 'a')
for g in x:
    cd = cd - 1
    thing = x[cd]
    output.write(thing)